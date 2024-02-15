import streamlit as st
import pandas as pd
import math

# Set the title of web app
st.title('Mortgage Payments Calculator')

# Display input data section
st.write('### Input data')
col1, col2 = st.columns(2)

# Define input fields for home value and deposit
with col1:
    home_value = st.number_input('Home value', min_value=0, value=500000)
    deposit = st.number_input('Deposit', min_value=0, value=100000)

# Define input fields for interest rate and loan term
with col2:
    interest_rate = st.number_input('Interest rate', min_value=0.0, value=7.47)
    loan_term_options = ['30-yr', '20-yr', '15-yr', '10-yr']
    loan_term = st.selectbox(
        'Loan term', loan_term_options, index=loan_term_options.index('30-yr'))

# Extract years from the loan term selection
loan_term = int(loan_term.split('-')[0])

# Calculate loan amount, monthly interest rate, number of payments, and monthly payment
loan_amount = home_value - deposit
monthly_interest_rate = interest_rate / 12 / 100
number_of_payments = loan_term * 12

_ = """ Formula to compute monthly mortgage payment:
M = P * [I(1 + I)^N] / [(1 + I)^N - 1]

* M = Monthly payment: This is what you're solving for.
* P = Principal amount: This is the loan balance, or what you're trying to pay off.
* I = Interest rate: Remember, you'll want to use the base interest rate and not the APR. Additionally, because the mortgage interest rate you're charged is an
  annual interest rate that represents the interest that's supposed to be paid over the whole year, you want to divide this by 12 to get the monthly interest rate.
* N = Number of payments: This is the total number of payments in your loan term. For instance, if it's a 30-year mortgage with monthly payments, there are 360 payments.
"""
monthly_payment = (
    loan_amount
    * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments)
    / ((1 + monthly_interest_rate) ** number_of_payments - 1)
)

# Calculate total payments and total interest paid
total_payments = monthly_payment * number_of_payments
total_interest = total_payments - loan_amount

# Display payment metrics
st.write('### Payments')
col1, col2, col3 = st.columns(3)
col1.metric(label="Monthly Payments", value=f"${monthly_payment:,.2f}")
col2.metric(label="Total Payments", value=f"${total_payments:,.0f}")
col3.metric(label="Total Interest", value=f"${total_interest:,.0f}")

# Generate the payment schedule
schedule = []
remaining_balance = loan_amount

# Loop through each month to calculate payment details
for i in range(1, number_of_payments + 1):
    interest_payment = remaining_balance * monthly_interest_rate
    principal_payment = monthly_payment - interest_payment
    remaining_balance -= principal_payment
    year = math.ceil(i / 12)
    schedule.append(
        [
            i,
            monthly_payment,
            interest_payment,
            principal_payment,
            remaining_balance,
            year,
        ]
    )

# Create a DataFrame from the payment schedule
df = pd.DataFrame(
    schedule,
    columns=['Month', 'Payment', 'Principal',
             'Interest', 'Remaining Balance', 'Year'],
)

# Display payment schedule
st.write('### Payment Schedule')

# Create a line chart showing the remaining balance over the years
payments_df = df[['Year', 'Remaining Balance']].groupby('Year').min()
st.line_chart(payments_df)
