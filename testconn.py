from dotenv import load_dotenv
from db import get_connection
import os
import psycopg2

load_dotenv()

conn = get_connection()
cur = conn.cursor()

try:
    cur.execute("SELECT 1")
    print("Database connection successful.")
except Exception as e:
    print(f"Database connection failed: {e}")

