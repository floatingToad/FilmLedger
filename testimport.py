from dotenv import load_dotenv
from pathlib import Path
import os
import psycopg2
import requests

load_dotenv(dotenv_path=Path(__file__).parent / ".env")

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
TMDB_API_KEY = os.getenv("TMBD_API_KEY")

try:
    # Connect to Supabase
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        sslmode="require"
    )
    cur = conn.cursor()
except Exception as e:
    print(f"Database connection failed: {e}")


#get a popular movie
url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}"
response = requests.get(url)

print("Status code:", response.status_code)

data = response.json()

print("Keys:", data.keys())
print("First movie:", data["results"][0])          
