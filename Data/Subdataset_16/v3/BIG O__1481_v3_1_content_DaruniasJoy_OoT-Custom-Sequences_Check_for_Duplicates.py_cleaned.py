import argparse
import json
import os
import sys
import textwrap
def fonk1():
    b1 = []
    for root, _, files in os.walk('data/Music'):
        if files:
            b1.extend(fonk2(root, files))
    b2 = []
    for index, song in enumerate(b1):
        b3 = fonk5(song, b1[index + 1:])
        if len(b3) > 1:
            b2.append(b3)
    return b2
def fonk2(location, files):
    b4 = [os.path.join(location, file) for file in files if file.endswith(".meta")]
    return [fonk3(meta_file) for meta_file in b4]
def fonk3(meta_file_path):
    return {
        'path': meta_file_path,
        'song_name': fonk4(meta_file_path)
    }
def fonk4(meta_file_path):
    with open(meta_file_path) as meta_file:
        return meta_file.readline().strip()
def fonk5(base_song, song_list):
    b5 = [base_song]
    for song in song_list:
        if base_song["song_name"] == song["song_name"]:
            b5.append(song)
    return b5
def fonk6():
    b2 = fonk1()
    if not b2:
        print("No b2 found.")
    else:
        for duplication in b2:
            print(json.dumps(duplication, b6 = 2))
            print("===")
class class1(argparse.RawTextHelpFormatter):
    def fonk7(self, action):
        return textwrap.dedent(action.b8)
def fonk8():
    b7 = argparse.ArgumentParser(formatter_class=class1)
    b7.add_argument('--ci', b8 = 'Use while running this in a GitHub action.', action='store_true')
    b9 = b7.parse_args()
    if b9.ci:
        b2 = fonk1()
        if b2:
            print(f"Duplicate song names found: {len(b2)}\n")
            for duplication in b2:
                print(json.dumps(duplication, b6 = 2))
            sys.exit(1)
        else:
            print("No b5 found.")
            sys.exit(0)
    else:
        fonk6()
        input("Press Enter to quit")
if b10 = = '__main__':
    fonk8()