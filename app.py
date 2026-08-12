from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("crop_yield_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = {
        "Crop": [request.form["Crop"]],
        "Region": [request.form["Region"]],
        "Soil_Type": [request.form["Soil_Type"]],
        "Soil_pH": [float(request.form["Soil_pH"])],
        "Rainfall_mm": [float(request.form["Rainfall_mm"])],
        "Temperature_C": [float(request.form["Temperature_C"])],
        "Humidity_pct": [float(request.form["Humidity_pct"])],
        "Fertilizer_Used_kg": [float(request.form["Fertilizer_Used_kg"])],
        "Irrigation": [request.form["Irrigation"]],
        "Pesticides_Used_kg": [float(request.form["Pesticides_Used_kg"])],
        "Planting_Density": [float(request.form["Planting_Density"])],
        "Previous_Crop": [request.form["Previous_Crop"]]
    }

    input_data = pd.DataFrame(data)

    prediction = model.predict(input_data)[0]

    return render_template(
        "index.html",
        prediction=round(prediction, 2)
    )


if __name__ == "__main__":
    app.run(debug=True)
