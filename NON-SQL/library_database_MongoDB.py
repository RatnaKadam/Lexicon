# Set up the necessary collections to store the information for the library system.
 
# Books: Will store details about books in the library, including the title, genre, publication
# Authors: Will store information about authors, such as name, birthdate, and nationality.
# Users: Will store information about library users, including their name, email, and borrow history.
 
 
# Set up three collections: books, authors, and users.
# Define the structure (fields and data types) for each collection. For example, books might have a title, author, and published_year, while users will have a name, email, and borrowed books.
 
 
# And try Insert at least five records into each collection. You can also practice reading and updating book information, and then deleting some records from the database.
# You can also try out filtering and sorting on the books and users collection. e.g., find books by a certain author published after the year 2000.


from pymongo import MongoClient

# connecting to local host
client = MongoClient("localhost", 27017)

# creating databases Books,Author,Users
db = client["DigitalLibrary"]

# creating collection
book_collection = db["Books"]
author_collection = db["Authors"]
user_collection = db["Users"]

#Inserting one data into collection
book_data = { 
    "title": "The Final Empire",
    "author": "Brandon",
    "pages": 400,
    "genres": ["Comedy","Dystopian" ],
    "published_year":2004
    }
book_collection.insert_one(book_data)

author_data = {
    "name" : "Brandon",
    "birthdate" : "12/1/1989",
    "nationality" : "USA"
}

author_collection.insert_one(author_data)

#Inserting multiple data at the same time in Book Collection

book_data_list =  [
        {"title":"Name of the Wind","author": "Patrik", "pages": 600,"genres": ["Comedy","Fantasy" ],"published_year":1998},
        {"title":"The Way of King","author": "Bella", "pages": 350,"genres": ["Dystopian","Fantasy" ],"published_year":2007},
        {"title":"The Call of the Weird","author": "Louis", "pages": 450,"genres": ["Non-Fiction","Comedy" ],"published_year":2010},
        {"title":"The Magic","author": "EDward", "pages": 700,"genres": ["Magic","Fantasy" ],"published_year":2020}
    ]
book_collection.insert_many(book_data_list)

#Inserting multiple data at the same time in Author Collection
author_data_list = [
    {"name" : "Patrik","birthdate" : "27/4/1970","nationality" : "Ghana"},
    {"name" : "Bella","birthdate" : "31/9/1995","nationality" : "India"},
    {"name" : "Louis","birthdate" : "6/8/1998","nationality" : "Sweden"},
    {"name" : "EDward","birthdate" : "15/3/2000","nationality" : "England"}
]
author_collection.insert_many(author_data_list)

#Inserting multiple data at the same time in User Collection
user_data_list = [
    {"name" : "Lucy","Email_id" :"lucy@example.com" ,"Book_borrowed" : "yes"},
    {"name" : "Tim","Email_id" :"tim@library.com" ,"Book_borrowed" : "no"},
    {"name" : "John","Email_id" :"john@reader.com" ,"Book_borrowed" : "yes"},
    {"name" : "Angela","Email_id" :"angela@new.com" ,"Book_borrowed" : "no"},
    {"name" : "Nyala","Email_id" :"nyla@example.com" ,"Book_borrowed" : "yes"},
]

user_collection.insert_many(user_data_list)

#Reading data from database
book_data = book_collection.find_one()
print("Book Data --- \n")
print(book_data)

for x in author_collection.find():
    print(x)

#Updating data in databse
user_collection.update_one({"name":"Tim"},{"$set":{"Book_borrowed":"yes"}})

#filter ascending oreder,names of users
my_doc = user_collection.find().sort("name")

for x in my_doc:
    print(x)

print("\n")

#filter descending based on number of pages in book
page_list = book_collection.find().sort("pages",-1)
for a in page_list:
    print(a)
print("\n")

#filter useing less than and greater than
publish_list = book_collection.find({"published_year":{"$gt":2000, "$lt":2020}})

for b in publish_list:
    print(b)
print("\n")

#count documents
print(book_collection.count_documents({}))
print(user_collection.count_documents({"Book_borrowed":"yes"}))

#delete 
book_collection.delete_one({"title": "The Final Empire"})
user_collection.find_one_and_replace({"name" : "Nyala"},{"name" : "Talia"})
user_collection.find_one_and_replace({"name" : "Talia"},{"name" : "Nyala","Email_id" :"nyla@example.com" ,"Book_borrowed" : "yes"})