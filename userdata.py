# Resources:
#1. https://flask.palletsprojects.com/en/stable/
import os
import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)

#gets database url
DATABASE_URL = os.environ.get('DATABASE_URL')

#connect to the database
connect = psycopg2.connect(DATABASE_URL, sslmode ='require')

# Route to display the login page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle login form submission
@app.route('/index', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    #add user data to the database
    with connect.cursor() as cur:
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        connect.commit()
    
    # Send a response back to the user
    return "Login data received."

#if __name__ == '__main__':
    #app.run(debug=True)

