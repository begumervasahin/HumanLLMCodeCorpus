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
    print(f"Token is not accessible for {config.username}: {e}")
print("Start retrieving audio features...")
b4 = perf_counter()
b5 = []
for tracksIds in chunker([track["id"] for track in b1], 50):
    b5.extend(b3.audio_features(tracksIds))
b5 = [audioFeature for audioFeature in b5 if audioFeature]
b6 = perf_counter() - b4
print(f"Retrieved {len(b5)} audio features in {b6:.2f}s.")
with open("json/b5.json", "w") as outfile:
    json.dump(b5, outfile)