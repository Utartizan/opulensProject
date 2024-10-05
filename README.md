# Welcome to Opulens - Your Financial Budgeting Companion!
Opulens is designed to help you visualise and manage your finances effectively. Using advanced PostgreSQL databases and Tableau, the app turns your financial data into insightful visualisations to support better budgeting decisions.

## How to Install and Run Opulens:
No installation required! Simply click on the link below to access the platform.



## How to Use Opulens:
Enter your monthly income (must be a non-negative value).

Provide your fixed monthly expenses such as rent, mortgage, utilities, and subscriptions.

Input variable monthly expenses like groceries, transportation, and leisure activities.

Record any debt payments (e.g., loans, credit cards) along with interest rates and payment amounts.

Specify your savings goals, such as emergency funds or future investments, and the desired savings percentage of your income.

Track additional income sources like side gigs or dividends.

Click the "Generate Financial Summary" button to view your financial health dashboard, complete with detailed visualisations of your spending, savings, and debt repayment progress.

## Methodology:
Opulens connects to a PostgreSQL database that stores your financial inputs. Tableau processes this data to create interactive visualisations, helping you identify trends in your spending habits, set achievable financial goals, and monitor debt management. Key financial indicators include income, savings rate, debt-to-income ratio, and expense distribution.

## Visualisations:
The visualisations on Opulens include:

Income vs. Expenses Breakdown: Bar or pie charts showing your total income and how it is divided among fixed, variable, and debt-related expenses.

Savings Projection: A line chart showing how much you can save over time based on your input goals.

Debt Repayment Progress: A visual tracker of your debt repayment schedule.

Spending Trends: A time-series analysis that helps you monitor fluctuations in spending habits over time.

##Interpretation of Results:
Healthy Budget: If your savings rate is above 20% and your debt-to-income ratio is below 36%, your finances are on track.

Warning: If your debt-to-income ratio is between 37-49% or your savings rate is below 10%, consider reducing expenses or increasing savings.

Critical: A debt-to-income ratio over 50% signals high financial risk. Immediate action may be needed.

## Acknowledgements:
Opulens was developed using PostgreSQL for data storage and Tableau for powerful data visualisation. The app's user interface is designed for ease of use, allowing you to gain insights into your finances without any technical knowledge.

## Data Security:
We take privacy seriously. All financial data is securely stored in a PostgreSQL database which is encrypted via PBKDF2-SHA256, and visualisations are created without compromising your sensitive information. No personal data is shared with third parties.
