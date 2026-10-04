import argparse
import json
import os
import sys
import textwrap
def fonk1():
    b1 = os.walk('data/Music')
    b2 = [fonk3(location, files) for location, directories, files in b1 if len(directories) == 0]
    b3 = fonk6(b2)
    b4 = []
    for index, song in enumerate(b3):
        b5 = fonk7(song, b3[index+1:])
        if len(b5) > 1:
            b4.append(b5)
    return b4
def fonk2():
    b4 = fonk1()
    if len(b4) == 0:
        print("No duplication")
    for duplication in b4:
        print(json.dumps(duplication, b6 = 2))
        print("===")
def fonk3(location, files):
    b7 = [os.path.join(location, file) for file in files if file.endswith(".meta")]
    return [fonk4(meta_file_path) for meta_file_path in b7]
def fonk4(meta_file_path):
    return {
        'path': meta_file_path,
        'song_name': fonk5(meta_file_path)
    }
def fonk5(meta_file_path):
    with open(meta_file_path) as meta_file:
        return meta_file.readline().rstrip()
def fonk6(base_list):
    return [item for sublist in base_list for item in sublist]
def fonk7(base_song, song_list):
    b8 = [base_song]
    for song in song_list:
        if base_song["song_name"] == song["song_name"]:
            b8.append(song)
    return b8
class class1(argparse.RawTextHelpFormatter):
    def fonk8(self, action):
        return textwrap.dedent(action.b10)
def fonk9():
    b9 = argparse.ArgumentParser(formatter_class=class1)
    b9.add_argument('--ci', b10 = 'Use while running this in a GitHub action.', action='store_true')
    b11 = b9.parse_args()
    if b11.ci:
        b12 = fonk1()
        if b12:
            print(f"Duplicate song names found: {len(b12)}\n")
            for b8 in b12:
                print(json.dumps(b8, b6 = 2))
            sys.exit(1)
        print("No b12 found.")
        sys.exit(0)
    fonk2()
    input("Press Enter to quit")
if b13 = = '__main__':
    fonk9()