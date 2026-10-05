import json
import spotipy
import spotipy.util as util
from time import perf_counter
from typing import List
from chunker import chunker
import config
with open("json/tracks.json") as json_file:
    tracks = json.load(json_file)
try:
    token = util.prompt_for_user_token(config.username, config.scope,
                                       config.client_id, config.client_secret,
                                       config.redirect_uri)
    sp = spotipy.Spotify(token)
except Exception as e:
    print(f"Failed to obtain token for user {config.username}: {e}")
print("Starting retrieval of audio features...")
start_time = perf_counter()
audio_features = []
for track_ids_chunk in chunker([track["id"] for track in tracks], 50):
    audio_features.extend(sp.audio_features(track_ids_chunk))
audio_features = [feature for feature in audio_features if feature]
elapsed_time = perf_counter() - start_time
print(f"Retrieved {len(audio_features)} audio features in {elapsed_time:.2f} seconds.")
with open("json/audioFeatures.json", "w") as outfile:
    json.dump(audio_features, outfile)