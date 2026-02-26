import requests
from config import get_env

BASE_URL = "https://api.themoviedb.org/3"
def get_genres():
    api_key = get_env("TMDB_API_KEY")
    
    response = requests.get(
        f"{BASE_URL}/genre/movie/list",
        params={"api_key": api_key}
    )
    response.raise_for_status()

    return response.json()["genres"]


if __name__ == "__main__":
    genres = get_genres()
    print("Genres:", genres)

