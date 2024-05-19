import streamlit as st
from scripts.create_users import init_db, validate_login, user_exists, add_user

# Initialize database
init_db()

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
    st.subheader("Login")
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")

    if st.button("Login", key="login_button"):
        if validate_login(username, password):
            st.markdown(f"Welcome back, {username}!")
            # Access the user's data or redirect to their dashboard
        else:
            st.error("Invalid username or password.")

# Register page
def register():
    st.subheader("Register")
    username = st.text_input("Username", key="register_username")
    email = st.text_input("Email", key="register_email")
    password = st.text_input("Password", type="password", key="register_password")
    confirm_password = st.text_input("Confirm Password", type="password", key="register_confirm_password")
    full_name = st.text_input("Full Name", key="register_full_name")
    age = st.number_input("Age", min_value=0, key="register_age")
    country = st.text_input("Country", key="register_country")

    if st.button("Register", key="register_button"):
        if password != confirm_password:
            st.error("Passwords do not match.")
        elif user_exists(username):
            st.error("Username already exists.")
        else:
            add_user(username, email, password, full_name, age, country)
            st.success("Registration successful! Please login.")

# Run the app
home()
