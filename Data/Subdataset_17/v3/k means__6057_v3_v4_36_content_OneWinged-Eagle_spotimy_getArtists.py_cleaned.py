import spotipy
import spotipy.util as util
from json import dump
from typing import Any, List
from time import perf_counter
from sys import stderr
username = 'YOUR_SPOTIFY_USERNAME'
scope = 'user-follow-read'
client_id = 'YOUR_SPOTIFY_CLIENT_ID'
client_secret = 'YOUR_SPOTIFY_CLIENT_SECRET'
redirect_uri = 'YOUR_SPOTIFY_REDIRECT_URI'
def get_spotify_token(username: str, scope: str, client_id: str, client_secret: str, redirect_uri: str) -> str:
    try:
        token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
        return token
    except Exception as e:
        print(f"Token is not accessible for {username}. Error: {e}", file=stderr)
        exit(1)
def create_spotify_object(token: str) -> spotipy.Spotify:
    return spotipy.Spotify(auth=token)
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
    token = get_spotify_token(username, scope, client_id, client_secret, redirect_uri)
    sp = create_spotify_object(token)
    print("Start retrieving artists...")
    start_time = perf_counter()
    artists = retrieve_artists(sp)
    elapsed_time = perf_counter() - start_time
    print(f"Retrieved {len(artists)} artists in {elapsed_time:.2f} seconds.")
    with open("artists.json", "w") as outfile:
        dump(artists, outfile, indent=4)
if __name__ == "__main__":
    main()