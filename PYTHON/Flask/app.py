#Create a Flask application with three routes:

from flask import Flask,jsonify

app = Flask(__name__)

#Route 1: Display a welcome message on the home page.
@app.route('/')
def home():
    return "<h1>Welcome to the Home Page!</h1>"

#Route 2: Display information about yourself on a separate page.
@app.route('/about_me')
def my_info():
    
    data = {
        "name" : "Ratna",
        "Occupation" : "Student @ Lexicon.."
    }
    return jsonify(data)


#Route 3: Create a custom 404 error page.
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 Error</h1><p>Sorry, the page you are looking for does not exist.</p>", 404



if __name__ == "__main__":
    app.run(debug = True)

