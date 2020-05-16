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

@app.route("/ENGI1006")
def ENGI1006():
    return 'ENGI1006 Assignments'

@app.route("/courses")
def courses():
    return 'RCES'

#start the server
if __name__ == "__main__":
    app.run()