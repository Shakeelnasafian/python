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

def format_timestamp(seconds: float) -> str:
    total_ms = int(round(seconds * 1000))
    hours = total_ms // 3_600_000
    minutes = (total_ms % 3_600_000) // 60_000
    secs = (total_ms % 60_000) // 1000
    ms = total_ms % 1000
    return f"{hours:02}:{minutes:02}:{secs:02},{ms:03}"

def write_txt(path: Path, segments):
    with path.open("w", encoding="utf-8") as f:
        for s in segments:
            f.write(s["text"].strip() + "\n")

def write_srt(path: Path, segments):
    with path.open("w", encoding="utf-8") as f:
        for i, s in enumerate(segments, start=1):
            f.write(f"{i}\n{format_timestamp(s['start'])} --> {format_timestamp(s['end'])}\n{s['text'].strip()}\n\n")

def main():
    p = argparse.ArgumentParser(description="Transcribe audio/video to TXT & SRT using faster-whisper.")
    p.add_argument("input", help="Path to input file (.m4a, .mp3, .wav, .mp4, etc.)")
    p.add_argument("--model", default="small", help="tiny, base, small, medium, large-v3 (default: small)")
    p.add_argument("--device", default="auto", help="auto, cpu, cuda, or metal")
    p.add_argument("--compute-type", default="auto", help="auto, int8, int8_float16, int16, float16, float32")
    p.add_argument("--language", default=None, help="Force language (e.g., en, ar). Leave empty to auto-detect.")
    p.add_argument("--vad", action="store_true", help="Enable voice activity detection")
    p.add_argument("--beam-size", type=int, default=5, help="Beam size (default: 5)")
    p.add_argument("--no-translate", dest="no_translate", action="store_true",
                   help="Keep original language (don’t translate to English)")
    args = p.parse_args()

    in_path = Path(args.input)
    if not in_path.exists():
        print(f"Input not found: {in_path}")
        sys.exit(1)

    # Output paths
    stem = in_path.with_suffix("")
    txt_out = stem.with_suffix(".txt")
    srt_out = stem.with_suffix(".srt")

    # Choose device
    device = None if args.device == "auto" else args.device

    print(f"Loading model '{args.model}'...")
    model = WhisperModel(args.model, device=device or "auto", compute_type=args.compute_type)

    print(f"Transcribing: {in_path.name}")
    # Task selection: default = transcribe; only translate if user wants English and audio isn’t already English
    task = "transcribe" if args.no_translate else "transcribe"
    # If you explicitly want English regardless of source language, you could do:
    # task = "translate" if (not args.no_translate and (args.language is None or args.language != "en")) else "transcribe"

    segments_iter, info = model.transcribe(
        str(in_path),
        task=task,
        language=args.language,   # None = auto-detect
        vad_filter=args.vad,
        beam_size=args.beam_size
    )

    segments = []
    for seg in segments_iter:
        segments.append({"start": seg.start, "end": seg.end, "text": seg.text})

    write_txt(txt_out, segments)
    write_srt(srt_out, segments)

    print(f"\nDetected language: {info.language} (prob={info.language_probability:.2f})")
    print(f"Saved transcript: {txt_out}")
    print(f"Saved subtitles:  {srt_out}")

if __name__ == "__main__":
    main()
