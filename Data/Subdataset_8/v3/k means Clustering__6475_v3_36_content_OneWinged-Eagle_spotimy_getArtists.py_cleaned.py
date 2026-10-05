from json import dump
import spotipy
import spotipy.util as util
from time import perf_counter
from typing import Any, List
from sys import stderr
import config
def get_spotify_client():
    try:
        token = util.prompt_for_user_token(config.username, config.scope,
                                           config.client_id, config.client_secret,
                                           config.redirect_uri)
        return spotipy.Spotify(token)
    except Exception as e:
        print(f"Failed to obtain a Spotify token for user '{config.username}': {e}", file=stderr)
        return None
def retrieve_followed_artists(spotify_client: spotipy.Spotify, batch_size: int = 50) -> List[Any]:
    artists = []
    last_artist_id = None
    while True:
        followed_artists = spotify_client.current_user_followed_artists(batch_size, last_artist_id)
        artist_items = followed_artists["artists"]["items"]
        if not artist_items:
            break
        last_artist_id = artist_items[-1]["id"]
        artists.extend(artist_items)
    return artists
def main():
    print("Starting to retrieve followed artists...")
    start_time = perf_counter()
    spotify_client = get_spotify_client()
    if not spotify_client:
        return
    artists = retrieve_followed_artists(spotify_client)
    elapsed_time = perf_counter() - start_time
    print(f"Retrieved {len(artists)} artists in {elapsed_time:.2f} seconds.")
    with open("json/artists.json", "w") as outfile:
        dump(artists, outfile, indent=4)
if __name__ == "__main__":
    main()