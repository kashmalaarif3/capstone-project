"Example API calls:

Churn PREDICTION:
POST /predict
{
  "model_type": "churn",
  "features": {
    "age": 35,
    "gender": 1,
    "segment": 2,
    "tenure_months": 24,
    "num_purchases": 15,
    "total_spent": 1200.50,
    "avg_spent": 80.03,
    "std_spent": 15.2,
    "spend_per_month": 50.0,
    "spend_consistency": 0.18,
    "spend_range": 120.0,
    "age_group": 2,
    "age_tenure_ratio": 1.46,
    "purchases_per_month": 0.63,
    "high_spender": 1,
    "frequent_buyer": 0,
    "customer_value_score": 0.72,
    "age_spend_interaction": 2800.0,
    "tenure_spend_interaction": 1920.7,
    "segment_spend_interaction": 160.0
  }
}

Example Output:
{"model":"churn","prediction":1}
