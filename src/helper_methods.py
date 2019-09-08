import spotipy
import spotipy.util as util


class SpotifyHelper:

    def __init__(self, username='qsnyvybl8iarj07dojit7xon1'):

        self.username = username
        self.scope = 'playlist-read-collaborative playlist-modify-private playlist-modify-public ' \
                     'playlist-read-private user-modify-playback-state user-read-currently-playing ' \
                     'user-read-playback-state user-read-private user-read-email user-library-modify ' \
                     'user-library-read user-follow-modify user-follow-read user-read-recently-played user-top-read ' \
                     'streaming app-remote-control'
        self.token = util.prompt_for_user_token(username, self.scope, client_id='b6227692e279468b8dc73975240df0b3',
                                                client_secret='459cb2f1c81146c0b6eaffbded50f2a2',
                                                redirect_uri='https://open.spotify.com/collection/playlists')
        self.sp = spotipy.Spotify(auth=self.token)

    def read_saved_tracks(self):
        results = self.sp.current_user_saved_tracks()
        for item in results['items']:
            track = item['track']
            print(track['name'] + ' - ' + track['artists'][0]['name'])
