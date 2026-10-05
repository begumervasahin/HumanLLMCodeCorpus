
import spotipy
import spotipy.util as util
import config
import json
from time import perf_counter
from sys import stderr
try:
    token = util.prompt_for_user_token(config.username, config.scope,
                                       config.client_id, config.client_secret,
                                       config.redirect_uri)
    sp = spotipy.Spotify(token)
except:
    print(f"Token is not accessible for {config.username}", file=stderr)
def retrieve_artists() -> list:
    artists = []
    last_artist_id = None
    while True:
        items = sp.current_user_followed_artists(50, last_artist_id)["artists"]["items"]
        if not items:
            break
        last_artist_id = items[-1]["id"]
        artists.extend(items)
    return artists
def main():
    print("Start retrieving artists...")
    start_time = perf_counter()
    artists = retrieve_artists()
    elapsed_time = perf_counter() - start_time
    print(f"Retrieved {len(artists)} artists in {elapsed_time:.2f}s.")
    with open("json/artists.json", "w") as outfile:
        json.dump(artists, outfile)
if __name__ == "__main__":
    main()