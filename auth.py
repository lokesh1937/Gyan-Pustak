from db import get_connection

def authenticate(username, password, role):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username=%s AND password=%s AND role=%s"
    cursor.execute(query, (username, password, role))

    user = cursor.fetchone()
    conn.close()

    return user