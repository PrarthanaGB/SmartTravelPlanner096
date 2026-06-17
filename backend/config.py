import os
from pathlib import Path
from dotenv import load_dotenv

root = Path(__file__).parent
load_dotenv(dotenv_path=root / '.env')
load_dotenv(dotenv_path=root / 'configure.env', override=False)

class Config:
    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
    MYSQL_DB = os.getenv("MYSQL_DB", "travel_db")
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key_here")
    