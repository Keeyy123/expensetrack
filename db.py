import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("PG_HOST", "localhost"),
        port=os.getenv("PG_PORT", 5432),
        dbname=os.getenv("PG_NAME", "postgres"),
        user=os.getenv("PG_USER", "contactuser"),
        password=os.getenv("PG_PASSWORD", "contactpass123")
    )

def setup_database():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id   SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id          SERIAL PRIMARY KEY,
            description TEXT NOT NULL,
            amount      NUMERIC(10,2) NOT NULL,
            category_id INTEGER REFERENCES categories(id),
            date        DATE NOT NULL DEFAULT CURRENT_DATE
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

