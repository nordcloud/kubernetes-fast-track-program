# This simple Python web application uses Flask to
# serve the message: "Hello, Docker!" on default
# Flask port 5000. 

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, Docker!'
