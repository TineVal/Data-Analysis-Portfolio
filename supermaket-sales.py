import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Create Connection
conn = sqlite3.connect('supermarket-sales.db')

#Reading csv file
df = pd.read_csv ("C:/valentine/DATA ANALYSIS/PYTHON/Supermarket Sales Analysis/supermarket_sales - Sheet1.csv")

#Exploratory Data Analysis
#print(df.info())
#print(df.head(10))
#print(df.describe())

#Storing Data into Database
df.to_sql('supermarket_sales', conn, if_exists='replace', index = False)

#Query Data
query = 'SELECT "Branch", COUNT(*) AS TOTAL_SALES FROM Supermarket_sales GROUP BY "Branch";'
df_result = pd.read_sql_query(query, conn)
query_1 = 'SELECT "Branch", SUM("gross income") AS TOTAL_INCOME FROM Supermarket_sales GROUP BY "Branch" ORDER BY "Branch" DESC;' 
df_result_1 = pd.read_sql_query(query_1, conn)
query_2 = 'SELECT "Customer Type", COUNT (*) AS TOTAL FROM Supermarket_sales GROUP BY "Customer Type";'
df_result_2 = pd.read_sql_query(query_2, conn)
query_3 = 'SELECT "Customer Type", SUM("gross income") AS TOTAL_INCOME FROM Supermarket_sales GROUP BY "Customer Type";'
df_result_3 = pd.read_sql_query(query_3, conn)
query_4 = 'SELECT "Customer Type", AVG("Rating") AS AVG_RATING FROM Supermarket_sales GROUP BY "Customer Type";'
df_result_4 = pd.read_sql_query(query_4, conn)
query_5 = 'SELECT "Gender", COUNT (*) AS TOTAL FROM Supermarket_sales GROUP BY "Gender";'
df_result_5 = pd.read_sql_query(query_5, conn)
query_6 = 'SELECT "Product Line", SUM(CASE WHEN "Gender" = "Male" THEN 1 ELSE 0 END) AS Male_Count, SUM(CASE WHEN "Gender" = "Female" THEN 1 ELSE 0 END) AS Female_Count FROM Supermarket_sales GROUP BY "Product Line";'
df_result_6 = pd.read_sql_query(query_6, conn)
query_7 = 'SELECT "Product Line", COUNT(*) AS TOTAL FROM Supermarket_sales GROUP BY "Product Line" ORDER BY TOTAL DESC;'
df_result_7 = pd.read_sql_query(query_7, conn)
query_8 = 'SELECT "Product Line", AVG("Rating") AS AVG_RATING FROM Supermarket_sales GROUP BY "Product Line";'
df_result_8 = pd.read_sql_query(query_8, conn)
query_9 =  'SELECT "Product Line", SUM("gross income") AS TOTAL_INCOME FROM Supermarket_sales GROUP BY "Product Line";'
df_result_9 = pd.read_sql_query(query_9, conn)
query_10 = 'SELECT "Payment Method", COUNT (*) AS TOTAL FROM Supermarket_sales GROUP BY "Payment Method";' 
df_result_10 = pd.read_sql_query(query_10, conn)
query_11 = 'SELECT "Payment Method", SUM("gross income") AS TOTAL_INCOME FROM Supermarket_sales GROUP BY "Payment Method";'
df_result_11 = pd.read_sql_query(query_11, conn)
query_12 = 'SELECT "Payment Method", AVG("Rating") AS AVG_RATING FROM Supermarket_sales GROUP BY "Payment Method";'
df_result_12 = pd.read_sql_query(query_12, conn)
query_13 = 'SELECT "Customer Type", "Payment Method", COUNT(*) AS Total_Transactions FROM Supermarket_sales GROUP BY "Customer Type", "Payment Method" ORDER BY "Customer Type", Total_Transactions DESC;'
df_result_13 = pd.read_sql_query(query_13, conn)

#Print Result
print(df_result)
print(df_result_1)
print(df_result_2)
print(df_result_3)
print(df_result_4)
print(df_result_5)
print(df_result_6)
print(df_result_7)
print(df_result_8)
print(df_result_9)
print(df_result_10)
print(df_result_11)
print(df_result_12)



conn.close()

#Data Visualization
#Total Sales by Branch
plt.figure(figsize=(10, 6))
sns.barplot(x='Branch', y='TOTAL_SALES', data=df_result)
plt.title('Total Sales by Branch')
plt.xlabel('Branch')
plt.ylabel('Total Sales')
plt.show()

#Customer Type Distribution
plt.figure(figsize=(8, 8))
plt.pie(df_result_2['TOTAL'], labels=df_result_2['Customer Type'], autopct='%1.1f%%', startangle=140)
plt.title('Customer Type Distribution')
plt.axis('equal')
plt.show()

#Total Income by Branch
plt.figure(figsize=(10, 6))
sns.barplot(x='Branch', y='TOTAL_INCOME', data=df_result_1)
plt.title('Total Income by Branch')
plt.xlabel('Branch')
plt.ylabel('Total Income')
plt.show()

#Customer Type by Total Income
plt.figure(figsize=(10, 6))
sns.barplot(x='Customer Type', y='TOTAL_INCOME', data=df_result_3)
plt.title('Total Income by Customer Type')
plt.xlabel('Customer Type')
plt.ylabel('Total Income')
plt.show()

#Average Rating by Customer Type
plt.figure(figsize=(10, 6))
sns.barplot(x='Customer Type', y='AVG_RATINGS', data=df_result_4)
plt.title('Average Rating by Customer Type')
plt.xlabel('Customer Type')
plt.ylabel('Average Rating')
plt.show()

#Gender Distribution
plt.figure(figsize=(8, 8))
sns.pie(df_result_5['TOTAL'], labels=df_result_5['Customer Type'], autopct='%1.1f%%', startangle=140)
plt.title('Gender Distribution')
plt.axis('equal')
plt.show()

