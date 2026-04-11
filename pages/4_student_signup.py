import streamlit as st
from db import get_connection

st.title("📝 Student Signup")

# ---------- Functions ----------

def user_exists(username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    result = cursor.fetchone()

    conn.close()
    return result


def create_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
    cursor.execute(query, (username, password, "Student"))

    conn.commit()
    conn.close()


# ---------- UI ----------

username = st.text_input("Username")
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

if st.button("Sign Up"):

    if not username or not password:
        st.warning("Please fill all fields")

    elif len(password) < 4:
        st.warning("Password must be at least 4 characters")

    elif password != confirm_password:
        st.error("Passwords do not match")

    elif user_exists(username):
        st.error("Username already exists")

    else:
        create_user(username, password)
        st.success("✅ Account created successfully!")

        # Optional: redirect to login
        if st.button("Go to Login"):
            st.switch_page("pages/1_Student_Login.py")