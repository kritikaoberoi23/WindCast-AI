import joblib
import pandas as pd

# ==========================================================
# LOAD TRAINED MODELS
# ==========================================================

speed_model = joblib.load("models/wind_speed_model.pkl")
direction_model = joblib.load("models/wind_direction_model.pkl")
feature_columns = joblib.load("models/feature_columns.pkl")


# ==========================================================
# GET SEASON
# ==========================================================

def get_season(month):

    if month in [12, 1, 2]:
        return "Winter"

    elif month in [3, 4, 5]:
        return "Spring"

    elif month in [6, 7, 8]:
        return "Summer"

    else:
        return "Autumn"


# ==========================================================
# WIND PREDICTION
# ==========================================================

def predict_wind(
    pressure,
    latitude,
    longitude,
    geopotential,
    temperature,
    humidity,
    selected_date,
    hour
):

    year = selected_date.year
    month = selected_date.month
    day = selected_date.day

    season = get_season(month)

    data = pd.DataFrame({

        "pressure_hpa":[pressure],
        "latitude":[latitude],
        "longitude":[longitude],
        "geopotential_height":[geopotential],
        "temperature":[temperature],
        "relative_humidity":[humidity],
        "year":[year],
        "month":[month],
        "day":[day],
        "hour":[hour],
        "season":[season]

    })

    # ---------------------------------------------
    # One Hot Encoding
    # ---------------------------------------------

    data = pd.get_dummies(
        data,
        columns=["season"]
    )

    # ---------------------------------------------
    # Add Missing Columns
    # ---------------------------------------------

    for col in feature_columns:

        if col not in data.columns:

            data[col] = 0

    # ---------------------------------------------
    # Keep Same Feature Order
    # ---------------------------------------------

    data = data[feature_columns]

    # ---------------------------------------------
    # Predictions
    # ---------------------------------------------

    speed = speed_model.predict(data)[0]

    direction = direction_model.predict(data)[0]

    confidence = (
        direction_model
        .predict_proba(data)
        .max()
        * 100
    )

    return (

        round(float(speed),2),

        direction,

        round(float(confidence),2)

    )


# ==========================================================
# FEATURE IMPORTANCE
# ==========================================================

def get_feature_importance():

    importance = pd.DataFrame({

        "Feature":feature_columns,

        "Importance":speed_model.feature_importances_

    })

    importance = importance.sort_values(

        by="Importance",

        ascending=True

    )

    return importance