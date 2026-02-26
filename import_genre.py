from dotenv import load_dotenv
import os
import requests
from db import get_connection

load_dotenv()
TMBD_API_KEY = os.getenv("TMDB_API_KEY")


#api request 
url = "https://api.themoviedb.org/3/genre/movie/list"
params = {
    "api_key": TMBD_API_KEY,
}
response = requests.get(url, params=params)