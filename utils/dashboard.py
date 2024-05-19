from .overview import overview
import streamlit as st

from .budget_tracking import budget_tracking
from .goal_tracking import goal_setting
from .investment_analysis import investment_portfolio
from .retirement_planning import retirement_planning

def dashboard():
    st.title("Dashboard")
    st.write("This is the dashboard. You can access various features related to financial tracking here.")

    #  dashboard features
    dashboard_page = st.sidebar.radio("Dashboard Navigation", ["Overview", "Budget Tracking", "Goal Setting", "Investment Portfolio", "Retirement Planning"])

    if dashboard_page == "Overview":
        st.subheader("Overview")
        overview()

    elif dashboard_page == "Budget Tracking":
        st.subheader("Budget Tracking")
        budget_tracking()

    elif dashboard_page == "Goal Setting":
        st.subheader("Goal Setting")
        goal_setting()

    elif dashboard_page == "Investment Portfolio":
        st.subheader("Investment Portfolio Management")
        investment_portfolio()

    elif dashboard_page == "Retirement Planning":
        st.subheader("Retirement Planning")
        retirement_planning()


dashboard()
