import streamlit as st
from auth import authenticate

st.title("💼 Employee Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    user = authenticate(username, password, "Employee")

    if user:
        st.success("Welcome Employee!")

        # Example dashboard placeholder
        st.write("📚 Manage books, issue/return system here")

    else:
        st.error("Invalid credentials")