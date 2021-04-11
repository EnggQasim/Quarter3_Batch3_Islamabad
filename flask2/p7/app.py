from flask import Flask

app = Flask(__name__)

@app.route("/user/<name>")
def index(name):
    return "Hello Dear <b>" + name + " </b>on our Digital Web portal"

app.run(debug=True)    