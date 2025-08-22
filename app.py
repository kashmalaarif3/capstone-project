from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)
with open("models/churn_model.pkl", "rb") as f:
    churn_model = pickle.load(f)
with open("models/kmeans_model.pkl", "rb") as f:
    kmeans_model = pickle.load(f)
with open("models/sales_prediction_model.pkl", "rb") as f:
    sales_prediction_model = pickle.load(f)
with open("models/sentiment_model.pkl", "rb") as f:
    sentiment_model = pickle.load(f)

@app.route("/")
def home():
    return jsonify({"message": "Customer Intelligence App is Running"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        model_type = data.get('model_type')
        feature = data.get('features')

        if not model_type or not feature: 
            return jsonify({"error": "model_type and features are required"}), 400
        
        data = np.array(feature).reshape(1, -1)

        if model_type == 'logreg':
            prediction = churn_model.predict(data)[0]
        elif model_type =='kmeans':
            prediction = kmeans_model.predict(data)[0]
        else:
            return jsonify({"error":"Invalid modle_type"}), 400
        
        return jsonify({
            'model_type':model_type,
            'features': feature,
            "predictions": int(prediction)
        })
    


    except Exception as e:
        return jsonify({"error":str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)