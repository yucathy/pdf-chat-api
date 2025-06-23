# app/query_log.py
import sqlite3
from datetime import datetime

DB_PATH = "app/query_history.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS query_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            answer TEXT,
            pdf_path TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_query(question: str, answer: str, pdf_path: str):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        INSERT INTO query_log (question, answer, pdf_path, timestamp)
        VALUES (?, ?, ?, ?)
    ''', (question, answer, pdf_path, datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()
