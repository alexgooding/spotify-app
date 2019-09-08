import spotipy
import spotipy.util as util


class SpotifyHelper:

    def __init__(self, username='qsnyvybl8iarj07dojit7xon1'):

        self.username = username

        self.scope = 'user-library-read'

        self.token = util.prompt_for_user_token(username, self.scope, client_id='b6227692e279468b8dc73975240df0b3',
                                                client_secret='459cb2f1c81146c0b6eaffbded50f2a2',
                                                redirect_uri='https://open.spotify.com/collection/playlists')

    def read_saved_tracks(self):
        if self.token:
            sp = spotipy.Spotify(auth=self.token)
            results = sp.current_user_saved_tracks()
            for item in results['items']:
                track = item['track']
                print(track['name'] + ' - ' + track['artists'][0]['name'])
        else:
            print("Can't get token for", self.username)
