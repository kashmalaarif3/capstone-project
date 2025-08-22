"Example API calls:

1. SALE PREDICTION:
POST /predict

 {"model_type": "sales",
  "features": {
    "price": 59.99,
    "quantity": 2,
    "age": 35,
    "tenure_months": 18,

    "category_encoded": 3,
    "region_encoded": 1,
    "gender_encoded": 0,

    "year": 2024,
    "month": 8,
    "quarter": 3,
    "day_of_week": 2,
    "day_of_month": 15,
    "is_weekend": 0,
    "is_month_end": 0,
    "is_month_start": 0,
    "is_holiday_season": 0,
    "is_summer": 1,
    "is_spring": 0

  }
