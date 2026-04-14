from flask import Flask, request, render_template
import numpy as np
from sklearn.linear_model import LogisticRegression
import pandas as pd

app = Flask(__name__)

def prediction(val):
    val = np.array(val).reshape(1, -1)
    return model.predict(val)

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        age = float(request.form["age"])
        bp = float(request.form["blood_pressure"])
        if age < 0 or age > 120:
            return render_template("index.html", error="ageinv")
        if bp < 50 or bp > 300:
            return render_template("index.html", error="bpinv")
        
        data = prediction(np.array([[age, bp]]))
        if data[0] == 1:
            p = "yes"
        else:
            p = "no"
        return render_template("index.html", prediction=p)
    return render_template("index.html")

def train_model():
    file = pd.read_csv("prediction/data.csv")
    file.fillna(file.mean(), inplace=True)
    global model
    model = LogisticRegression(class_weight="balanced")
    x = np.array(file[["age", "blood_pressure"]])
    y = np.array(file["result"])
    model.fit(x, y)

if(__name__ == "__main__"):
    train_model()
    app.run(debug=True)