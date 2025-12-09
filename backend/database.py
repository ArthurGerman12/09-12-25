import sqlite3

DB_NAME = "data.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    # -----------------------------------------
    # CREATE TABLES
    # -----------------------------------------

    cur.execute("""
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS sports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            team TEXT NOT NULL,
            score TEXT NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS economy (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            market TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    # -----------------------------------------
    # SEED NEWS (ONLY IF EMPTY)
    # -----------------------------------------
    count = cur.execute("SELECT COUNT(*) FROM news").fetchone()[0]
    if count == 0:
        cur.executemany("""
            INSERT INTO news (title, content)
            VALUES (?, ?)
        """, [
            ("Breaking News: Python Takes Over", "Developers worldwide flock to Python for its simplicity."),
            ("Flask 3.0 Released", "The Flask team releases a major update with improved performance."),
            ("Tech Market Surges", "Investors rally behind AI-focused companies.")
        ])

    # -----------------------------------------
    # SEED SPORTS
    # -----------------------------------------
    count = cur.execute("SELECT COUNT(*) FROM sports").fetchone()[0]
    if count == 0:
        cur.executemany("""
            INSERT INTO sports (team, score)
            VALUES (?, ?)
        """, [
            ("Lakers vs Bulls", "102-97"),
            ("Arsenal vs Chelsea", "2-1"),
            ("Patriots vs Dolphins", "24-20")
        ])

    # -----------------------------------------
    # SEED ECONOMY
    # -----------------------------------------
    count = cur.execute("SELECT COUNT(*) FROM economy").fetchone()[0]
    if count == 0:
        cur.executemany("""
            INSERT INTO economy (market, status)
            VALUES (?, ?)
        """, [
            ("NASDAQ", "Green"),
            ("DOW JONES", "Red"),
            ("S&P 500", "Neutral")
        ])

    # -----------------------------------------

    conn.commit()
    conn.close()
