import datetime
import sqlite3
from matplotlib import pyplot as plt
import streamlit as st 

def budget_tracking():
    st.write("Input your financial data below:")

    conn = sqlite3.connect('/Users/aditinarayan/Downloads/Finance/data/finance.db')
    c = conn.cursor()

    with st.form(key='transaction_form'):
        trans_type = st.selectbox("Type", ["Income", "Expense"])
        amount = st.number_input("Amount", min_value=0.0, format="%.2f")
        date = st.date_input("Date", datetime.now())
        submit_button = st.form_submit_button(label='Add Transaction')

        if submit_button:
            user_id = 1  # Assuming user_id is 1 f
            c.execute("INSERT INTO transactions (user_id, type, amount, date) VALUES (?, ?, ?, ?)", (user_id, trans_type, amount, str(date)))
            conn.commit()
            st.success("Transaction added successfully")

    conn.close()


        #  SQLite database
    conn = sqlite3.connect('data/finance.db')
    c = conn.cursor()

    #  fetch transaction data
    c.execute("SELECT date, SUM(amount) FROM transactions GROUP BY date")
    transaction_data = c.fetchall()

    # Close the database connection
    conn.close()

    # Extract dates and total amounts from the fetched data
    dates = [data[0] for data in transaction_data]
    total_amounts = [amount[1] for amount in transaction_data]

    #  expenses and incomes over time
    st.write("### Budget Tracking - Expenses and Incomes Over Time")
    fig1, ax1 = plt.subplots()
    ax1.plot(dates, total_amounts, marker='o', linestyle='-', color='b')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Total Amount')
    ax1.set_title('Expenses and Incomes Over Time')
    ax1.grid(True)
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig1)

    # Pie chart for comparing expenses and incomes
    #st.write("### Budget Tracking - Proportion of Expenses vs Incomes")
    #expenses = [amount for amount in total_amounts if amount < 0]
    #incomes = [amount for amount in total_amounts if amount >= 0]
   # labels = ['Expenses', 'Incomes']
    #sizes = [sum(expenses), sum(incomes)]
    #colors = ['red', 'green']
    #fig2, ax2 = plt.subplots()
    #ax2.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    #ax2.axis('equal')
    #ax2.set_title('Proportion of Expenses vs Incomes')
    #st.pyplot(fig2)

if __name__=="__main__":
    budget_tracking()
