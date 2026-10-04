
from json import dump
from typing import Any, List
from time import perf_counter
from sys import stderr
import spotipy
import spotipy.util as util
import config
def get_spotify_client() -> spotipy.Spotify:
    try:
        token = util.prompt_for_user_token(
            config.username,
            config.scope,
            config.client_id,
            config.client_secret,
            config.redirect_uri
        )
        return spotipy.Spotify(token)
    except Exception as e:
        print(f"Token is not accessible for {config.username}: {e}", file=stderr)
        return None
def retrieve_artists(sp: spotipy.Spotify) -> List[Any]:
    artists = []
    last_artist_id = None
    while True:
        response = sp.current_user_followed_artists(limit=50, after=last_artist_id)
        items = response['artists']['items']
        if not items:
            break
        last_artist_id = items[-1]['id']
        artists.extend(items)
    return artists
def main():
    print("Start retrieving artists...")
    sp = get_spotify_client()
    if not sp:
        return
    start_time = perf_counter()
    artists = retrieve_artists(sp)
    elapsed_time = perf_counter() - start_time
    print(f"Retrieved {len(artists)} artists in {elapsed_time:.2f} seconds.")
    with open("json/artists.json", "w") as outfile:
        dump(artists, outfile)
if __name__ == "__main__":
    main()