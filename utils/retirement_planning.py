import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def retirement_planning():
    st.write("Plan your retirement:")

    conn = sqlite3.connect('data/finance.db')
    c = conn.cursor()

    with st.form(key='retirement_form'):
        retirement_goal = st.text_input("Retirement Goal")
        target_amount = st.number_input("Target Amount", min_value=0.0, format="%.2f")
        current_savings = st.number_input("Current Savings", min_value=0.0, format="%.2f")
        retirement_age = st.number_input("Retirement Age", min_value=0, max_value=100, step=1)
        submit_button = st.form_submit_button(label='Set Retirement Plan')

        if submit_button:
            user_id = 1  # Assuming user_id is 1 for demonstration purposes
            c.execute("INSERT INTO retirement (user_id, goal, target_amount, current_savings, retirement_age) VALUES (?, ?, ?, ?, ?)",
                      (user_id, retirement_goal, target_amount, current_savings, retirement_age))
            conn.commit()
            st.success("Retirement plan set successfully")

    conn.close()
        # Connect to the SQLite database
    conn = sqlite3.connect('data/finance.db')
    c = conn.cursor()

    # Query the database to fetch retirement plans data
    c.execute("SELECT goal, target_amount, current_savings, retirement_age FROM retirement")
    retirement_data = c.fetchall()

    # Close the database connection
    conn.close()

    # Create a DataFrame from the fetched data
    retirement_df = pd.DataFrame(retirement_data, columns=["Goal", "Target Amount", "Current Savings", "Retirement Age"])

    # Display the DataFrame
    st.write("### Your Retirement Plans")
    st.write(retirement_df)

     # Connect to the SQLite database
    conn = sqlite3.connect('data/finance.db')
    c = conn.cursor()

    # Query the database to fetch retirement plan data
    c.execute("SELECT goal, target_amount, current_savings FROM retirement")
    retirement_data = c.fetchall()

    # Close the database connection
    conn.close()

    # Extract retirement goals, target amounts, and current savings from the fetched retirement data
    retirement_goals = [data[0] for data in retirement_data]
    target_amounts = [amount[1] for amount in retirement_data]
    current_savings = [savings[2] for savings in retirement_data]

    # Bar chart for progress towards retirement goals
    st.write("### Retirement Planning - Progress towards Goals")
    fig, ax = plt.subplots()
    bar_width = 0.35
    index = range(len(retirement_goals))
    bar1 = ax.bar(index, current_savings, bar_width, label='Current Savings')
    bar2 = ax.bar([i + bar_width for i in index], [target_amount - savings for target_amount, savings in zip(target_amounts, current_savings)], bar_width, label='Remaining Amount')
    ax.set_xlabel('Retirement Goals')
    ax.set_ylabel('Amount')
    ax.set_title('Progress towards Retirement Goals')
    ax.set_xticks([i + bar_width / 2 for i in index])
    ax.set_xticklabels(retirement_goals, rotation=45, ha='right')
    ax.legend()
    st.pyplot(fig)



if __name__ == "__main__":
    retirement_planning()
