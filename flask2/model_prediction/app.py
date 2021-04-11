from flask import Flask, request
from tensorflow import keras
m = keras.models.load_model('../abc.h5')


app = Flask(__name__)

@app.route("/")
def index():
    return ''' 
    <h1>User Information</h1>
    <form action="/info" method="POST"> 
    <input type="text" name="height" placeholder="User Name">
    
    <input type="submit" value="Send">

    </form>
    '''


@app.route("/info", methods=["GET","POST"])
def info():
    if request.method == "GET":
       pass
    elif request.method == "POST":
        a = m.predict([[request.form['height']]])
        return "Data is showing with POST method {} Now prediction is: {}".format(request.form['height'],a)
app.run(debug=True)    