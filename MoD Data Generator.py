from faker import Faker
import pandas as pd
import random

# Initialize Faker
fake = Faker()

# Constants
num_customers = 1000
num_products = 15
num_sales = 10000
max_orders_per_sale = 5  # Maximum number of orders per sale

# Generate Customer Dimension Data
customers = []
country_to_continent = {
    "India": "Asia",
    "United Arab Emirates": "Asia",
    "Korea": "Asia",
    "Saudi Arabia": "Asia",
    "China": "Asia",
    "Japan": "Asia",
    "United States of America": "North America",
    "Egypt": "Africa",
    "Turkey": "Asia",  # Transcontinental, but primarily in Asia
    "Sri Lanka": "Asia",
    "Ireland": "Europe",
    "Greenland": "North America",  # Geographically part of North America
    "Poland": "Europe",
    "Germany": "Europe",
    "New Zealand": "Oceania",
    "Spain": "Europe",
    "Canada": "North America",
    "Italy": "Europe",
    "Portugal": "Europe",
    "France": "Europe",
    "Mexico": "North America",
    "Brazil": "South America",
    "Argentina": "South America",
    "Australia": "Oceania",
    "South Africa": "Africa",
    "Malaysia": "Asia",
    "Belgium": "Europe",
    "Qatar": "Asia",
    "Switzerland": "Europe",
    "Austria": "Europe",
    "Denmark": "Europe",
    "Hong Kong": "Asia"
}
for customer_id in range(1, num_customers + 1):
    country = random.choice(["India", "United Arab Emirates", "Korea", "Saudi Arabia", "China",
                             "Japan", "United States of America", "Hong Kong",
                             "Egypt", "Turkey", "Sri Lanka", "Ireland", "Greenland",
                             "Poland", "Germany", "New Zealand", "Spain", "Canada",
                             "Italy", "Portugal", "France", "Mexico", "Brazil",
                             "Argentina", "Australia", "South Africa", "Malaysia",
                             "Belgium","Qatar", "Switzerland", "Austria", "Denmark"])
    customers.append({
        "CustomerID": "C"+str("{:05d}".format(customer_id)),
        "CustomerName": fake.name(),
        "EmailAddress": fake.email(),
        "Country": country,
        "Region": country_to_continent[country]  # Adding region
    })

customer_df = pd.DataFrame(customers)

# Generate Product Dimension Data with Subcategories
product_categories = {
    "Business Cards": ["Standard", "Premium", "Eco-Friendly"],
    "Apparel": ["T-Shirts", "Hoodies", "Caps"],
    "Signage": ["Banners", "Yard Signs", "Window Clings"],
    "Gifts": ["Mugs", "Calendars", "Stickers"],
    "Packaging": ["Boxes", "Bubble Mailers", "Envelopes"]
}

products = []
product_id = 1
for category in product_categories:
    for subcategory in product_categories[category]:
        product_cost = round(random.uniform(10, 500), 2)  # Random base price between $10 and $500
        
        products.append({
            "ProductID": product_id,
            "ProductName": f"{subcategory} {category}",
            "ProductCategory": category,
            "ProductSubcategory": subcategory,
            "UnitCost": product_cost
        })
        product_id+=1

product_df = pd.DataFrame(products)

# Generate Date Dimension Data
dates = []
start_date = pd.to_datetime("2020-01-01")
end_date = pd.to_datetime("2024-12-31")
date_range = pd.date_range(start=start_date, end=end_date)

for date in date_range:
    dates.append({
        "DateKey": date.strftime("%Y%m%d"),
        "Date": date.strftime("%Y-%m-%d"),
        "Month": date.strftime("%B"),
        "Quarter": f"Q{(date.month - 1) // 3 + 1}",
        "Year": date.year
    })

date_df = pd.DataFrame(dates)

# Generate Sales Fact Table Data with Multiple Orders per Sale
sales = []


for sales_id in range(10001, num_sales + 10000 +1):
    num_orders = random.randint(1, max_orders_per_sale)  # Random number of orders for this sale
    order_id_counter = 1
    # Select a random order date from the date dimension
    order_date_key = random.choice(date_df["DateKey"])
        
    # Calculate due date (up to 14 days from order date)
    order_date = pd.to_datetime(order_date_key)
    due_date = order_date + pd.Timedelta(days=random.randint(7, 14))
    C_ID = "C"+str("{:05d}".format(random.randint(1, num_customers)))
    
    for _ in range(num_orders):
        product_id = random.randint(1, num_products)
        quantity_sold = random.randint(1, 10)  # Random quantity between 1 and 10

        if order_date_key[:6] == "202401":
            product_id=product_id = random.choice([1,2,3,4,5,6,7,9,11,12,13,14,15])
        elif order_date_key[:6] == "202402":
            product_id=product_id = random.choice([1,2,3,4,5,6,7,10,12,13,14,15])
        elif order_date_key[:6] == "202403":
            product_id=product_id = random.choice([1,2,3,4,6,8,9,10,12,13,14,15])
        elif order_date_key[:6] == "202404":
            product_id=product_id = random.choice([1,2,3,4,6,9,10,12,13,14,15])
        elif order_date_key[:6] == "202405":
            product_id=product_id = random.choice([1,2,3,4,6,7,8,10,12,13,14,15])
        elif order_date_key[:6] == "202406":
            product_id=product_id = random.choice([1,2,3,4,7,8,9,12,13,14,15])
        elif order_date_key[:6] == "202407":
            product_id=product_id = random.choice([1,2,3,4,7,8,9,10,12,13,14,15])
        elif order_date_key[:6] == "202408":
            product_id=product_id = random.choice([1,2,3,4,5,6,7,8,9,10,12,13,14,15])
        elif order_date_key[:6] == "202409":
            product_id=product_id = random.choice([1,2,3,4,5,6,9,10,12,13,14])
        elif order_date_key[:6] == "202410":
            product_id=product_id = random.choice([1,2,3,4,5,6,7,8,9,12,13,14,15])
        elif order_date_key[:6] == "202411":
            product_id=product_id = random.choice([1,2,3,4,5,6,7,8,9,10,11,12,14,15])
        elif order_date_key[:6] == "202412":
            product_id=product_id = random.choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

        # Get the corresponding product price from product dimension
        product_price = product_df.loc[product_df['ProductID'] == product_id, 'UnitCost'].values[0]
        profit_margin = random.uniform(0.30, 0.60)
        product_price = round(product_price*(1+profit_margin),2)
        total_sales_amount = round(product_price * quantity_sold, 2)  # Calculate total sales amount based on quantity sold
        
        sales.append({
            "SalesID": "SO"+str("{:05d}".format(sales_id)),
            "OrderID": (sales_id*1000)+order_id_counter,
            "ProductID": product_id,
            "CustomerID": C_ID,
            "DateKey": order_date_key,
            "QuantitySold": quantity_sold,
            "UnitPrice": product_price,  # Add Product Price to Sales Fact Table
            "DueDate": due_date.strftime("%Y%m%d"),
            "TotalSalesAmount": total_sales_amount,  # Use the calculated total sales amount
            "ShippingCost": round(random.uniform(5, 50), 2)  # Random shipping cost between $5 and $50
            
        })
        
        order_id_counter += 1

sales_df = pd.DataFrame(sales)

# Save to CSV files
writer = pd.ExcelWriter('Cimpress.xlsx',engine='xlsxwriter')
customer_df.to_excel(writer, sheet_name = 'customer_dimension.csv', index=False)
product_df.to_excel(writer, sheet_name ='product_dimension.csv', index=False)
date_df.to_excel(writer, sheet_name ='date_dimension.csv', index=False)
sales_df.to_excel(writer, sheet_name ='sales_fact_table.csv', index=False)
writer.close()
print("Data generation complete! CSV files created.")
