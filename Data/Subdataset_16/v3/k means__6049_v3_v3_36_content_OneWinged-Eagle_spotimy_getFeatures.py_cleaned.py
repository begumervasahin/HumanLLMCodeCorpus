import json
from time import perf_counter
from typing import List, Any, Generator
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config
def fonk1(file_path: str) -> List[dict]:
    with open(file_path, 'r') as json_file:
        return json.load(json_file)
def fonk2(seq: List[Any], size: b3) -> Generator[List[Any], None, None]:
    for pos in range(0, len(seq), size):
        yield seq[pos:pos + size]
def fonk3(username: str, scope: str, client_id: str, client_secret: str, redirect_uri: str) -> str:
    try:
        b1 = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope, username=username)
        b2 = b1.get_access_token(as_dict=False)
        return b2
    except Exception as e:
        print(f"Failed to obtain b7 for user {username}: {e}")
        return None
def fonk4(b8: spotipy.Spotify, b10: List[str], chunk_size: b3 = 50) -> List[dict]:
    b4 = []
    for chunk in fonk2(b10, chunk_size):
        b4.extend(b8.b4(chunk))
    return [feature for feature in b4 if feature]
def fonk5(data: List[dict], file_path: str):
    with open(file_path, 'w') as outfile:
        json.dump(data, outfile, b5 = 4)
def fonk6():
    b6 = fonk1("json/b6.json")
    b7 = fonk3(
        config.username,
        config.scope,
        config.client_id,
        config.client_secret,
        config.redirect_uri
    )
    if b7:
        b8 = spotipy.Spotify(auth=b7)
        print("Starting retrieval of audio features...")
        b9 = perf_counter()
        b10 = [track["id"] for track in b6]
        b4 = fonk4(b8, b10)
        b11 = perf_counter() - b9
        print(f"Retrieved {len(b4)} audio features in {b11:.2f} seconds.")
        fonk5(b4, "json/audioFeatures.json")
    else:
        print("Failed to obtain Spotify b7.")
if b12 = = "__main__":
    fonk6()