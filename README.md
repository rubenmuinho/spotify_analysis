# Spotify Analysis

Este proyecto permite analizar la actividad de un usuario en Spotify, incluyendo los artistas y canciones más escuchadas. Utiliza la API de Spotify a través de la biblioteca `spotipy`.

## Requisitos

Asegúrate de tener instalado Python 3.8 o superior. También necesitas instalar las dependencias listadas en `requirements.txt`.

```sh
pip install -r requirements.txt
```

## Uso

1. **Autenticación en Spotify:**
   - Al ejecutar el script `main_functions.py`, se solicitará autenticación en Spotify.
   - Se eliminará cualquier caché previa para permitir el inicio de sesión con una nueva cuenta.

2. **Análisis de Datos:**
   - El archivo `spotify_analysis.ipynb` contiene un análisis de los datos obtenidos de la API.
   - Puedes ejecutarlo en Jupyter Notebook para explorar la información.

## Archivos

- `main_functions.py`: Contiene funciones para autenticarse en Spotify y obtener los artistas y canciones más escuchadas.
- `spotify_analysis.ipynb`: Un notebook de Jupyter que analiza y visualiza los datos extraídos de Spotify.
- `requirements.txt`: Lista de dependencias necesarias para ejecutar el proyecto.

## Autenticación en Spotify

El script `main_functions.py` usa `SpotifyOAuth` para autenticar al usuario. Asegúrate de configurar correctamente las credenciales de la API de Spotify en el código.

## Contacto

Si tienes preguntas o sugerencias, abre un issue en el repositorio o contacta al autor.
