from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return " Hello world \
        We Love our Country \
        We are pakistani \
    "

@app.route("/about")
def about():
    return """ 
    <h1>PIAIC Islamabad Quarter3</h1>
    we are providing latest art of the technology.
    """

app.run(debug=True)    