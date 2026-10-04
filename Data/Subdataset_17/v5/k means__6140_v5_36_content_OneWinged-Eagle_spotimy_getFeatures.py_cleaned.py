import json
from time import perf_counter
from typing import List
from sys import stderr
import spotipy
import spotipy.util as util
from chunker import chunker
import config
def load_tracks_from_json(json_file_path: str) -> List[dict]:
    with open(json_file_path) as json_file:
        return json.load(json_file)
def retrieve_spotify_token(username: str, scope: str, client_id: str, client_secret: str, redirect_uri: str) -> str:
    try:
        return util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
    except:
        print(f"Token retrieval failed for {username}", file=stderr)
        return None
def retrieve_audio_features(sp: spotipy.Spotify, track_ids: List[str]) -> List[dict]:
    audio_features = []
    for chunk in chunker(track_ids, 50):
        audio_features.extend(sp.audio_features(chunk))
    return [af for af in audio_features if af]
def main():
    tracks = load_tracks_from_json("json/tracks.json")
    token = retrieve_spotify_token(config.username, config.scope, config.client_id, config.client_secret, config.redirect_uri)
    if not token:
        return
    sp = spotipy.Spotify(token)
    print("Start retrieving audio features...")
    start_time = perf_counter()
    audio_features = retrieve_audio_features(sp, [track["id"] for track in tracks])
    elapsed_time = perf_counter() - start_time
    print(f"Retrieved {len(audio_features)} audio features in {elapsed_time:.2f}s.")
    with open("json/audioFeatures.json", "w") as outfile:
        json.dump(audio_features, outfile)
if __name__ == "__main__":
    main()