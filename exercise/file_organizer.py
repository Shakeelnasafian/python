import os
import shutil
from pathlib import Path
import logging
import time

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def organize_downloads():
    # Use the specific Downloads folder path provided by the user
    downloads_folder = r"C:\Users\ShakeelAhmad\OneDrive - AGH Directory\Downloads"
    
    # Verify the path exists
    if not os.path.exists(downloads_folder):
        print(f"Error: The directory '{downloads_folder}' does not exist.")
        return
    
    logging.info(f"Starting organization of: {downloads_folder}")
    
    # Define file categories and their extensions
    categories = {
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".tiff", ".webp"],
        "PDFs": [".pdf"],
        "Documents": [".doc", ".docx", ".txt", ".rtf", ".odt", ".pages"],
        "Spreadsheets": [".xls", ".xlsx", ".csv", ".ods", ".numbers"],
        "Presentations": [".ppt", ".pptx", ".key", ".odp"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv", ".webm"],
        "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
        "Executables": [".exe", ".msi", ".app", ".bat", ".sh"],
        "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".php", ".go", ".rb"],
    }
    
    try:
        # Get all files in the downloads folder
        files = [f for f in os.listdir(downloads_folder) if os.path.isfile(os.path.join(downloads_folder, f))]
        
        # Count of files moved
        moved_count = 0
        
        # Process each file
        for file in files:
            # Get the full path and extension
            file_path = os.path.join(downloads_folder, file)
            file_ext = os.path.splitext(file)[1].lower()
            
            # Find the category for this file
            target_category = "Others"  # Default category
            
            for category, extensions in categories.items():
                if file_ext in extensions:
                    target_category = category
                    break
                    
            # Create target directory if it doesn't exist
            target_dir = os.path.join(downloads_folder, target_category)
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
                logging.info(f"Created directory: {target_dir}")
            
            # Move the file
            target_path = os.path.join(target_dir, file)
            
            # Handle file name conflicts
            if os.path.exists(target_path):
                # Add timestamp to make filename unique
                base_name, extension = os.path.splitext(file)
                new_name = f"{base_name}_{int(time.time())}{extension}"
                target_path = os.path.join(target_dir, new_name)
            
            try:
                shutil.move(file_path, target_path)
                logging.info(f"Moved: {file} -> {target_category}")
                moved_count += 1
            except Exception as e:
                logging.error(f"Error moving {file}: {e}")
        
        logging.info(f"Organization complete! Moved {moved_count} of {len(files)} files.")
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    
if __name__ == "__main__":
    organize_downloads()
    print("\nDownloads folder has been organized!")
    input("Press Enter to exit...")