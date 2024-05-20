import streamlit as st
from user_interface import home, login, register
from dashboard import dashboard
from budget_tracking import budget_tracking
from goal_tracking import goal_setting
from investment_analysis import investment_portfolio
from retirement_planning import retirement_planning

def main():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        dashboard()
    else:
        page = st.sidebar.selectbox("Navigation", ["Home", "Login", "Register"])

        if page == "Home":
            home()
        elif page == "Login":
            login()
        elif page == "Register":
            register()

if __name__ == "__main__":
    main()
