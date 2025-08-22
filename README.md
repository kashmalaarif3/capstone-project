"Example API calls:

1. CHURN PREDICTION:
POST /predict/churn
{
    "age": 35,
    "gender": 1,
    "segment": 2, 
    "tenure_months": 24,
    "total_spend": 1500.0,
    "purchase_frequency": 8,
    "recency_days": 30,
    "customer_value_score": 0.75
}

Response:
{
    "prediction": 0,
    "churn_probability": 0.23,
    "no_churn_probability": 0.77,
    "risk_level": "LOW",
    "model_used": "RandomForestClassifier"
}

2. CUSTOMER CLUSTERING:
POST /predict/cluster
{
    "purchase_frequency": 10,
    "total_spend": 2000.0,
    "avg_price": 50.0,
    "unique_products": 5,
    "recency_days": 15,
    "age": 40,
    "tenure_months": 36
}

Response:
{
    "cluster": 2,
    "confidence": 0.85,
    "cluster_distances": [2.1, 1.8, 0.3, 3.2],
    "model_used": "KMeans"
}

3. SALES PREDICTION:
POST /predict/sales
{
    "price": 45.99,
    "quantity": 2,
    "age": 35,
    "category_encoded": 1,
    "region_encoded": 0,
    "month": 12,
    "is_holiday_season": 1,
    "customer_total_purchases": 15,
    "product_popularity": 100
}

Response:
{
    "predicted_sales": 156.78,
    "prediction_interval_lower": 142.33,
    "prediction_interval_upper": 171.23,
    "prediction_std": 7.45,
    "model_used": "RandomForestRegressor"
}

4. GENERAL PREDICTION:
POST /predict
{
    "model_type": "churn",
    "features": {
        "age": 35,
        "total_spend": 1500.0,
        ...
    }
}

5. MODEL INFO:
GET /model/info

Response:
{
    "churn_model": {
        "loaded": true,
        "type": "RandomForestClassifier",
        "features": 20
    },
    "cluster_model": {
        "loaded": true,
        "type": "KMeans", 
        "features": 15
    },
    "sales_model": {
        "loaded": true,
        "type": "RandomForestRegressor",
        "features": 25
    }
}"