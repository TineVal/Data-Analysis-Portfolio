import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\valentine\DATA ANALYSIS\PYTHON\sample_data.csv')
print(data.head())
print(data.info())
print(data.dtypes)
print(data.isnull().sum())

# Convert 'Date' column to datetime type (if it's not already)
data['Date'] = pd.to_datetime(data['Date'])

# Create a new column for total sales (Price * Quantity)
data['Total Sales'] = data['Price'] * data['Quantity']


#Basic Statistics
statistics = data.describe()
print(statistics)

#Group Data
grouped_quantity = data.groupby('Product')['Quantity'].mean()
print(grouped_quantity)

average_price = data.groupby('Product')['Price'].mean()
print(average_price)

#Checking for Patterns
max_quantity_product = grouped_quantity.idxmax()
max_quantity = grouped_quantity.max()
print(f"\nThe product with the highest average quantity sold is {max_quantity_product} with {max_quantity} units sold on average.")

#Plotting The Visualization Graphs
# Plotting the line chart for total sales over time
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Total Sales'], marker='o', color='b', linestyle='-', label='Total Sales')
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)  
plt.legend()
plt.tight_layout()  
plt.show()

# 2. Bar Chart - Average Quantity Sold by Product
grouped_quantity = data.groupby('Product')['Quantity'].mean()
plt.figure(figsize=(10, 6))
grouped_quantity.plot(kind='bar', color=['orange', 'green', 'blue'])
plt.title('Average Quantity Sold by Product')
plt.xlabel('Product')
plt.ylabel('Average Quantity Sold')
plt.xticks(rotation=0)
plt.show()

# 3. Histogram - Distribution of Product Prices
plt.figure(figsize=(10, 6))
plt.hist(data['Price'], bins=5, color='purple', edgecolor='black')
plt.title('Distribution of Product Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter Plot - Price vs Quantity Sold
plt.figure(figsize=(10, 6))
plt.scatter(data['Price'], data['Quantity'], color='red', alpha=0.6)
plt.title('Price vs Quantity Sold')
plt.xlabel('Price')
plt.ylabel('Quantity Sold')
plt.show()
