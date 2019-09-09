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

    def get_playlist_track_ids(self, playlist_id):

        results = self.sp.user_playlist_tracks(self.username, playlist_id)
        tracks = results['items']

        # Loops to ensure I get every track of the playlist
        while results['next']:
            results = self.sp.next(results)
            tracks.extend(results['items'])

        track_ids = []
        for track in tracks:
            track_ids.append(track.get('track').get('id'))

        return track_ids

    def create_playlist_with_track_ids(self, playlist_name, track_ids, public=False):
        playlist_id = self.sp.user_playlist_create(self.username, playlist_name, public).get('id')
        self.sp.user_playlist_add_tracks(self.username, playlist_id, track_ids)

    def combine_playlists_into_new_playlist(self, new_playlist_name, old_playlist_ids):
        track_ids = []
        for id in old_playlist_ids:
            track_ids.extend(self.get_playlist_track_ids(id))

        # Genre filtering if wanted
        if is_genre_filtering:
            track_ids = self.filter_tracks(track_ids, genre_list, is_exact_match, filter_untagged_artists)

        self.create_playlist_with_track_ids(new_playlist_name, track_ids)

    def filter_tracks(self, track_ids, genre_list, is_exact_match=True, filter_untagged_artists=False):
        ids_to_remove = []
        for track_id in track_ids:
            for genre in genre_list:
                if self.is_track_genre(track_id, genre, is_exact_match, filter_untagged_artists):
                    ids_to_remove.append(track_id)

        track_ids = [i for i in track_ids if i not in ids_to_remove]
        return track_ids

    def is_track_genre(self, track_id, genre, is_exact_match=True, filter_untagged_artists=False):
        track_artists = self.sp.track(track_id).get('artists')
        track_genres = []
        for artist in track_artists:
            track_genres.extend(self.sp.artist(artist.get('id')).get('genres'))
        if filter_untagged_artists:
            if not track_genres:
                return True
        if is_exact_match:
            if genre in track_genres:
                return True
        else:
            for track_genre in track_genres:
                if genre in track_genre:
                    return True
        return False
