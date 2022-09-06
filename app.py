# Import flask dependency to access all that Flask has to offer.
from flask import Flask

# Create a new Flask app instance.
app = Flask(__name__)

# Create our first route. This is the starting point called "root."
@app.route('/')

# Create a function.
def hello_world():
    return 'Hello world'


