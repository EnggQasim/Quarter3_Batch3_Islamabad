from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    students = [
        {'id':1,'name':'Asif'},
        {'id':2, 'course':'A.I'},
        {'id':3, 'name':"Hamza", 'Age':20}
    ]
    return jsonify({"piaic_students":students})

app.run(debug=True)    