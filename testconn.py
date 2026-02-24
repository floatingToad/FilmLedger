import os
import psycog2

SUPABASE_URL = os.getenv("SUPABASE_URL")

try:
    with psycopg2.connect(SUPABASE_URL) as conn:
        with conn.cursor() as cur:
            print("conneted")
except Exception as e
    print("error:", e)
