import argparse
import json
import os
import sys
import textwrap
def get_duplicate_songs():
    song_details = []
    for root, _, files in os.walk('data/Music'):
        if files:
            song_details.extend(build_meta_file_list(root, files))
    duplications = []
    for index, song in enumerate(song_details):
        song_duplicates = find_duplicates(song, song_details[index + 1:])
        if len(song_duplicates) > 1:
            duplications.append(song_duplicates)
    return duplications
def build_meta_file_list(location, files):
    meta_files = [os.path.join(location, file) for file in files if file.endswith(".meta")]
    return [extract_song_info(meta_file) for meta_file in meta_files]
def extract_song_info(meta_file_path):
    return {
        'path': meta_file_path,
        'song_name': get_registered_song_name(meta_file_path)
    }
def get_registered_song_name(meta_file_path):
    with open(meta_file_path) as meta_file:
        return meta_file.readline().strip()
def find_duplicates(base_song, song_list):
    duplicates = [base_song]
    for song in song_list:
        if base_song["song_name"] == song["song_name"]:
            duplicates.append(song)
    return duplicates
def validate_song_name_unicity():
    duplications = get_duplicate_songs()
    if not duplications:
        print("No duplications found.")
    else:
        for duplication in duplications:
            print(json.dumps(duplication, indent=2))
            print("===")
class ArgumentDefaultsHelpFormatter(argparse.RawTextHelpFormatter):
    def _get_help_string(self, action):
        return textwrap.dedent(action.help)
def main():
    parser = argparse.ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('--ci', help='Use while running this in a GitHub action.', action='store_true')
    args = parser.parse_args()
    if args.ci:
        duplications = get_duplicate_songs()
        if duplications:
            print(f"Duplicate song names found: {len(duplications)}\n")
            for duplication in duplications:
                print(json.dumps(duplication, indent=2))
            sys.exit(1)
        else:
            print("No duplicates found.")
            sys.exit(0)
    else:
        validate_song_name_unicity()
        input("Press Enter to quit")
if __name__ == '__main__':
    main()