import sys
from helper_methods import SpotifyHelper

if __name__ == "__main__":
    if len(sys.argv) > 1:
        username = sys.argv[1]
        spotify_helper = SpotifyHelper(username)
    else:
        spotify_helper = SpotifyHelper()

    spotify_helper.read_saved_tracks()
