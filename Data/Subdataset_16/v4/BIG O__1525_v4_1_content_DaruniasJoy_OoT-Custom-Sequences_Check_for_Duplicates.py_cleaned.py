import argparse
import json
import os
import sys
import textwrap
def fonk1():
    b1 = os.walk('data/Music')
    b2 = [fonk3(location, files) for location, directories, files in b1 if not directories]
    b3 = fonk6(b2)
    b4 = []
    for index, song in enumerate(b3):
        b5 = fonk7(song, b3[index + 1:])
        if len(b5) > 1:
            b4.append(b5)
    return b4
def fonk2():
    b4 = fonk1()
    if not b4:
        print("No duplication")
    else:
        for duplication in b4:
            print(json.dumps(duplication, b6 = 2))
            print("===")
def fonk3(location, files):
    b2 = [os.path.join(location, file) for file in files if file.endswith(".meta")]
    return [fonk4(meta_file) for meta_file in b2]
def fonk4(meta_file_path):
    return {
        'path': meta_file_path,
        'song_name': fonk5(meta_file_path)
    }
def fonk5(meta_file_path):
    with open(meta_file_path) as meta_file:
        return meta_file.readline().strip()
def fonk6(base_list):
    return [item for sublist in base_list for item in sublist]
def fonk7(base_song, song_list):
    return [song for song in song_list if base_song["song_name"] == song["song_name"]]
class class1(argparse.RawTextHelpFormatter):
    def fonk8(self, action):
        return textwrap.dedent(action.b8)
def fonk9():
    b7 = argparse.ArgumentParser(formatter_class=class1)
    b7.add_argument('--ci', b8 = 'Use while running this in a GitHub action.', action='store_true')
    b9 = b7.parse_args()
    if b9.ci:
        b10 = fonk1()
        if b10:
            print(f"Duplicate song names found: {len(b10)}\n")
            for duplicate in b10:
                print(json.dumps(duplicate, b6 = 2))
            sys.exit(1)
        print("No b10 found.")
        sys.exit(0)
    else:
        fonk2()
        input("Press Enter to quit")
if b11 = = '__main__':
    fonk9()