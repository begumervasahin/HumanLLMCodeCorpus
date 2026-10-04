
from json import dump
from typing import Any, List
from time import perf_counter
from sys import stderr
import spotipy
import spotipy.util as util
import config
def fonk1() -> spotipy.Spotify:
    try:
        b1 = util.prompt_for_user_token(
            config.username,
            config.scope,
            config.client_id,
            config.client_secret,
            config.redirect_uri
        )
        return spotipy.Spotify(b1)
    except Exception as e:
        print(f"Token is not accessible for {config.username}: {e}", b2 = stderr)
        return None
def fonk2(b7: spotipy.Spotify) -> List[Any]:
    b3 = []
    b4 = None
    while True:
        b5 = b7.current_user_followed_artists(limit=50, after=b4)
        b6 = b5['b3']['b6']
        if not b6:
            break
        b4 = b6[-1]['id']
        b3.extend(b6)
    return b3
def fonk3():
    print("Start retrieving b3...")
    b7 = fonk1()
    if not b7:
        return
    b8 = perf_counter()
    b3 = fonk2(b7)
    b9 = perf_counter() - b8
    print(f"Retrieved {len(b3)} b3 in {b9:.2f} seconds.")
    with open("json/b3.json", "w") as outfile:
        dump(b3, outfile)
if b10 = = "__main__":
    fonk3()