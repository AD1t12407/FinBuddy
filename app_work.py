import streamlit as st
import sqlite3
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import openai
import requests

# Set your OpenAI API key
openai_api_key = "sk-proj-BLldiuhVnIFSCjp7r3LcT3BlbkFJhp5jXm5uwhWOlVEkD2Lo"


# Function to generate financial advice using OpenAI API
def get_advice(user_input):
    try:
        # Make a POST request to the OpenAI API to generate advice based on the prompt
        response = requests.post(
            "https://api.openai.com/v1/engines/text-davinci-003/completions",
            headers={
                "Authorization": f"Bearer {openai_api_key}",
                "Content-Type": "application/json"
            },
            json={
                "prompt": user_input,
                "max_tokens": 200
            }
        )
        data = response.json()
        if 'choices' in data and len(data['choices']) > 0:
            advice = data['choices'][0]['text'].strip()
            return advice
        else:
            return "No advice generated."
    except Exception as e:
        return f"An error occurred: {str(e)}"
# Dashboard page
def dashboard():
    st.title("Dashboard")
    st.write("This is the dashboard. You can access various features related to financial tracking here.")

    # Navigation for dashboard features
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
        investment_portfolio_management()

    elif dashboard_page == "Retirement Planning":
        st.subheader("Retirement Planning")
        retirement_planning()

# Set up financial news API key
news_api_key = "9c364d44f202437fa167782d1d075057"

# Function to get financial news
def get_news():
    try:
        today = date.today()
        response = requests.get(
            f"https://newsapi.org/v2/everything?q=finance&from={today}&sortBy=publishedAt&apiKey={news_api_key}"
        )
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])
            return articles
        else:
            # You can print the status code and error message here, or handle it as per your app's error handling strategy
            print(f"Failed to fetch news: {response.status_code}")
            return []
    
    except Exception as e:
        # Log the exception; You could use logging instead of print in production applications
        print(f"An error occurred: {str(e)}")
        return []

# Overview Page
def overview():



    st.write("Overview of your financial status and goals.")

    # Connect to database
    conn = sqlite3.connect('data/finance.db')
    c = conn.cursor()

    # Fetch user data (assuming user_id is 1 for demonstration purposes)
    user_id = 1

    # Fetch transaction data
    c.execute("SELECT type, SUM(amount) FROM transactions WHERE user_id=? GROUP BY type", (user_id,))
    transaction_summary = c.fetchall()

    # Fetch transactions for line chart
    c.execute("SELECT date, SUM(amount) FROM transactions WHERE user_id=? GROUP BY date", (user_id,))
    transaction_timeline = c.fetchall()

    # Fetch savings goals
    c.execute("SELECT goal, target_amount, saved_amount FROM goals WHERE user_id=?", (user_id,))
    savings_goals = c.fetchall()

    conn.close()

    # Convert transaction summary to DataFrame
    df_transaction_summary = pd.DataFrame(transaction_summary, columns=["Type", "Total Amount"])
    
    # Convert transaction timeline to DataFrame
    df_transaction_timeline = pd.DataFrame(transaction_timeline, columns=["Date", "Total Amount"])
    
    # Convert savings goals to DataFrame
    df_savings_goals = pd.DataFrame(savings_goals, columns=["Goal", "Target Amount", "Saved Amount"])

    # Display transactions by category as a pie chart
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

   
    

    # displaying savings goals progress as a bar chart
    st.write("### Savings Goals Progress")
    fig3, ax3 = plt.subplots()
    ax3.barh(df_savings_goals["Goal"], df_savings_goals["Saved Amount"], color='green', label='Saved Amount')
    ax3.barh(df_savings_goals["Goal"], df_savings_goals["Target Amount"] - df_savings_goals["Saved Amount"], left=df_savings_goals["Saved Amount"], color='red', label='Remaining Amount')
    ax3.set_xlabel('Amount')
    ax3.set_ylabel('Goal')
    ax3.set_title('Savings Goals Progress')
    ax3.legend()
    st.pyplot(fig3)

    # displaying the financial news

    st.write("### Financial News")
    news_articles = get_news()
    if news_articles:
        for article in news_articles:
            st.write(f"- [{article['title']}]({article['url']})")
    else:
        st.write("Unable to fetch financial news at the moment.")

# Budget Tracking
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
            user_id = 1  # Assuming user_id is 1 for demonstration purposes
            c.execute("INSERT INTO transactions (user_id, type, amount, date) VALUES (?, ?, ?, ?)", (user_id, trans_type, amount, str(date)))
            conn.commit()
            st.success("Transaction added successfully")

    conn.close()


        # Connect to the SQLite database
    conn = sqlite3.connect('data/finance.db')
    c = conn.cursor()

    # Query the database to fetch transaction data
    c.execute("SELECT date, SUM(amount) FROM transactions GROUP BY date")
    transaction_data = c.fetchall()

    # Close the database connection
    conn.close()

    # Extract dates and total amounts from the fetched data
    dates = [data[0] for data in transaction_data]
    total_amounts = [amount[1] for amount in transaction_data]

    # Line chart for expenses and incomes over time
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

# Goal Setting
def goal_setting():
    st.write("Set and track your financial goals:")

    conn = sqlite3.connect('data/finance.db')
    c = conn.cursor()

    with st.form(key='goal_form'):
        goal = st.text_input("Goal")
        target_amount = st.number_input("Target Amount", min_value=0.0, format="%.2f")
        submit_button = st.form_submit_button(label='Set Goal')

        if submit_button:
            user_id = 1  # Assuming user_id is 1 for demonstration purposes
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

# Investment Portfolio Management
def investment_portfolio_management():
    st.write("Manage and analyze your investment portfolio:")

    conn = sqlite3.connect('data/finance.db')
    c = conn.cursor()

    with st.form(key='investment_form'):
        investment_type = st.selectbox("Investment Type", ["Stocks", "Bonds", "Mutual Funds", "Real Estate", "Other"])
        amount_invested = st.number_input("Amount Invested", min_value=0.0, format="%.2f")
        date = st.date_input("Date of Investment", datetime.now())
        submit_button = st.form_submit_button(label='Add Investment')

        if submit_button:
            user_id = 1  # Assuming user_id is 1 for demonstration purposes
            c.execute("INSERT INTO investments (user_id, type, amount_invested, date) VALUES (?, ?, ?, ?)", (user_id, investment_type, amount_invested, str(date)))
            conn.commit()
            st.success("Investment added successfully")

    conn.close()

    # Display existing investments
        # Connect to the SQLite database
    conn = sqlite3.connect('data/finance.db')
    c = conn.cursor()

    # Query the database to fetch investment data
    c.execute("SELECT type, amount_invested, date FROM investments")
    investments_data = c.fetchall()

    # Close the database connection
    conn.close()

    # Create a DataFrame from the fetched data
    investment_df = pd.DataFrame(investments_data, columns=["Type", "Amount Invested", "Date"])

    st.write("### Your Investment Plans")
    st.write(investment_df)

    # Connect to the SQLite database
    conn = sqlite3.connect('data/finance.db')
    c = conn.cursor()

    # Query the database to fetch investment data
    c.execute("SELECT type, SUM(amount_invested) FROM investments GROUP BY type")
    investment_data = c.fetchall()

    # Close the database connection
    conn.close()

    # Extract investment types and total amounts from the fetched investment data
    investment_types = [data[0] for data in investment_data]
    investment_amounts = [amount[1] for amount in investment_data]

    # Bar chart for distribution of investments by type
    st.write("### Investments - Distribution by Type")
    fig, ax = plt.subplots()
    ax.barh(investment_types, investment_amounts, color='skyblue')
    ax.set_xlabel('Amount Invested')
    ax.set_ylabel('Investment Type')
    ax.set_title('Distribution of Investments by Type')
    st.pyplot(fig)

    # Export the DataFrame to an Excel sheet
    #excel_file_path = "investment_data.xlsx"
    #investment_df.to_excel(excel_file_path, index=False)
    #st.write(f"Exported investment data to {excel_file_path}")

   
# Retirement Planning
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



    
# Main function to run the app
def main():

    dashboard()
    st.title("Financial Advice Generator")

    # Form for user input
    with st.form(key='advice_form'):
        user_input = st.text_area("Ask for financial advice:")
        submit_button = st.form_submit_button(label='Get Advice')

        if submit_button and user_input:
            # Generate financial advice based on user input
            advice = get_advice(user_input)
            
            # Display the generated advice
            st.subheader("Generated Advice:")
            st.write(advice)

    
    
    
    


if __name__ == "__main__":
    main()
