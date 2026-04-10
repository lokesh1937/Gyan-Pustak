import streamlit as st

st.set_page_config(layout="wide")

# ---------------- HEADER ----------------
st.title("📚 GyanPustak")

# ---------------- SIDEBAR (LEFT) ----------------
with st.sidebar:
    st.header("🔍 Search")
    search_query = st.text_input("Search books")

# ---------------- MAIN LAYOUT ----------------
col1, col2, col3 = st.columns([1, 6, 1])

# LEFT EMPTY (for spacing like your sketch)
with col1:
    st.write("")

# CENTER CONTENT (BOOK GRID)
with col2:
    st.subheader("Available Books")

    # Create 2 rows of 2 columns (like your drawing)
    for i in range(2):
        cols = st.columns(2)
        for j in range(2):
            with cols[j]:
                st.container(border=True)
                st.markdown("### 📖 Book Title")
                st.write("Author Name")
                st.write("₹500")
                st.button("View", key=f"btn_{i}_{j}")

# RIGHT SIDE (ORDERS)
with col3:
    st.write("")
    st.write("")
    if st.button("📦 Orders"):
        st.success("Go to Orders Page")
