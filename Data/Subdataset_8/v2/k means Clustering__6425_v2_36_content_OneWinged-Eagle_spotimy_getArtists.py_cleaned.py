from json import dump
import spotipy
import spotipy.util as util
from time import perf_counter
from typing import Any, List
from sys import stderr
import config
try:
    token = util.prompt_for_user_token(config.username, config.scope,
                                       config.client_id, config.client_secret,
                                       config.redirect_uri)
    spotify_client = spotipy.Spotify(token)
except:
    print(f"Failed to obtain a token for user '{config.username}'", file=stderr)
    exit(1)
def retrieve_artists() -> List[Any]:
    artists = []
    last_artist_id = None
    while True:
        followed_artists = spotify_client.current_user_followed_artists(50, last_artist_id)
        artist_items = followed_artists["artists"]["items"]
        if len(artist_items) == 0:
            break
        last_artist_id = artist_items[-1]["id"]
        artists.extend(artist_items)
    return artists
def main():
    print("Starting to retrieve followed artists...")
    start_time = perf_counter()
    artists = retrieve_artists()
    elapsed_time = perf_counter() - start_time
    print(f"Retrieved {len(artists)} artists in {elapsed_time:.2f} seconds.")
    with open("json/artists.json", "w") as outfile:
        dump(artists, outfile, indent=4)
if __name__ == "__main__":
    main()
