import streamlit as st
from auth import authenticate

st.title("🎓 Student Login")

# Session state for login
if "student_logged_in" not in st.session_state:
    st.session_state.student_logged_in = False

# If not logged in → show login form
if not st.session_state.student_logged_in:

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = authenticate(username, password, "Student")

        if user:
            st.session_state.student_logged_in = True
            st.session_state.username = username
            st.success("Welcome Student!")
            st.rerun()
        else:
            st.error("Invalid credentials")

    # 👉 Signup redirect
    st.markdown("Don't have an account?")
    if st.button("Go to Signup"):
        st.switch_page("pages/4_Student_Signup.py")

# If logged in → show dashboard
else:
    st.success(f"Welcome {st.session_state.username} 🎉")

    st.write("📚 Student Dashboard")
    st.write("- View available books")
    st.write("- Issue books")
    st.write("- Return books")

    if st.button("Logout"):
        st.session_state.student_logged_in = False
        st.session_state.username = ""
        st.rerun()