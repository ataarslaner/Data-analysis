import matplotlib.pyplot as plt
import pandas as pd

# read csv
df = pd.read_excel("online_retail2.xlsx")

#Task1: “top 10” products ordered by individuals.
product_sale = df.groupby(['StockCode'])['Quantity'].sum().sort_values(ascending=False).head(10)
print('Top 10, most sold products: ')
print(product_sale)

#Task2: “top 10” customers who spent the most money.

df['TotalAmount'] = df['Quantity'].astype(int) * df['Price'].astype(float)
df.head(8)
Customer_price = df.groupby(['Customer ID'])['TotalAmount'].sum().sort_values(ascending=False).head(10)
print(' top 10 customers who spent the most money.')
print(Customer_price)

#Task3: 5 dates in which the greatest number of orders were placed.
df['InvoiceOnlyDate'] = df['InvoiceDate'].dt.date
top_dates = df.groupby(['InvoiceOnlyDate'])['Quantity'].sum().sort_values(ascending=False).head(5)
print('Top 5 dates with the most sales: ')
print(top_dates)

#Task4: Average number of orders placed on the days of the week.

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['day_of_week'] = df['InvoiceDate'].dt.dayofweek

days = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}

df['day_of_week'] = df['day_of_week'].apply(lambda x: days[x])

df.head(8)
numbers = df.groupby(['day_of_week']).size()
total = df.groupby(['day_of_week'])['Quantity'].sum()
average = total / numbers
print('Average number of orders placed on the days of the week.')
print(average)

#Task5: Most ordered product for a specific day given by user.

df['InvoiceOnlyDate'] = df['InvoiceDate'].dt.date

inputDate = input('Enter a date (DD.MM.YYYY): ')
splicedDate = inputDate.split(".")
day = int(splicedDate[0])
month = int(splicedDate[1])
year = int(splicedDate[2])
d = date(year, month, day)

dff = df.loc[df['InvoiceOnlyDate'] == d]

topSoldProduct = dff.groupby(['Description'])['Quantity'].sum().sort_values(ascending=False).head(1)

print('Most ordered product for a specific day given by user.')
print(topSoldProduct)

#VİSUALİZATİON PART.

#Country-Customer graph that shows you how many customer in each country.(without United Kingdom)

no_uk = df[df.Country != 'United Kingdom']

customer_country = no_uk.groupby(['Country'])['Customer ID'].size()
customer_country.plot(kind='bar')
plt.title('Country-Customer graph')
plt.xlabel('Countries')
plt.ylabel('Number of Customers')
plt.show()

#Country- Customer graph of United Kingdom

UK = df[df['Country'] == "United Kingdom"]

customer_UK = UK.groupby(['Country'])['Customer ID'].size()
customer_UK.plot(kind='bar')
plt.title('Country-Customer graph')
plt.ylabel('Number of Customers')
plt.show()

#TotalAmount-Date graph that shows you how much money spent on each day of the week

df['TotalAmount'] = df['Quantity'].astype(int) * df['Price'].astype(float)

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['day_of_week'] = df['InvoiceDate'].dt.dayofweek

days = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}

df['day_of_week'] = df['day_of_week'].apply(lambda x: days[x])

TotalAmount_Date = df.groupby(['day_of_week'])['TotalAmount'].sum()

plt.title('TotalAmount-Date graph')
plt.xlabel('Date')
plt.ylabel('TotalAmounts')
TotalAmount_Date.plot(kind='bar')
plt.show()

#Country-Quantity graph that shows you how many product sold in each country.(without UK)

no_uk = df[df.Country != 'United Kingdom']
Country_Quantity = no_uk.groupby(['Country'])['Quantity'].sum().sort_values(ascending=False)

plt.title('Country-Quantity graph')
plt.xlabel('Countries')
plt.ylabel('Quantities')
Country_Quantity.plot(kind= 'bar')
plt.show()

#Country-Quantity graph of United Kingdom

UK = df[df['Country'] == "United Kingdom"]
UK_Quantity = UK.groupby(['Country'])['Quantity'].sum()
plt.title('Country-Quantity graph')
plt.ylabel('Quantity')
UK_Quantity.plot(kind= 'bar')
plt.show()

#Customer-TotalAmount graph that shows you TotalAmount of each Customer.

df['TotalAmount'] = df['Quantity'].astype(int) * df['Price'].astype(float)
countries = df.groupby(['Customer ID'])['TotalAmount'].sum()

plt.figure(figsize=(50, 7.5))
plt.plot(countries)
plt.xlabel('Customer ID')
plt.ylabel('Total Sales')
plt.title('Total Sales by Each Costumer')
plt.legend()
plt.show()

#Date-Quantity graph that shows you how many products sold each day.
date_quant = df.groupby(['InvoiceOnlyDate'])['Quantity'].sum()
plt.figure(figsize=(50, 7.5))
plt.plot(date_quant)
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Total Products Sold Each Day')
plt.show()







