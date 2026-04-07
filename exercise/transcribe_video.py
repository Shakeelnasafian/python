import sys
import argparse
from pathlib import Path
from datetime import timedelta
from tqdm import tqdm

try:
    from faster_whisper import WhisperModel
except ImportError:
    print("Please install faster-whisper: pip install faster-whisper")
    sys.exit(1)

def ts_srt(seconds: float) -> str:
    ms = int(round(seconds * 1000))
    h = ms // 3_600_000
    m = (ms % 3_600_000) // 60_000
    s = (ms % 60_000) // 1000
    ms = ms % 1000
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

def write_txt(path: Path, segments):
    with path.open("w", encoding="utf-8") as f:
        for s in segments:
            f.write(s["text"].strip() + "\n")

def write_srt(path: Path, segments):
    with path.open("w", encoding="utf-8") as f:
        for i, s in enumerate(segments, start=1):
            f.write(f"{i}\n{ts_srt(s['start'])} --> {ts_srt(s['end'])}\n{s['text'].strip()}\n\n")

# def run_whisper(model: WhisperModel, in_path: Path, task: str, language: str|None,
#                 vad: bool, beam_size: int):
#     segments_iter, info = model.transcribe(
#         str(in_path),
#         task=task,                 # "transcribe" (original language) or "translate" (to English)
#         language=language,         # None = auto-detect; set "ar" to force Arabic, "en" to force English, etc.
#         vad_filter=vad,
#         beam_size=beam_size,
#     )
#     segs = []
#     for seg in segments_iter:
#         segs.append({"start": seg.start, "end": seg.end, "text": seg.text})
#     return segs, info

def run_whisper(model: WhisperModel, in_path: Path, task: str, language: str|None,
                vad: bool, beam_size: int):
    segments_iter, info = model.transcribe(
        str(in_path),
        task=task,
        language=language,
        vad_filter=vad,
        beam_size=beam_size,
    )

    total_duration = getattr(info, "duration", None)  # duration in seconds (if available)
    segs = []

    if total_duration:  # if we know total duration, show progress
        with tqdm(total=total_duration, unit="sec", desc=f"{task.capitalize()} Progress") as pbar:
            for seg in segments_iter:
                segs.append({"start": seg.start, "end": seg.end, "text": seg.text})
                pbar.update(seg.end - (segs[-2]['end'] if len(segs) > 1 else 0))
    else:  # fallback if duration not available
        for seg in tqdm(segments_iter, desc=f"{task.capitalize()} Progress", unit="segment"):
            segs.append({"start": seg.start, "end": seg.end, "text": seg.text})

    return segs, info


def main():
    p = argparse.ArgumentParser(description="Transcribe video/audio (mixed Arabic/English) with faster-whisper.")
    p.add_argument("input", help="Path to video/audio file (.mp4, .mov, .mkv, .m4a, .mp3, .wav, ...)")
    p.add_argument("--model", default="small", help="tiny, base, small, medium, large-v3 (default: small)")
    p.add_argument("--device", default="auto", help="auto, cpu, cuda, or metal")
    p.add_argument("--compute-type", default="auto", help="auto, int8, int8_float16, int16, float16, float32")
    p.add_argument("--language", default=None, help="Force language code (e.g., ar, en). Leave empty to auto-detect.")
    p.add_argument("--vad", action="store_true", help="Enable voice activity detection")
    p.add_argument("--beam-size", type=int, default=5, help="Beam size (default: 5)")
    group = p.add_mutually_exclusive_group()
    group.add_argument("--translate-only", action="store_true",
                       help="Only produce English translation (no original-language files)")
    group.add_argument("--bilingual", action="store_true",
                       help="Produce both original-language and English translation outputs")
    args = p.parse_args()

    in_path = Path(args.input)
    if not in_path.exists():
        print(f"Input not found: {in_path}")
        sys.exit(1)

    # Output stems
    stem = in_path.with_suffix("")  # drop extension
    orig_txt = stem.with_suffix(".txt")
    orig_srt = stem.with_suffix(".srt")
    en_txt = stem.with_name(stem.name + ".en").with_suffix(".txt")
    en_srt = stem.with_name(stem.name + ".en").with_suffix(".srt")

    # Load model
    device = None if args.device == "auto" else args.device
    print(f"Loading model '{args.model}'...")
    model = WhisperModel(args.model, device=device or "auto", compute_type=args.compute_type)

    # Decide what to generate
    want_original = not args.translate_only  # default: produce original-language files
    want_english  = args.translate_only or args.bilingual

    # 1) Original-language transcription
    if want_original:
        print(f"Transcribing (original language): {in_path.name}")
        orig_segments, orig_info = run_whisper(
            model, in_path, task="transcribe", language=args.language, vad=args.vad, beam_size=args.beam_size
        )
        write_txt(orig_txt, orig_segments)
        write_srt(orig_srt, orig_segments)
        print(f"Detected primary language: {orig_info.language} (prob={orig_info.language_probability:.2f})")
        print(f"Saved: {orig_txt}\nSaved: {orig_srt}")

    # 2) English translation (regardless of source language)
    if want_english:
        print(f"Translating to English: {in_path.name}")
        en_segments, en_info = run_whisper(
            model, in_path, task="translate", language=None, vad=args.vad, beam_size=args.beam_size
        )
        write_txt(en_txt, en_segments)
        write_srt(en_srt, en_segments)
        print(f"Saved (English): {en_txt}\nSaved (English): {en_srt}")

if __name__ == "__main__":
    main()
