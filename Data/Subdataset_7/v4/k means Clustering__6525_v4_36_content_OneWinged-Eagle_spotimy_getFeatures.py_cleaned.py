import json
import spotipy
import spotipy.util as util
from time import perf_counter
from typing import Any, List
from sys import stderr
from chunker import chunker
import config
with open("json/b1.json") as json_file:
    b1 = json.load(json_file)
try:
    b2 = util.prompt_for_user_token(config.username, config.scope,
                                       config.client_id, config.client_secret,
                                       config.redirect_uri)
    b3 = spotipy.Spotify(b2)
except:
    print(f"Token is not accessible for {config.username}", b4 = stderr)
print("Start retrieving audio features...")
b5 = perf_counter()
b6 = []
for tracksIds in chunker([track["id"] for track in b1], 50):
    b6.extend(b3.audio_features(tracksIds))
b6 = [audioFeature for audioFeature in b6 if audioFeature]
b7 = perf_counter() - b5
print(f"Retrieved {len(b6)} audio features in {b7:.2f}s.")
with open("json/b6.json", "w") as outfile:
    json.dump(b6, outfile)