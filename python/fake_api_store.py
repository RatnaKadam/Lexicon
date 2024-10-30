import requests

# get data from fakeapi
url = 'https://fakestoreapi.com/products'

response = requests.get(url)

print("""
_______    ___       __  ___  _______           ___      .______    __            _______.___________.  ______   .______       _______ 
|   ____|  /   \     |  |/  / |   ____|         /   \     |   _  \  |  |          /       |           | /  __  \  |   _  \     |   ____|
|  |__    /  ^  \    |  '  /  |  |__    ______ /  ^  \    |  |_)  | |  |  ______ |   (----`---|  |----`|  |  |  | |  |_)  |    |  |__   
|   __|  /  /_\  \   |    <   |   __|  |______/  /_\  \   |   ___/  |  | |______| \   \       |  |     |  |  |  | |      /     |   __|  
|  |    /  _____  \  |  .  \  |  |____       /  _____  \  |  |      |  |      .----)   |      |  |     |  `--'  | |  |\  \----.|  |____ 
|__|   /__/     \__\ |__|\__\ |_______|     /__/     \__\ | _|      |__|      |_______/       |__|      \______/  | _| `._____||_______|
""")


def view_all_products():
    response = requests.get(url)
    products = response.json()
    for every_product in products:
        print(f"ID: {every_product['id']}, Title: {every_product['title']}, Price: {every_product['price']},"
        "Description: {every_product['description']}, Category:{every_product['category']}, Image: {every_product['image']}\n")

def view_perticular_product():
    product_id_num = int(input("Enter a number as the product id number from 1-20  "))
    if product_id_num in range(1,21): 
        response = requests.get(f"https://fakestoreapi.com/products/{product_id_num}")
        particular_product = response.json()
        product_id_num in range(1,21)
        print(f"ID: {particular_product['id']}, Title: {particular_product['title']}, Price: {particular_product['price']},"
        "Description: {particular_product['description']}, Category:{particular_product['category']}, Image: {particular_product['image']}\n")
        print("\n")

def update_product_list():
    print("Adding a new product...")
    product_name = input("Product name: ")
    product_price = int(input("Product price: "))
    product_description = input("product_description: ")
    product_category = input("product_category: ")
    new_product = {
            "title" : product_name,
            "price" : product_price,
            "description" : product_description,
            "category" : product_category,
            "image": "image: 'https://i.pravatar.cc"
        } 
    response = requests.post(url,json=new_product)
    result = response.json()
    print(f"Product added successfully: {result}")

if __name__ == "__main__":
    game_on = True
    while game_on:
        user_choice = int(input("Menu: \n 1. Show all products\n 2. Show a pertucular product\n 3. Add a new product \n 4. Exit \n"))
        if user_choice == 1:
            view_all_products()

        elif user_choice == 2:
            view_perticular_product()

        elif user_choice == 3:
            update_product_list()
        
        elif user_choice == 4:
            print("Exiting the program...")
            game_on = False
        
        else:
            print("Invalid choice.")
