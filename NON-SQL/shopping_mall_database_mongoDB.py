from pymongo import MongoClient
import random
import shopping_inventory


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

client = MongoClient("localhost", 27017)

#reate the database
db = client["ecommerce_store"]     

product_collection = db["Products"]
order_collection = db["Product_Order"]
customer_collection = db["Customer_information"]
categories_collection = db["Categories"]
purchase_history_collection = db["Purchase_History"]


# Class definitions
class Customer:
    def __init__(self, name):
        self.name = name
        customer_data = customer_collection.find_one({"name": self.name})
        if customer_data:
            self.order_history = customer_data.get("order_history", [])
        else:
            self.order_history = []

    def place_order(self, order_id, total_bill, products_purchased):
        # Update order history in Customer collection
        self.order_history.append(order_id)
        customer_collection.update_one({"name": self.name}, {"$set": {"order_history": self.order_history}})
        
        # Add purchase history to the new collection
        purchase_history_collection.insert_one({
            "customer_name": self.name,
            "order_id": order_id,
            "products_purchased": products_purchased,
            "total_bill": total_bill
        })
        print(f"Purchase history updated for {self.name}. Order ID: {order_id}.")

class Product:
    def __init__(self, name):
        product_data = product_collection.find_one({"name": name})
        if product_data:
            self.name = product_data["name"]
            self.price = product_data["price"]
            self.category = product_data["category"]
            self.stock_quantity = product_data["stock_quantity"]
            self.reviews = product_data["customer_review"]
        else:
            self.name = None

    def update_stock(self, quantity):
        if self.stock_quantity is not None:
            self.stock_quantity -= quantity
            product_collection.update_one({"name": self.name}, {"$set": {"stock_quantity": self.stock_quantity}})

class Order:
    def __init__(self, customer_name, products, total_amount):
        self.customer_name = customer_name
        self.products = products
        self.total_amount = total_amount
        self.status = "pending"
    
    def save_order(self):
        order_id = f"AXY-0{random.randint(10, 100)}"
        order_collection.insert_one({
            "customer_ID": self.customer_name,
            "products_purchased": self.products,
            "total_amount": self.total_amount,
            "order_status": self.status
        })
        print(f"Order saved! Order ID: {order_id}")
        return order_id

class Shop:
    def __init__(self):
        self.total_bill = 0
        self.items_purchased = []

    def list_products(self):
        products = product_collection.find()
        print("Products        : Price")
        print("----------------------------")
        for product in products:
            print(f"{product['name']}       : {product['price']}")

    def add_to_cart(self, product_name):
        product_name = product_name.title()  # Capitalize user input to match product names
        product = Product(product_name)
        if product.name and product.stock_quantity > 0:
            self.total_bill += product.price
            self.items_purchased.append(product_name)
            product.update_stock(1)  # Decrease stock by 1
            print(f"Added {product_name} to cart. Price: {product.price}")
        else:
            print(f"Sorry, {product_name} is out of stock or not available.")

    def view_cart(self):
        print(f"Current cart items: {self.items_purchased}")
        print(f"Total cart value: {self.total_bill}")

    def checkout(self, customer):
        if self.items_purchased:
            order = Order(customer_name=customer.name, products=self.items_purchased, total_amount=self.total_bill)
            order_id = order.save_order()
            customer.place_order(order_id, self.total_bill, self.items_purchased)
            print(f"Final bill: {self.total_bill}")
        else:
            print("No items in cart to checkout.")

# Simulated customer shopping session
def shopping_session():
    shop = Shop()
    customer_name = input("Enter your name: ").title()  # Capitalize customer name
    customer = Customer(customer_name)

    shopping = True
    while shopping:
        try:
            user_input = int(input("""
            Press 1: To see the products list, availability, and prices
            Press 2: Add a product to the cart
            Press 3: View cart and total amount
            Press 4: Place the order and exit\n"""))
            
            if user_input == 1:
                shop.list_products()

            elif user_input == 2:
                product_name = input("What do you want to purchase?\n").title()  # Capitalize product name
                shop.add_to_cart(product_name)

            elif user_input == 3:
                shop.view_cart()

            elif user_input == 4:
                shop.checkout(customer)
                print("Thank you for shopping!")
                shopping = False

            else:
                print("Invalid option. Please select a valid one.")

        except ValueError:
            print("Please enter a valid number.")

# Start the shopping session
shopping_session()
