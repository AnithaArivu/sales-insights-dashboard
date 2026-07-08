# Sales Forecasting with Linear Regression

import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("superstore.csv")

# Prepare features
data['Order_Date'] = pd.to_datetime(data['Order_Date'])
data['Month'] = data['Order_Date'].dt.month
monthly_sales = data.groupby('Month')['Sales'].sum().reset_index()

# Train model
X = monthly_sales[['Month']]
y = monthly_sales['Sales']
model = LinearRegression()
model.fit(X, y)

# Predict next month
next_month = [[max(X['Month']) + 1]]
prediction = model.predict(next_month)
print("Predicted Sales for Next Month:", prediction[0])

