# 1st question:--
'''Lambda function:-- It is a small function and it can take any number of arguments, but can only have one expression.
Lambda function is used when you need a short function for a short time or as an argument for functions like map(),filter(),sorted(),etc.
These functions are directly defined at the place where they are supposed to be called. So no prior def function needed.
syntax:- lambda arguments:expression
Anonymous function:--Anonymous function means a function without  any name. Lambda functions are called as Anonymous functions and they are used where function name is required.
Inline Function:- Lambda functions are inline because they can be written directly in the place where they are used, often as arguments to higher-order functions.
They are used to make the code more concise.'''

#----------------------------------------

# 2nd question:--
''' Filter function:-- It is a built-in function that filters elements from an iterable (like a list) based on whether they meet a condition specified by a function.
It takes two arguments: a function and an iterable. The function should return *True* or *False* for each element, and filter() returns only those elements where the function returns True.
Syntax:- filter(function,iterator)
Result: It returns a filter object (an iterator) and it can be converted to a list, tuple, or other iterables.'''

given_list = [1,2,3,4,5,6,7,8,9,10]
answer_list = list(filter(lambda x : x % 2 == 0, given_list))
print(answer_list)

#----------------------------------------

#3rd question:--
#Learn how to use map() to apply a transformation to every item in a list.
# Task:
# Explain the purpose of map() and how it works in Python.
# Create a real-life scenario where you need to modify every element of a list in the same way.
# For example, you have a list of prices, and you want to apply a 10% discount to each. How would you use map () with a lambda function to achieve this?
''' Map function :-- map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
Syntax:- map(function,itereator)
The output of map() function is an object so we need to convert it into list or tuple so as to get a readable form.
'''
price_list = [299,358,591,647,789]
after_discount_price = list(map(lambda x : x - x*0.1, price_list))
print(after_discount_price)

#----------------------------------------

#4th question:-- Learn how to combine the functionality of  filter() and map() to both select and modify elements in a list.
#Task:
# Describe a scenario where you need to filter out unwanted elements from a list and then modify the remaining elements.
# For example, you might first filter a list to keep only positive numbers, and then square those numbers.
# Break down the process of applying filter () first, and then using map() on the filtered result.
''' Filter function takes a function and iterable as input. It applies the condition on each element of iterable and if the condition is fulllfilled, function return True or ealse returns False.
Filter() will then filter out elements that returns True. So we can apply this filter function and get a filtered list first.Then apply map() function on the filtered list.
Map() function, does the mapping of given function with each element of itereable and creats a map object which can further be converted into list ot tuples etc.
'''
given_list = [10,-34,25,-94,84,-463]
filtered_list = list(filter(lambda x: x > 0,given_list))
print(filtered_list) 
mapped_list = list(map(lambda x : x*x, filtered_list))
print(mapped_list)

#----------------------------------------

#5th question:--
#LEGB functions:- 
'''
1. Local: Variables defined within the current function. These variables are only accessible within the function where they are declared.
2. Enclosing: In the case of nested functions, the enclosing scope refers to the function within which another function is defined. 
Variables defined in this outer function are accessible to inner functions.
3. Global: Variables defined at the top level of a script or module, outside of any function. These variables are accessible throughout the entire program.
4. Built-in: This refers to the built-in namespace that contains Python’s built-in functions and constants (like print(), len(), etc.). These are always available.'''

#Explanation:--
''' 
LEGB scope resolves the precedence of varaibles with same name.(local → enclosing → global → built-in)
Explanation of Variable Scoping:
1. Variable defined inside a function (Local Scope):
When a variable is defined inside a function, it is local to that function. Python looks for variables in the local scope first. 
If the variable is not found, it checks the enclosing, global, and built-in scopes in that order.

2. Variable inside a function within another function (Enclosing Scope):
If a function is defined inside another function, the enclosing scope is the scope of the outer function. 
If Python can't find the variable in the local scope of the inner function, it checks the enclosing (outer) function's scope.

3. Variable in the main body of the program (Global Scope):
A variable defined in the main body of a Python program (outside all functions) is in the global scope. It can be accessed throughout the program unless overridden by a local definition within a function.

4. Built-in Functions (Built-in Scope):
The built-in scope contains Python’s predefined functions (e.g., len(), print(), range()). Python checks this last when trying to resolve a variable name.

If a variable is found in the nearest scope, Python uses that value and ignores the same variable name in outer scopes.
'''
#Example:--
x = 10 # global scope
def outer_func():
    x = 20 # enclosing scope
    print(f"it's a enclosing scope of x : {x}")
    def inner_func():
        x = 30 #local scope
        print(f"it's a local scope of x : {x}")
    inner_func()

outer_func()
print(f"it's a global scope of x : {x}")