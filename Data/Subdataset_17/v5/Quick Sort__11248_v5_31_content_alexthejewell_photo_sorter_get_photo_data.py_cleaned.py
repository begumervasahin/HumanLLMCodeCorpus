import hashlib
import os
from pathlib import Path
import time
import exifread
def get_date_taken(file_path):
    try:
        with open(file_path, 'rb') as file:
            tags = exifread.process_file(file, stop_tag="EXIF DateTimeOriginal")
            date_taken = tags.get("EXIF DateTimeOriginal")
            return date_taken
    except Exception as e:
        print(f"Error reading EXIF data from {file_path}: {e}")
        return None
def file_hash(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        buf = file.read()
        hasher.update(buf)
    return hasher.hexdigest()
def move_file(source, destination):
    if not destination.parent.exists():
        destination.parent.mkdir(parents=True)
    source.rename(destination)
    print(f"Moved file: From {source} To {destination}")
def delete_file(file_path):
    os.unlink(file_path)
    print(f"Deleted file: {file_path}")
def main():
    source = Path(r"E:\Jewell Family Media\Photos")
    destination = Path(r"E:\Jewell Family Media")
    duplicates_folder = Path(r"E:\photo_duplicates")
    start_time = time.time()
    moved_file_count = 0
    duplicate_count = 0
    total_files = 0
    deleted_count = 0
    unhandled_count = 0
    video_count = 0
    file_extensions = set()
    image_extensions = ['.bmp', '.png', '.jpg', '.jpeg', '.gif']
    video_extensions = ['.wmv', '.mov', '.avi', '.mp4']
    ignore_extensions = ['.idx2', '.psd']
    delete_extensions = ['.ini', '.ithmb', '.db']
    for root, dirs, files in os.walk(source, topdown=True):
        root_path = Path(root)
        for name in files:
            total_files += 1
            file_path = root_path / name
            file_suffix = file_path.suffix.lower()
            file_extensions.add(file_suffix)
            if file_suffix in delete_extensions:
                delete_file(file_path)
                deleted_count += 1
            elif file_suffix in video_extensions:
                print(f"Skipping video file: {file_path}")
                video_count += 1
            elif file_suffix in image_extensions:
                date_taken = get_date_taken(file_path)
                if date_taken:
                    date_parts = date_taken.values.split(':')
                    date_folder = f"{date_parts[0]}-{date_parts[1]}"
                    new_location = destination / date_folder / file_path.name
                    if new_location.exists():
                        if file_hash(file_path) == file_hash(new_location):
                            print(f"Ignoring duplicate: {file_path}")
                            duplicate_count += 1
                            new_location = duplicates_folder / f"{time.time()}_{name}"
                        else:
                            new_location = new_location.parent / f"{time.time()}_{name}"
                            print(f"Renaming duplicate: {file_path} to {new_location}")
                    move_file(file_path, new_location)
                    moved_file_count += 1
                else:
                    print(f"Cannot process file (no EXIF date): {file_path}")
                    unhandled_count += 1
            else:
                print(f"Unknown file type: {file_path}")
    print(f"Moved: {moved_file_count} files in {(time.time() - start_time) / 60:.2f} minutes")
    print(f"Duplicate files: {duplicate_count}")
    print(f"Deleted files: {deleted_count}")
    print(f"Unhandled files: {unhandled_count}")
    print(f"Video files: {video_count}")
    print(f"Total files processed: {total_files}")
    print(f"File extensions encountered: {file_extensions}")
if __name__ == "__main__":
    main()