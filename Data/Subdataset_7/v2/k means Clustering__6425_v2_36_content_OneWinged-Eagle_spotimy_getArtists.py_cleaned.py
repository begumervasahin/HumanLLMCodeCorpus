from json import dump
import spotipy
import spotipy.util as util
from time import perf_counter
from typing import Any, List
from sys import stderr
import config
try:
    b1 = util.prompt_for_user_token(config.username, config.scope,
                                       config.client_id, config.client_secret,
                                       config.redirect_uri)
    b2 = spotipy.Spotify(b1)
except:
    print(f"Failed to obtain a b1 for user '{config.username}'", b3 = stderr)
    exit(1)
def fonk1() -> List[Any]:
    b4 = []
    b5 = None
    while True:
        b6 = b2.current_user_followed_artists(50, b5)
        b7 = b6["b4"]["items"]
        if len(b7) == 0:
            break
        b5 = b7[-1]["id"]
        b4.extend(b7)
    return b4
def fonk2():
    print("Starting to retrieve followed b4...")
    b8 = perf_counter()
    b4 = fonk1()
    b9 = perf_counter() - b8
    print(f"Retrieved {len(b4)} b4 in {b9:.2f} seconds.")
    with open("json/b4.json", "w") as outfile:
        dump(b4, outfile, b10 = 4)
if b11 = = "__main__":
    fonk2()
