import time
import psycopg2
import os

RETRIES = 10
while RETRIES > 0:
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB", "mydatabase"),
            user=os.getenv("POSTGRES_USER", "user"),
            password=os.getenv("POSTGRES_PASSWORD", "password"),
            host="db"
        )
        print("Database is ready!")
        break
    except psycopg2.OperationalError:
        print("Database not ready, waiting...")
        RETRIES -= 1
        time.sleep(3)
else:
    print("Database connection failed after retries.")
    exit(1)
