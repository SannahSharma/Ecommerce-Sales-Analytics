import pandas as pd

# Load datasets
customers = pd.read_csv("olist_customers_dataset.csv")
orders = pd.read_csv("olist_orders_dataset.csv")
payments = pd.read_csv("olist_order_payments_dataset.csv")

# Merge
df = orders.merge(customers, on="customer_id")
df = df.merge(payments, on="order_id")

# Convert date
df['order_purchase_timestamp'] = pd.to_datetime(
    df['order_purchase_timestamp']
)

# Monthly Revenue
monthly_revenue = (
    df.groupby(
        df['order_purchase_timestamp'].dt.to_period('M')
    )['payment_value']
    .sum()
    .reset_index()
)

monthly_revenue.columns = ['month', 'revenue']

monthly_revenue.to_csv(
    'monthly_revenue.csv',
    index=False
)

print(monthly_revenue.head())