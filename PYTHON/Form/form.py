from flask import Flask,jsonify,request,render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get data
        name = request.form['name']
        email = request.form['email']

        # Redirect to display page with the submitted data
        return render_template('display.html', name=name, email=email)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug = True)