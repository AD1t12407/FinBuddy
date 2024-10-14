# Financial Planning

This tool analyzes user’s financial data, identifies their financial goals and priorities, and recommends personalized strategies to achieve them. It provides features such as budget tracking, goal setting, investment portfolio management, and retirement planning, helping users make informed financial decisions and achieve long-term financial success.

## Motivation 
Financial literacy and advisory services, is an area which is crucial yet often overlooked in traditional education systems. Finance is a necessity that impacts everyone's life, but unfortunately, it is not a part of the standard school curriculum unless one specifically pursues it as a field of study.
As college students who have just started earning and managing our own money, we understand the importance of financial literacy firsthand. Whether it's dealing with pocket
money, part-time job earnings, or just navigating the basics of personal finance, we often findourselves lost. We don't realize where we are spending, how to save, or what loans and
investments are like and what interest rates mean. This gap leaves many individuals ill-prepared to manage their finances effectively as they grow older.

### Financial Dashboard with Streamlit

This application provides a comprehensive financial dashboard for tracking, managing, and planning your finances. It includes features for overview, budget tracking, goal setting, investment portfolio management, retirement planning, and a financial advice generator using OpenAI's API.

### Setup and Usage

1. **Dependencies**: Make sure you have the following dependencies installed:

   - Streamlit
   - SQLite3
   - Pandas
   - Matplotlib
   - OpenAI
   - Requests

2. **API Keys**: You need to set up API keys for OpenAI and NewsAPI. Replace `openai_api_key` and `news_api_key` variables in the code with your respective API keys.

3. **Database**: Ensure you have a SQLite database named `finance.db` in the `data` directory. You can adjust the database path as per your setup.

4. **Running the App**: Execute the script and open the Streamlit app in your browser. You can run the script using the command `streamlit run filename.py`.

### Features

1. **Overview**: Provides an overview of your financial status and goals, including income vs. expense breakdown, income and expenses over time, and progress towards savings goals.

2. **Budget Tracking**: Allows input of financial transactions, tracks expenses and incomes over time, and provides visualization of budget tracking data.

3. **Goal Setting**: Enables setting and tracking financial goals with target amounts and visualization of goal distribution.

4. **Investment Portfolio Management**: Manages and analyzes your investment portfolio, allowing addition of investments, visualization of distribution by type, and viewing existing investments.

5. **Retirement Planning**: Helps in planning your retirement by setting goals, tracking progress towards retirement goals, and visualization of retirement plans.

6. **Financial Advice Generator**: Utilizes OpenAI's API to generate financial advice based on user input.

## SCREENSHOTS
<img width="1421" alt="Screenshot 2024-10-14 at 8 13 00 PM" src="https://github.com/user-attachments/assets/18ec74c0-7a87-4fca-8622-8cdc053ee025">
<img width="1439" alt="Screenshot 2024-10-14 at 8 25 37 PM" src="https://github.com/user-attachments/assets/5cc4cf40-6b01-4d85-bf56-d23199f05ac4">
<img width="1433" alt="Screenshot 2024-10-14 at 8 26 21 PM" src="https://github.com/user-attachments/assets/af826cc2-5e0a-4b36-9833-0dfed7f5eb40">
<img width="1440" alt="Screenshot 2024-10-14 at 8 26 38 PM" src="https://github.com/user-attachments/assets/885022d3-f6c8-4aa2-a12d-36453c16e7dc">
<img width="1434" alt="Screenshot 2024-10-14 at 8 26 58 PM" src="https://github.com/user-attachments/assets/cc4a8381-b111-45a7-8d75-eddd236c8127">



### Additional Notes

- The application assumes a user ID of 1 for demonstration purposes. You can adjust it as per your user management system.
- Error handling is implemented for API requests and database operations. Ensure appropriate error handling strategy for your production environment.
- Financial news fetching functionality uses NewsAPI. You may need to adjust the API request parameters or endpoint based on your requirements.

## (To be Implemented)

The application currently lacks user login and registration functionality.

- **User Authentication**: Implementing login and registration functionality to allow users to create accounts, log in securely, and access personalized features and data.

Machine learning integration are essential components to enhance the intelligence of the financial applicatio

- **Machine Learning Integration**: Integrating machine learning models to provide intelligent insights and personalized recommendations for financial decision-making.
