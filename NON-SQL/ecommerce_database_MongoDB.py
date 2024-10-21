# You are going to create a system to manage the inventory of an online e-commerce store, with products, categories, orders, and customer data.
 
# Collections:
# -Name the database ecommerce store.
# -Store product details like name, price, category, stock quantity, and a list of customer reviews.
# -Store categories with attributes like category name, description, and a list of products in that category.
# -Store customer information like name, address, and their order history.
# -Store details of customer orders including customer ID, products purchased, total amount, and the status of the order (pending, shipped, etc.).
 
# Insert data:
# -Add product data with various categories (e.g., electronics, clothing, etc.).
# -Add customer data with initial information.
# -Insert some orders where customers have purchased multiple products.

#Database ----
from pymongo import MongoClient
import random

# Connect to MongoDB
client = MongoClient("localhost", 27017)

# Create the database
db = client["ecommerce_store"]

# Customer Collection
customer_collection = db["Customer_information"]
customer_data_list = [
    {"name": "Sheldon", "address": "New street, New York"},
    {"name": "Amy", "address": "Old street, California"},
    {"name": "Leonard", "address": "New way, Arizona"},
    {"name": "Penny", "address": "Half way, Ohio"},
    {"name": "Raj", "address": "No way, Los Angeles"}
]
#customer_collection.insert_many(customer_data_list)

# Category Collection
categories_collection = db["Categories"]
categories_data_list = [
    {
        "category_name": "Electronics", "category_description": "This category contains all the electronic items",
        "products": ["Cellphone", "Laptop", "Digital watch"]
    },
    {
        "category_name": "Clothing", "category_description": "This category contains all the clothing items",
        "products": ["Dress", "Jackets", "Jeans"]
    },
    {
        "category_name": "Cosmetics", "category_description": "This category contains all the cosmetic items",
        "products": ["Lipsticks", "Serums", "Moisturizer"]
    }
]
#categories_collection.insert_many(categories_data_list)

# Products Collection
product_collection = db["Products"]
product_data_list = [
    {"name": "Cellphone", "price": 5000, "category": "Electronics", "stock_quantity": 500,
     "customer_review": [{"review": "It's a very good product!!"}, {"review": "Good features"}, {"review": "Camera quality is nice!!!"}]},
    {"name": "Laptop", "price": 10000, "category": "Electronics", "stock_quantity": 250,
     "customer_review": [{"review": "It's an amazing product!!!"}, {"review": "I liked it!!!"}]},
    {"name": "Digital Watch", "price": 2000, "category": "Electronics", "stock_quantity": 150,
     "customer_review": [{"review": "It's a waterproof watch!!!"}, {"review": "It's a good health monitor!!!"}]},
    {"name": "Dress", "price": 150, "category": "Clothing", "stock_quantity": 10000,
     "customer_review": [{"review": "Dress quality is really good"}, {"review": "Fabulous...."}]},
    {"name": "Jackets", "price": 5000, "category": "Clothing", "stock_quantity": 2000,
     "customer_review": [{"review": "These Jackets are awesome..."}, {"review": "Jackets are beautiful."}]},
    {"name": "Jeans", "price": 250, "category": "Clothing", "stock_quantity": 30000,
     "customer_review": [{"review": "These jeans are a perfect fit.."}, {"review": "These jeans are comfy."}]},
    {"name": "Lipsticks", "price": 100, "category": "Cosmetics", "stock_quantity": 50000,
     "customer_review": [{"review": "Lipsticks are long lasting..."}, {"review": "Good quality product."}]},
    {"name": "Serums", "price": 50, "category": "Cosmetics", "stock_quantity": 700000,
     "customer_review": [{"review": "Serums helped my skin to glow."}, {"review": "Made my skin acne-free!!!"}, {"review": "Wow!! My skin is glowing now..."}]},
    {"name": "Moisturizer", "price": 300, "category": "Cosmetics", "stock_quantity": 890000,
     "customer_review": [{"review": "Provides hydration."}, {"review": "My skin is healthy now"}, {"review": "Rich in hydration..."}]}
]
#product_collection.insert_many(product_data_list)

# Order Collection
order_collection = db["Product_Order"]
order_data_list = [
    {"customer_ID": "001", "products_purchased": ["Cellphone", "Jeans"], "total_amount": 5250, "order_status": "shipped"},
    {"customer_ID": "002", "products_purchased": ["Laptop", "Dress"], "total_amount": 10150, "order_status": "delivered"},
    {"customer_ID": "003", "products_purchased": ["Digital Watch", "Jackets", "Serums"], "total_amount": 2150, "order_status": "packed"},
    {"customer_ID": "004", "products_purchased": ["Dress", "Serums"], "total_amount": 200, "order_status": "packed"}
]
#order_collection.insert_many(order_data_list)

#Python code for user interaction______________________________
ascii_art = """
 __        __   _                                _             ____  _                       _               __  __       _ _  
 \ \      / /__| | ___ ___  _ __ ___   ___      | |_ ___      / ___|| |__   ___  _ __  _ __ (_)_ __   __ _  |  \/  | __ _| | |
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \_____| __/ _ \ ____\___ \| '_ \ / _ \| '_ \| '_ \| | '_ \ / _` | | |\/| |/ _` | | |
   \ V  V /  __/ | (_| (_) | | | | | |  __/_____| || (_) |_____|__) | | | | (_) | |_) | |_) | | | | | (_| | | |  | | (_| | | |
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|      \__\___/     |____/|_| |_|\___/| .__/| .__/|_|_| |_|\__, | |_|  |_|\__,_|_|_|
                                                                                |_|   |_|            |___/                     
"""

# Print the ASCII art
print(ascii_art)


total_bill = 0
items_purchased = []
shopping = True
while shopping:
    user_input = int(input("""
    Press 1: To see the products list, availabllity and prices
    Press 2: Add a product to cart
    Press 3: To see list of products and cart amount
    Press 4: Place a order and exit \n"""))
    if user_input == 1:
        print("""
                Products        : Price
                -----------------------------
                Cellphone       : 5000
                Laptop          : 10000
                Digital watch   : 2000
                Dress           : 150
                Jackets         : 5000
                Jeans           : 250
                Lipsticks       : 100
                Serums          : 50
                Moisturizer     : 300
        """)

    elif user_input == 2: 
        shopping_going_on = True
        while shopping_going_on:
            user = input("What you want to purchase?\n").capitalize() 
            identify_product = product_collection.find()
            for a in identify_product:
                if a["name"] == user:
                    total_bill+=a["price"]
                    items_purchased.append(user)
                    product_collection.find_one_and_update({"name": user},{"$inc":{"stock_quantity":-1}})
                    print(f"Your product is {user} added into cart and it's price is {a["price"]}\n")
            still_on = input("Do you want to shop more? yes/no\n").lower()
            if still_on == "yes":
                continue
            else:
                shopping_going_on = False
                print(f"Your current cart consist of : {items_purchased} and cart amount is {total_bill}.")

    elif user_input == 3:
        print(f"Your current cart consist of : {str(items_purchased)} ")
        more_shopping = True
        while more_shopping:
            want_more = input("Do you want to shop more?yes/no\n")
            if want_more == "yes":
                user = input("What you want to purchase?\n").capitalize()
            elif want_more == "no":
                more_shopping = False
                break
   
    elif user_input == 4:
        print(f"Your Final order is : {str(items_purchased)} and your total bill is {total_bill}")
        shopping = False
        print("Order placed Successfully!!!!")
        print(f"Your order ID is AXY-0{random.randint(10,100)}.")
        break

    else:
        print("Invalid option. Select a valid")


    





