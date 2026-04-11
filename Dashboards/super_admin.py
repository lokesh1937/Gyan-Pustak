import streamlit as st

st.set_page_config(page_title="Super Admin Dashboard", page_icon="🛠️")

st.title("🛠️ Super Admin Dashboard")

st.subheader("➕ Add New Employee")

# -------- FORM --------
with st.form("employee_form"):

    emp_id = st.text_input("Employee ID")

    col1, col2 = st.columns(2)
    with col1:
        first_name = st.text_input("First Name")
    with col2:
        last_name = st.text_input("Last Name")

    gender = st.selectbox("Gender", ["Male", "Female", "Other"])

    salary = st.number_input("Salary", min_value=0)

    aadhaar = st.text_input("Aadhaar Number")

    email = st.text_input("Email Address")

    address = st.text_area("Address")

    phone = st.text_input("Telephone Number")

    submit = st.form_submit_button("Add Employee")

# -------- OUTPUT --------
if submit:
    if not emp_id or not first_name or not email:
        st.warning("Please fill required fields")
    else:
        st.success("✅ Employee added successfully!")

        st.write("### Entered Data:")
        st.write({
            "Employee ID": emp_id,
            "First Name": first_name,
            "Last Name": last_name,
            "Gender": gender,
            "Salary": salary,
            "Aadhaar": aadhaar,
            "Email": email,
            "Address": address,
            "Phone": phone
        })