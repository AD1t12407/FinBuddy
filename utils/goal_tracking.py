import streamlit as st
import sqlite3
import matplotlib.pyplot as plt

def goal_setting():
    st.write("Set and track your financial goals:")

    conn = sqlite3.connect('data/finance.db')
    c = conn.cursor()

    with st.form(key='goal_form'):
        goal = st.text_input("Goal")
        target_amount = st.number_input("Target Amount", min_value=0.0, format="%.2f")
        submit_button = st.form_submit_button(label='Set Goal')

        if submit_button:
            user_id = 1  # Assuming user_id is 1 
            c.execute("INSERT INTO goals (user_id, goal, target_amount, saved_amount) VALUES (?, ?, ?, 0)", (user_id, goal, target_amount))
            conn.commit()
            st.success("Goal set successfully")

    conn.close()

        # Connect to the SQLite database
    conn = sqlite3.connect('data/finance.db')
    c = conn.cursor()

    # Query the database to fetch goal setting data
    c.execute("SELECT goal, target_amount FROM goals")
    goals_data = c.fetchall()

    # Close the database connection
    conn.close()

    # Extract goals and target amounts from the fetched data
    goals = [goal[0] for goal in goals_data]
    target_amounts = [amount[1] for amount in goals_data]

    # Bar chart for goal setting
    st.write("### Goal Setting - Target Amounts")
    fig1, ax1 = plt.subplots()
    ax1.bar(goals, target_amounts)
    ax1.set_xlabel('Goals')
    ax1.set_ylabel('Target Amounts')
    ax1.set_title('Target Amounts for Different Goals')
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig1)

    # Pie chart for goal setting
    st.write("### Goal Setting - Target Amounts Distribution")
    fig2, ax2 = plt.subplots()
    ax2.pie(target_amounts, labels=goals, autopct='%1.1f%%', startangle=90)
    ax2.axis('equal')
    ax2.set_title('Distribution of Target Amounts for Goals')
    st.pyplot(fig2)

goal_setting()
