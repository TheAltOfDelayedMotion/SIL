import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from ytmusicapi import ytmusic as ytm
import songfinder

cid = '05a8b389bcbb4ec486a4f07ca33959ac'
secret = '5a9c34a5881e45e99e0248458d4d0f01'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

song = songfinder.call_playlist("spotify","6HNtu1w10bhmGhbnN4jwSR")








