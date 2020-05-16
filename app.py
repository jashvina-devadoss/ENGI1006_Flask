##############################################################################
# Name: Jashvina Devadoss
# UNI: jd3654
#
#
#
##############################################################################

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/hw1a")
def hw1a():
    return render_template('hw1a.html')

@app.route("/hw1b")
def hw1b():
    return render_template('hw1b.html')

@app.route("/hw2a")
def hw2a():
    return render_template('hw2a.html')

@app.route("/hw2b")
def hw2b():
    return render_template('hw2b.html')

#start the server
if __name__ == "__main__":
    app.run()