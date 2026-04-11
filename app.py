import streamlit as st

st.set_page_config(
    page_title="Gyan Pustak",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="collapsed"   # 👈 hides sidebar by default
)

# Title
st.markdown("<h1 style='text-align: center;'>GYAN PUSTAK</h1>", unsafe_allow_html=True)

st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        [data-testid="collapsedControl"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

st.write("")

# Initialize session state
if "role" not in st.session_state:
    st.session_state.role = None

# Function to set role and rerun immediately
def set_role(role):
    st.session_state.role = role
    st.rerun()   # 🔥 fixes double-click issue

# Show role selection
if st.session_state.role is None:
    st.markdown("### Select Login Type")

    # Custom CSS for bigger buttons
    st.markdown("""
        <style>
        div.stButton > button {
            width: 140%;
            height: 80px;
            font-size: 25px;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Vertical buttons
    if st.button("🎓 Student"):
        set_role("Student")

    if st.button("💼 Employee"):
        set_role("Employee")

    if st.button("🛠️ Super Admin"):
        set_role("Super Admin")

# Login form
else:
    st.success(f"Login as {st.session_state.role}")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.success(f"Welcome {st.session_state.role}!")
        else:
            st.error("Invalid credentials")

    if st.button("⬅ Back"):
        st.session_state.role = None
        st.rerun()