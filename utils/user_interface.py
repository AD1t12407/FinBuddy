import streamlit as st
from authentication import authenticate, register_user
from dashboard import dashboard

# Home page
def home():
    st.title("Financial Tracking App")
    st.write("Welcome to our financial tracking app!")
    st.write("Learn more about financial tracking and how our app can help you manage your finances.")

    # Login and Register options
    login_selected = st.button("Login")
    register_selected = st.button("Register")

    if login_selected:
        login()
    elif register_selected:
        register()

# Login page
def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login", key="login_button"):
        user = authenticate(username, password)
        if user:
            st.session_state.logged_in = True
            st.session_state.user = user
            st.success("Logged in successfully!")
            dashboard()
        else:
            st.error("Invalid username or password")

# Register page
def register():
    st.markdown("### Or sign up with email:")

    with st.form(key='register_form'):
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")

        # Check if passwords match
        if password != confirm_password:
            st.error("Passwords do not match")
            return

        # Additional details
        full_name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        country = st.text_input("Country")

        # Terms and conditions
        agreed_to_terms = st.checkbox("I agree to the terms and conditions")

        # Submit button
        if st.form_submit_button("Register"):
            if agreed_to_terms:
                # Call a function to handle registration
                register_user(username, email, password, full_name, age, country)
                st.success("Registration successful! You can now log in.")
            else:
                st.error("Please agree to the terms and conditions to register")
