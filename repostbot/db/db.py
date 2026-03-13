import os
import sqlite3


def get_db_path() -> str:
    return os.environ.get("REPOST_DB_PATH", "repostdb.sqlite")


def connect_db() -> sqlite3.Connection:
    db_path = get_db_path()
    db_directory = os.path.dirname(db_path)
    if db_directory:
        os.makedirs(db_directory, exist_ok=True)
    return sqlite3.connect(db_path)
