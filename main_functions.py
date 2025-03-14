import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def authenticate_spotify():
    # Eliminar el caché si existe
    if os.path.exists('.cache'):
        os.remove('.cache')
        print("✅ Caché eliminada. Inicia sesión con una nueva cuenta.")

    CLIENT_ID = '831c19eb66b34d0a8810422ad1585a93'
    CLIENT_SECRET = 'bbbf5e44f1aa48cf894049e0fce4ae69'
    REDIRECT_URI = 'http://127.0.0.1:8888/callback'

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="user-top-read"
    ))

    user = sp.current_user()
    print(f"¡Autenticado como: {user['display_name']}!")
    return sp

def get_top_artists(sp, limit, time_range='medium_term'):
    # Obtener los artistas más escuchados
    return sp.current_user_top_artists(limit=limit, time_range=time_range)

def get_top_tracks(sp, limit, time_range='medium_term'):
    # Obtener las canciones más escuchadas
    return sp.current_user_top_tracks(limit=limit, time_range=time_range)

def display_top_artists(top_artists, display_limit):
    # Mostrar los primeros X artistas
    for idx, artist in enumerate(top_artists['items'][:display_limit]):
        print(f"{idx + 1}. {artist['name']} - Género: {', '.join(artist['genres'])}")

def display_top_tracks(top_tracks, display_limit):
    # Mostrar las primeras X canciones
    for idx, track in enumerate(top_tracks['items'][:display_limit]):
        print(f"{idx + 1}. {track['name']} - Artista: {track['artists'][0]['name']}")
