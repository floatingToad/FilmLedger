from db import get_connection
from pathlib import Path
import os
import requests
import db

# Load environment variables
TMDB_API_KEY = os.getenv("TMBD_API_KEY")
if not TMDB_API_KEY:
    raise RuntimeError("TMBD_API_KEY missing")

#api request 
url = "https://api.themoviedb.org/3/genre/movie/list"
params = {
    "api_key": TMDB_API_KEY,
}
response = requests.get(url, params=params)
if response.status_code != 200:
    print("failed.", response.text)
    exit(1)

# parse response
data = response.json()
genres = data["genres"]

#insert genres, if ID exist update the record
with db.get_connection() as conn:
    with conn.cursor() as cur:
        for genre in genres:
            cur.execute("""
            INSERT INTO genres (tmbd_id, name)
            VALUES (%s, %s)
            ON CONFLICT (tmbd_id)
            DO UPDATE SET name = EXCLUDED.name;  
            """, (genre["id"], genre["name"]))
    conn.commit()
print("Done!")


        