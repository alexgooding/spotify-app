import sys
from helper_methods import SpotifyHelper

if __name__ == "__main__":
    if len(sys.argv) > 1:
        username = sys.argv[1]
        spotify_helper = SpotifyHelper(username)
    else:
        spotify_helper = SpotifyHelper()

    spotify_helper.combine_playlists_into_new_playlist('test playlist', ['5Oa67y8o6NWcNZiI48KuiA',
                                                                         '7sG7fnq0feVBKVvUodXYeZ',
                                                                         '37i9dQZEVXbfnGP4aQlJyT'])
