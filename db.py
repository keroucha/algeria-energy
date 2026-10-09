"""قاعدة SQLite صغيرة تحفظ الزوار (نسخة احتياطية إلى جانب الإيميل)."""
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("visitors.db")


def init() -> None:
    with sqlite3.connect(DB_PATH) as c:
        c.execute("""CREATE TABLE IF NOT EXISTS visitors(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL, lang TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP)""")


def add(email: str, lang: str) -> None:
    with sqlite3.connect(DB_PATH) as c:
        c.execute("INSERT INTO visitors(email, lang) VALUES (?, ?)", (email, lang))
