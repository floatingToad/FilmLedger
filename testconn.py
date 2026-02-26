from db import get_connection
import os

conn = get_connection()
cur = conn.cursor()

try:
    cur.execute("SELECT 1")
    print("Database connection successful.")
except Exception as e:
    print(f"Database connection failed: {e}")

