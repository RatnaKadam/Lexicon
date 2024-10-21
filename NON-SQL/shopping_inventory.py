from pymongo import MongoClient

client = MongoClient("localhost", 27017)

#reate the database
db = client["ecommerce_store"]                                              

#Collections
product_collection = db["Products"]
order_collection = db["Product_Order"]
customer_collection = db["Customer_information"]
categories_collection = db["Categories"]
purchase_history_collection = db["Purchase_History"]

customer_data_list = [
    {"name": "Sheldon", "address": "New street, New York"},
    {"name": "Amy", "address": "Old street, California"},
    {"name": "Leonard", "address": "New way, Arizona"},
    {"name": "Penny", "address": "Half way, Ohio"},
    {"name": "Raj", "address": "No way, Los Angeles"}
]
#customer_collection.insert_many(customer_data_list) 

#Category Collection
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

#Products Collection
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

#Order Collection
order_data_list = [
    {"customer_ID": "001", "products_purchased": ["Cellphone", "Jeans"], "total_amount": 5250, "order_status": "shipped"},
    {"customer_ID": "002", "products_purchased": ["Laptop", "Dress"], "total_amount": 10150, "order_status": "delivered"},
    {"customer_ID": "003", "products_purchased": ["Digital Watch", "Jackets", "Serums"], "total_amount": 2150, "order_status": "packed"},
    {"customer_ID": "004", "products_purchased": ["Dress", "Serums"], "total_amount": 200, "order_status": "packed"}
]
#order_collection.insert_many(order_data_list)
