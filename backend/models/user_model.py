from database import get_db, get_cursor


def find_user(email):
    cursor = get_cursor()
    if cursor is None:
        return None

    query = "SELECT * FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    return cursor.fetchone()


def create_user(user_data):
    db = get_db()
    cursor = get_cursor()
    if db is None or cursor is None:
        raise RuntimeError('Database is not connected')

    query = "INSERT INTO users (email, password) VALUES (%s, %s)"
    cursor.execute(query, (user_data['email'], user_data['password']))
    db.commit()
    return cursor.lastrowid