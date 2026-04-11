import streamlit as st
from auth import authenticate

st.title("🛠️ Super Admin Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    user = authenticate(username, password, "Admin")

    if user:
        st.success("Welcome Super Admin!")

        # Example admin controls
        st.write("⚙️ Add/remove employees, manage system")

    else:
        st.error("Invalid credentials")