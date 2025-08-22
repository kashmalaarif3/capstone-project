from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# -------- Load Models --------
with open("models/churn_model.pkl", "rb") as f:
    churn_model = pickle.load(f)

with open("models/kmeans_model.pkl", "rb") as f:
    kmeans_model = pickle.load(f)

with open("models/sales_prediction_model.pkl", "rb") as f:
    sales_model = pickle.load(f)   # This might be a dict (see note below)

with open("models/sentiment_model.pkl", "rb") as f:
    sentiment_model = pickle.load(f)


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API is running"})


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    model_type = data.get("model_type")
    features = data.get("features")
    text = data.get("text")

    if model_type == "churn":
        X = pd.DataFrame([features])
        pred = int(churn_model.predict(X)[0])
        return jsonify({"model": "churn", "prediction": pred})

    elif model_type == "kmeans":
        X = pd.DataFrame([features])
        cluster = int(kmeans_model.predict(X)[0])
        return jsonify({"model": "kmeans", "cluster": cluster})

    elif model_type == "sales":
        # if saved as dict, get model out of bundle
        if isinstance(sales_model, dict):
            model = sales_model["model"]
            scaler = sales_model["scaler"]
            feature_names = sales_model["feature_names"]

            X = pd.DataFrame([features], columns=feature_names)
            X_scaled = scaler.transform(X)
            pred = float(model.predict(X_scaled)[0])
        else:
            X = pd.DataFrame([features])
            pred = float(sales_model.predict(X)[0])

        return jsonify({"model": "sales", "prediction": pred})

    elif model_type == "sentiment":
        result = sentiment_model.predict(text)
        return jsonify({"model": "sentiment", "result": result})

    else:
        return jsonify({"error": "Invalid model_type"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)