# Mortgage Payments Calculator

This is a simple web application built using Streamlit to calculate mortgage payments and display payment schedules and metrics.

## Overview

This mortgage payments calculator allows users to input various parameters such as home value, deposit, interest rate, and loan term to estimate their monthly mortgage payments. It provides insights into the total payments and total interest paid over the loan term and generates a payment schedule showing the remaining balance over the years.

## How to Use

1. Visit the web app hosted [here](https://mortgage-loan-calculator-b83cyzfhphtrbvzgd5mb9x.streamlit.app/).
2. Input the required parameters:
   - Home value: The total value of the property you intend to purchase.
   - Deposit: The initial payment made towards the home purchase.
   - Interest rate: The annual interest rate for the mortgage.
   - Loan term: The duration of the mortgage in years (e.g., 30-yr, 20-yr, 15-yr, 10-yr).
3. The app will calculate the monthly payments, total payments, and total interest paid based on the provided inputs.
4. It will also generate a payment schedule showing the remaining balance over the years.

## Technologies Used

- [Streamlit](https://streamlit.io/): For building, creating visualizations, and deploying the web application.
- [Pandas](https://pandas.pydata.org/): For data manipulation and analysis.

## Running the App Locally

To run this Streamlit app locally, follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/wdam2002/mortgage-payments-calculator.git

2. Install the required dependencies:
   ```pip install -r requirements.txt```

3. Run the Streamlit app:
   ```streamlit run mortgage_calculator.py```
