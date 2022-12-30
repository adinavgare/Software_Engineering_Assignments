from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def greet():
    # Get the current date and the user's birthday from the query string
    name = request.args.get('name')
    current_date = request.args.get('date')
    birthday = request.args.get('birthday')
    
    # Convert the dates to datetime objects
    current_date = datetime.strptime(current_date, '%Y-%m-%d')
    birthday = datetime.strptime(birthday, '%Y-%m-%d')
    
    # Check if it is the user's birthday
    if current_date.month == birthday.month and current_date.day == birthday.day:
        return '<h1>Happy Birthday {name}!</h1>'
    else:
        return "<h1>This is a simple Web-Server</h1>"
    

if __name__ == "__main__":
    app.run(debug=True)

