import json
import spotipy
import spotipy.util as util
from time import perf_counter
from typing import List
from chunker import chunker
import config
with open("json/b1.json") as json_file:
    b1 = json.load(json_file)
try:
    b2 = util.prompt_for_user_token(config.username, config.scope,
                                       config.client_id, config.client_secret,
                                       config.redirect_uri)
    b3 = spotipy.Spotify(b2)
except Exception as e:
    print(f"Failed to obtain b2 for user {config.username}: {e}")
print("Starting retrieval of audio features...")
b4 = perf_counter()
b5 = []
for track_ids_chunk in chunker([track["id"] for track in b1], 50):
    b5.extend(b3.b5(track_ids_chunk))
b5 = [feature for feature in b5 if feature]
b6 = perf_counter() - b4
print(f"Retrieved {len(b5)} audio features in {b6:.2f} seconds.")
with open("json/audioFeatures.json", "w") as outfile:
    json.dump(b5, outfile)