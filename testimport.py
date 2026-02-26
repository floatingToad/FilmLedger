from db import get_connection
import os
import requests

# Load environment variables
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
if not TMDB_API_KEY:
    raise RuntimeError("TMDB_API_KEY missing") 

conn = get_connection()
cur = conn.cursor()

#get a popular movie
url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}"
response = requests.get(url)

if response.status_code != 200:
    print("TMDB API error:", response.text)
    exit(1)

data = response.json()
movie = data["results"][0] 

tmdb_id = movie["id"]
title = movie["title"]
release_date = movie.get("release_date")
description = movie.get("overview")

#insert into movies table, if id exist update the record
cur.execute("""
    INSERT INTO movies (tmdb_id, title, release_date, description)
    VALUES (%s, %s, %s, %s)
    ON CONFLICT (tmdb_id)            
    DO UPDATE SET     
        title = EXCLUDED.title,
        release_date = EXCLUDED.release_date,
        description = EXCLUDED.description;
""", (tmdb_id, title, release_date, description))

conn.commit()
print(f"Done!")

cur.close()
conn.close()
