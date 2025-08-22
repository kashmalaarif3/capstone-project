"Example API calls:

1. CHURN PREDICTION:
POST /predict

  "model_type": "sales",
    "features": {
    "price": 49.99,
    "quantity": 2,
    "age": 35,
    "tenure_months": 18,

    "category_encoded": 3,
    "region_encoded": 1,
    "gender_encoded": 0,

    "year": 2024,
    "month": 5,
    "quarter": 2,
    "day_of_week": 2,
    "day_of_month": 14,
    "is_weekend": 0,
    "is_month_end": 0,
    "is_month_start": 0,
    "is_holiday_season": 0,
    "is_summer": 0,
    "is_spring": 1,

    "customer_total_purchases": 12,
    "customer_avg_quantity": 1.6,
    "customer_total_spent": 720.0,
    "customer_avg_spent": 60.0,

    "product_popularity": 350,
    "product_avg_price": 52.0,
    "product_total_sales": 18200.0,

    "region_avg_sales": 58.5,
    "region_total_sales": 150000.0,

    "price_vs_avg": 0.96,
    "discount_indicator": 1,

    "segment_avg_sales": 62.4,

    "customer_rolling_avg_3": 57.8,
    "customer_rolling_avg_7": 60.3
  }
}
  
