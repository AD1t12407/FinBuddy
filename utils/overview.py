import streamlit as st
import sqlite3
# Overview Page
def overview():

    st.write("Overview of your financial status and goals.")

    # connect to database
    conn = sqlite3.connect('data/finance.db')
    c = conn.cursor()

    # fetch user data (assuming user_id is 1 for demonstration purposes)
    user_id = 1

    # fetch transaction data
    c.execute("SELECT type, SUM(amount) FROM transactions WHERE user_id=? GROUP BY type", (user_id,))
    transaction_summary = c.fetchall()

    # fetch transactions for line chart
    c.execute("SELECT date, SUM(amount) FROM transactions WHERE user_id=? GROUP BY date", (user_id,))
    transaction_timeline = c.fetchall()

    # fetch savings goals
    c.execute("SELECT goal, target_amount, saved_amount FROM goals WHERE user_id=?", (user_id,))
    savings_goals = c.fetchall()

    conn.close()

    # convert transaction summary to DataFrame
    df_transaction_summary = pd.DataFrame(transaction_summary, columns=["Type", "Total Amount"])
    
    # convert transaction timeline to DataFrame
    df_transaction_timeline = pd.DataFrame(transaction_timeline, columns=["Date", "Total Amount"])
    
    # convert savings goals to DataFrame
    df_savings_goals = pd.DataFrame(savings_goals, columns=["Goal", "Target Amount", "Saved Amount"])

    #  transactions by category as a pie chart
    st.write("### Income vs Expense")
    fig1, ax1 = plt.subplots()
    income_expense_labels = df_transaction_summary["Type"].tolist()
    income_expense_amounts = df_transaction_summary["Total Amount"].tolist()
    ax1.pie(income_expense_amounts, labels=income_expense_labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    ax1.set_title("Income vs Expense")
    st.pyplot(fig1)


    # Display income and expenses over time as a line chart
    st.write("### Income and Expenses Over Time")
    df_transaction_timeline["Date"] = pd.to_datetime(df_transaction_timeline["Date"])
    df_transaction_timeline.set_index("Date", inplace=True)
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    ax2.plot(df_transaction_timeline.index, df_transaction_timeline["Total Amount"], marker='o', linestyle='-')
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Amount")
    ax2.set_title("Income and Expenses Over Time")
    ax2.grid(True)
    st.pyplot(fig2)

   
    

    # savings goals progress as a bar chart
    st.write("### Savings Goals Progress")
    fig3, ax3 = plt.subplots()
    ax3.barh(df_savings_goals["Goal"], df_savings_goals["Saved Amount"], color='green', label='Saved Amount')
    ax3.barh(df_savings_goals["Goal"], df_savings_goals["Target Amount"] - df_savings_goals["Saved Amount"], left=df_savings_goals["Saved Amount"], color='red', label='Remaining Amount')
    ax3.set_xlabel('Amount')
    ax3.set_ylabel('Goal')
    ax3.set_title('Savings Goals Progress')
    ax3.legend()
    st.pyplot(fig3)

if __name__=="__main__":
    overview()