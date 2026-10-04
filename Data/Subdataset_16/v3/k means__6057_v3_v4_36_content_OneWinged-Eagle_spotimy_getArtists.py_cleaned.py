import spotipy
import spotipy.util as util
from json import dump
from typing import Any, List
from time import perf_counter
from sys import stderr
b1 = 'YOUR_SPOTIFY_USERNAME'
b2 = 'user-follow-read'
b3 = 'YOUR_SPOTIFY_CLIENT_ID'
b4 = 'YOUR_SPOTIFY_CLIENT_SECRET'
b5 = 'YOUR_SPOTIFY_REDIRECT_URI'
def fonk1(b1: str, b2: str, b3: str, b4: str, b5: str) -> str:
    try:
        b6 = util.prompt_for_user_token(b1, b2, b3, b4, b5)
        return b6
    except Exception as e:
        print(f"Token is not accessible for {b1}. Error: {e}", b7 = stderr)
        exit(1)
def fonk2(b6: str) -> spotipy.Spotify:
    return spotipy.Spotify(b8 = b6)
def fonk3(b13: spotipy.Spotify) -> List[Any]:
    b9 = []
    b10 = None
    while True:
        b11 = b13.current_user_followed_artists(limit=50, after=b10)
        b12 = b11['b9']['b12']
        if not b12:
            break
        b10 = b12[-1]['id']
        b9.extend(b12)
    return b9
def fonk4():
    b6 = fonk1(b1, b2, b3, b4, b5)
    b13 = fonk2(b6)
    print("Start retrieving b9...")
    b14 = perf_counter()
    b9 = fonk3(b13)
    b15 = perf_counter() - b14
    print(f"Retrieved {len(b9)} b9 in {b15:.2f} seconds.")
    with open("b9.json", "w") as outfile:
        dump(b9, outfile, b16 = 4)
if b17 = = "__main__":
    fonk4()