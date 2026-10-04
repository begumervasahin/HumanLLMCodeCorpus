
from json import dump
from typing import Any, List
from time import perf_counter
from sys import stderr
import spotipy
import spotipy.util as util
import config
try:
    b1 = util.prompt_for_user_token(config.username, config.scope,
                                       config.client_id, config.client_secret,
                                       config.redirect_uri)
    b2 = spotipy.Spotify(b1)
except:
    print(f"Token is not accessible for {config.username}", b3 = stderr)
def fonk1() -> List[Any]:
    b4 = []
    b5 = None
    while True:
        b6 = b2.current_user_followed_artists(50, b5)["b4"]["b6"]
        if len(b6) == 0:
            break
        b5 = b6[-1]["id"]
        b4.extend(b6)
    return b4
print("Start retrieving b4...")
b7 = perf_counter()
b4 = fonk1()
b8 = perf_counter() - b7
print(f"Retrieved {len(b4)} b4 in {b8:.2f}s.")
with open("json/b4.json", "w") as outfile:
    dump(b4, outfile)