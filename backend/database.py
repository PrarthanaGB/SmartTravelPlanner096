import mysql.connector
from mysql.connector import errorcode
from config import Config

# Global database connection variables
db = None
cursor = None

def init_database():
    global db, cursor
    try:
        db = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB
        )
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            print(f"Database '{Config.MYSQL_DB}' not found. Creating it now...")
            try:
                admin_conn = mysql.connector.connect(
                    host=Config.MYSQL_HOST,
                    user=Config.MYSQL_USER,
                    password=Config.MYSQL_PASSWORD
                )
                admin_cursor = admin_conn.cursor()
                admin_cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{Config.MYSQL_DB}`")
                admin_conn.commit()
                admin_cursor.close()
                admin_conn.close()
                db = mysql.connector.connect(
                    host=Config.MYSQL_HOST,
                    user=Config.MYSQL_USER,
                    password=Config.MYSQL_PASSWORD,
                    database=Config.MYSQL_DB
                )
            except mysql.connector.Error as err2:
                print(f"Database creation failed: {err2}")
                return _demo_mode(err2)
        else:
            return _demo_mode(err)

    cursor = db.cursor(dictionary=True)
    _create_tables()
    print("Database connected successfully!")
    return True


def _demo_mode(error):
    print(f"Database connection failed: {error}")
    print("Running in demo mode without database...")
    global db, cursor
    db = None
    cursor = None
    return False


def _create_tables():
    global db, cursor
    if db is None or cursor is None:
        return
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    db.commit()


def get_db():
    return db


def get_cursor():
    return cursor
