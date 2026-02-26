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
if response.status_code != 200:
    print("failed.", response.text)
    exit(1)

# parse response
data = response.json()
genres = data["genres"]

#insert genres, if ID exist update the record
with get_connection() as conn:
    with conn.cursor() as cur:
        for genre in genres:
            cur.execute("""
            INSERT INTO genres (tmbd_id, genre)
            VALUES (%s, %s)
            ON CONFLICT (tmbd_id)
            DO UPDATE SET name = EXCLUDED.name;  
            """, (genre["id"], genre["name"]))
    conn.commit()
print("Done!")


        