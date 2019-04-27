import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time

code= "BQDaDCMhbXFvjQdBJ57BVt3ksMcyTZJ2OI9wsNId3zyI8kfNAcV5Ciw_b2XXD2wMNAMTSJTcCDvid-4kJZPekBA3mDIfJG_IYHPclteV94_pfr05ag_BY3TfEsVb0U1SARqSNehluPJh9NY"

sp = spotipy.client.Spotify(auth= code, requests_session=True, client_credentials_manager=None, proxies=None, requests_timeout=None)

albums = [
"6oxVabMIqCMJRYN1GqR3Vf",
"0Zd10MKN5j9KwUST0TdBBB",
"23Y5wdyP5byMFktZf8AcWU",
"5O7PYNgE3VLWrvB80fIaDZ",
"2UJwKSBUz6rtW4QLK74kQu",
"4X6b6POxbjX9inC7TWQd54",
"35S1JCj5paIfElT2GODl6x"
]

dataset = {}

for album in albums:
    dataset[album] = {}
    track_results = sp.album_tracks(album, limit=50, offset=0)
    tracks_s = track_results['items']
    print("album")
    time.sleep(0.1)



    for track in tracks_s:
        audioResults = sp.audio_features(tracks=[track['id']])
        dataset[album][track['name']] = {}
        dataset[album][track['name']]['name'] = track['name']
        print(track['name'])
        time.sleep(0.1)

        for t in audioResults:
            for i in t.keys():
                dataset[album][track['name']][i] = t[i]
                print("yes audio")
    time.sleep(0.3)
