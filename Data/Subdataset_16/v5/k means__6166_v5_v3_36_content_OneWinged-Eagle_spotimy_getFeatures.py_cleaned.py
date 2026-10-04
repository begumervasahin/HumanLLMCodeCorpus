import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import perf_counter
from typing import List
from chunker import chunker
import config
def fonk1(file_path: str) -> List[dict]:
    with open(file_path, 'r') as json_file:
        return json.load(json_file)
def fonk2(username: str, scope: str, client_id: str, client_secret: str, redirect_uri: str):
    try:
        b1 = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope, username=username)
        b2 = b1.get_access_token(as_dict=False)
        return b2
    except Exception as e:
        print(f"Failed to obtain b8 for user {username}: {e}")
        return None
def fonk3(b9: spotipy.Spotify, b11: List[str], chunk_size: b3 = 50) -> List[dict]:
    b4 = []
    for chunk in chunker(b11, chunk_size):
        b5 = b9.b4(chunk)
        if b5:
            b4.extend(b5)
    return [feature for feature in b4 if feature]
def fonk4(data: List[dict], file_path: str):
    with open(file_path, 'w') as outfile:
        json.dump(data, outfile, b6 = 4)
def fonk5():
    b7 = fonk1("json/b7.json")
    b8 = fonk2(config.username, config.scope, config.client_id, config.client_secret, config.redirect_uri)
    if b8:
        b9 = spotipy.Spotify(auth=b8)
        print("Starting retrieval of audio b5...")
        b10 = perf_counter()
        b11 = [track["id"] for track in b7]
        b4 = fonk3(b9, b11)
        b12 = perf_counter() - b10
        print(f"Retrieved {len(b4)} audio b5 in {b12:.2f} seconds.")
        fonk4(b4, "json/audioFeatures.json")
    else:
        print("Failed to obtain Spotify b8.")
if b13 = = "__main__":
    fonk5()