from flask import Flask
import os
from flask import render_template

app = Flask(__name__)



@app.route("/")
def rootfun():
    return "Flask inside Docker demo"

@app.route("/secret")
def secret():
    return "WTH you doing here. Get the H out"

@app.route("/bye")
def bye():
    return "OK, not sure why you were here anyway"

@app.route("/hello")
def hello():
    return "oh, hi. don\'t stay too long"

@app.route('/eg1')
def template():
    return render_template('eg1.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
