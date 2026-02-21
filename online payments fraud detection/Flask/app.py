from flask import Flask, render_template, request
import pandas as pd
import pickle
import math

app = Flask(__name__)

# Load model
with open("models/random_forest_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load label encoder
with open("models/label_encoder.pkl", "rb") as f:
    le = pickle.load(f)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict-page")
def predict_page():
    return render_template("predict.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        step = float(request.form["step"])
        transaction_type = request.form["type"]
        amount = float(request.form["amount"])
        oldbalanceOrg = float(request.form["oldbalanceOrg"])
        newbalanceOrig = float(request.form["newbalanceOrig"])
        oldbalanceDest = float(request.form["oldbalanceDest"])
        newbalanceDest = float(request.form["newbalanceDest"])

        # log transform amount
        if amount > 0:
            amount = math.log(amount)
        else:
            amount = 0

        # encode type
        transaction_type_encoded = le.transform([transaction_type])[0]

        # IMPORTANT: include isFlaggedFraud (model expects it)
        input_data = pd.DataFrame([{
            "step": step,
            "type": transaction_type_encoded,
            "amount": amount,
            "oldbalanceOrg": oldbalanceOrg,
            "newbalanceOrig": newbalanceOrig,
            "oldbalanceDest": oldbalanceDest,
            "newbalanceDest": newbalanceDest,
            "isFlaggedFraud": 0
        }])

        prediction = model.predict(input_data)[0]
        prob = model.predict_proba(input_data)[0][1]

        if prediction == 1:
            result = "FRAUD Transaction 🚨"
            color = "danger"
        else:
            result = "SAFE Transaction ✅"
            color = "safe"

        return render_template(
            "result.html",
            result=result,
            probability=round(prob * 100, 2),
            color=color
        )

    except Exception as e:
        return f"Error occurred: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)

