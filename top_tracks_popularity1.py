import matplotlib.pyplot as plt
import seaborn as sns
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Autenticación con Spotify API (asegúrate de tener tus credenciales)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="TU_CLIENT_ID",
                                               client_secret="TU_CLIENT_SECRET",
                                               redirect_uri="TU_REDIRECT_URI",
                                               scope=["user-top-read"]))

def mostrar_top_20_tracks():
    # Obtener las 50 canciones más escuchadas
    top_tracks = sp.current_user_top_tracks(limit=50, time_range='medium_term')

    # Mostrar el top 20 de canciones
    print("Top 20 Canciones Más Escuchadas:")
    for idx, track in enumerate(top_tracks['items'][:20]):
        print(f"{idx + 1}. {track['name']} - Popularidad: {track['popularity']}")

    # Solicitar que el usuario ingrese el número de la canción que desea saber más
    selected_index = int(input("\nElige el número de la canción para ver su popularidad: ")) - 1
    selected_track = top_tracks['items'][selected_index]

    # Mostrar la popularidad de la canción seleccionada
    print(f"\nLa popularidad de '{selected_track['name']}' es: {selected_track['popularity']}")

    # Visualizar la distribución de la popularidad y marcar la canción seleccionada
    track_popularity = [track['popularity'] for track in top_tracks['items']]

    # Crear el gráfico
    plt.figure(figsize=(10, 5))
    sns.histplot(track_popularity, bins=10, color='purple')

    # Marcar la popularidad de la canción seleccionada en el gráfico
    plt.axvline(x=selected_track['popularity'], color='red', linestyle='--', label=f"{selected_track['name']} ({selected_track['popularity']})")

    # Configuración del gráfico
    plt.title('🎵 Distribución de la Popularidad de tus Canciones Más Escuchadas')
    plt.xlabel('Popularidad (0-100)')
    plt.ylabel('Frecuencia')
    plt.legend()

    # Mostrar el gráfico
    plt.show()

if __name__ == "__main__":
    mostrar_top_20_tracks()
