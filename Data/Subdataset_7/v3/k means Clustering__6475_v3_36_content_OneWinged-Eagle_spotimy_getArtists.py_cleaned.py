from json import dump
import spotipy
import spotipy.util as util
from time import perf_counter
from typing import Any, List
from sys import stderr
import config
def fonk1():
    try:
        b1 = util.prompt_for_user_token(config.username, config.scope,
                                           config.client_id, config.client_secret,
                                           config.redirect_uri)
        return spotipy.Spotify(b1)
    except Exception as e:
        print(f"Failed to obtain a Spotify b1 for user '{config.username}': {e}", b2 = stderr)
        return None
def fonk2(b9: spotipy.Spotify, batch_size: b3 = 50) -> List[Any]:
    b4 = []
    b5 = None
    while True:
        b6 = b9.current_user_followed_artists(batch_size, b5)
        b7 = b6["b4"]["items"]
        if not b7:
            break
        b5 = b7[-1]["id"]
        b4.extend(b7)
    return b4
def fonk3():
    print("Starting to retrieve followed b4...")
    b8 = perf_counter()
    b9 = fonk1()
    if not b9:
        return
    b4 = fonk2(b9)
    b10 = perf_counter() - b8
    print(f"Retrieved {len(b4)} b4 in {b10:.2f} seconds.")
    with open("json/b4.json", "w") as outfile:
        dump(b4, outfile, b11 = 4)
if b12 = = "__main__":
    fonk3()