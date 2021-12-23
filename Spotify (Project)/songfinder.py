import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = '05a8b389bcbb4ec486a4f07ca33959ac'
secret = '5a9c34a5881e45e99e0248458d4d0f01'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


def call_playlist(creator, playlist_id):
    playlist = sp.user_playlist_tracks(creator, playlist_id)["items"]
    for track in playlist:
        # Create empty dict
        playlist_features = {}

        playlist_features["Track Name"] = track["track"]["name"]
        print(playlist_features["Track Name"])


    return(playlist_features)
