from flask import Flask, request
from tensorflow import keras
import tensorflow as tf
import numpy as np
m = tf.keras.models.load_model('abc.h5')


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
        print(m.summary())
        print(request.form['height'])
        input1 = np.int64([[request.form['height']]])
        print("input",input1, type(input1))
        # a = m.predict([[200]])
        a = m.predict(input1)
        print("Prediction...",a)
        return "Data is showing with POST method {} Now prediction is: {}".format(input1,a)
app.run(debug=True)    