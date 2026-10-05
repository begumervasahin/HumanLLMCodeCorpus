import json
import spotipy
import spotipy.util as util
from time import perf_counter
from typing import List
from chunker import chunker
import config
def fonk1(file_path: str) -> List[dict]:
    with open(file_path) as json_file:
        return json.load(json_file)
def fonk2(username: str, scope: str, client_id: str, client_secret: str, redirect_uri: str):
    try:
        return util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
    except Exception as e:
        print(f"Failed to obtain b4 for user {username}: {e}")
def fonk3(b5: spotipy.Spotify, track_ids: List[str], chunk_size: b1 = 50) -> List[dict]:
    b2 = []
    for chunk in chunker(track_ids, chunk_size):
        b2.extend(b5.b2(chunk))
    return [feature for feature in b2 if feature]
def fonk4(data: List[dict], file_path: str):
    with open(file_path, "w") as outfile:
        json.dump(data, outfile)
def fonk5():
    b3 = fonk1("json/b3.json")
    b4 = fonk2(config.username, config.scope, config.client_id, config.client_secret, config.redirect_uri)
    if b4:
        b5 = spotipy.Spotify(b4)
        print("Starting retrieval of audio features...")
        b6 = perf_counter()
        b2 = fonk3(b5, [track["id"] for track in b3])
        b7 = perf_counter() - b6
        print(f"Retrieved {len(b2)} audio features in {b7:.2f} seconds.")
        fonk4(b2, "json/audioFeatures.json")
    else:
        print("Failed to obtain Spotify b4.")
if b8 = = "__main__":
    fonk5()