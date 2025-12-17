import sqlite3
from datetime import datetime

DB_PATH = 'app.db'

class UserDAO:
    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
        self.create_table()

    def get_conn(self):
        return sqlite3.connect(self.db_path)

    def create_table(self):
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            created_at TEXT NOT NULL
        );
        """)
        conn.commit()
        conn.close()

    def create_user(self, email, username, password):
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute("""
        INSERT INTO users (email, username, password, created_at)
        VALUES (?, ?, ?, ?)
        """, (email, username, password, datetime.utcnow().isoformat()))
        conn.commit()
        conn.close()
        return True

    def get_user_by_email(self, email):
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute("""
        SELECT id, email, username, password, created_at
        FROM users WHERE email=?
        """, (email,))
        row = cur.fetchone()
        conn.close()
        if not row:
            return None
        return {
            "id": row[0],
            "email": row[1],
            "username": row[2],
            "password": row[3],
            "created_at": row[4]
        }

    def get_all_users(self):
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT id, email, username, created_at FROM users")
        rows = cur.fetchall()
        conn.close()
        return rows
