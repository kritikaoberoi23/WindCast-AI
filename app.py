import streamlit as st
import plotly.express as px
from datetime import date

from utils import (
    predict_wind,
    get_feature_importance
)

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="WindCast AI",
    page_icon="🌪️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================================
# LOAD CSS
# ==========================================================

with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ==========================================================
# HEADER
# ==========================================================

st.title("🌪 WindCast AI")

st.markdown("""
### AI Powered Wind Speed & Direction Prediction

Predict wind speed and wind direction using atmospheric
parameters extracted from the IMDAA 3-hourly weather dataset
provided by NCMRWF.
""")

st.divider()

# ==========================================================
# DEFAULT VALUES
# ==========================================================

speed = "-- m/s"
direction = "--"
confidence = "-- %"

# ==========================================================
# MAIN LAYOUT
# ==========================================================

left, right = st.columns([1.25, 1], gap="large")

# ==========================================================
# INPUT PANEL
# ==========================================================

with left:

    st.subheader("🌤 Atmospheric Inputs")

    pressure = st.selectbox(
        "Pressure Level (hPa)",
        [50, 70, 100, 150, 200],
        index=2
    )

    geopotential = st.slider(
        "Geopotential Height (m)",
        min_value=0,
        max_value=18000,
        value=5500
    )

    temperature = st.slider(
        "Temperature (K)",
        min_value=180,
        max_value=330,
        value=280
    )

    humidity = st.slider(
        "Relative Humidity (%)",
        min_value=0,
        max_value=100,
        value=50
    )

    latitude = st.number_input(
        "Latitude",
        min_value=-90.0,
        max_value=90.0,
        value=28.60,
        format="%.2f"
    )

    longitude = st.number_input(
        "Longitude",
        min_value=-180.0,
        max_value=180.0,
        value=77.20,
        format="%.2f"
    )

    selected_date = st.date_input(
        "Date",
        value=date.today()
    )

    hour = st.selectbox(
        "Hour (UTC)",
        [0, 3, 6, 9, 12, 15, 18, 21],
        index=4
    )

    st.write("")

    predict = st.button(
        "🚀 Predict Wind",
        use_container_width=True
    )

    if predict:

        with st.spinner("Predicting Wind..."):

            try:

                pred_speed, pred_direction, pred_confidence = predict_wind(

                    pressure,
                    latitude,
                    longitude,
                    geopotential,
                    temperature,
                    humidity,
                    selected_date,
                    hour

                )
                # Convert short direction to full name
                direction_map = {
                    "N": "🧭 North",
                    "NE": "🧭 North-East",
                    "E": "🧭 East",
                    "SE": "🧭 South-East",
                    "S": "🧭 South",
                    "SW": "🧭 South-West",
                    "W": "🧭 West",
                    "NW": "🧭 North-West"
                }
                speed = f"{pred_speed} m/s"
                direction = direction_map.get(pred_direction, pred_direction)
                confidence = f"{pred_confidence}%"

            except Exception as e:

                st.error(f"Prediction Error : {e}")
# ==========================================================
# PREDICTION RESULTS
# ==========================================================

with right:

    st.subheader("📊 Prediction Results")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "🌬 Wind Speed",
            speed
        )

    with col2:

        st.metric(
            "🧭 Direction",
            direction
        )

    st.metric(
        "🎯 Confidence",
        confidence
    )

    if confidence != "-- %":

        confidence_value = float(
            confidence.replace("%", "")
        )

        st.progress(
            confidence_value / 100
        )

        st.success("Prediction Completed Successfully!")

    else:

        st.info(
            "👈 Enter the atmospheric parameters and click **Predict Wind**."
        )

# ==========================================================
# FEATURE IMPORTANCE
# ==========================================================

st.divider()

st.subheader("📈 Random Forest Feature Importance")

feature_importance = get_feature_importance()

fig = px.bar(

    feature_importance,

    x="Importance",

    y="Feature",

    orientation="h",

    color="Importance",

    text="Importance",

    color_continuous_scale="Blues"

)

fig.update_traces(

    texttemplate="%{x:.3f}",

    textposition="outside"

)

fig.update_layout(

    template="plotly_dark",

    height=500,

    margin=dict(
        l=20,
        r=20,
        t=20,
        b=20
    ),

    coloraxis_showscale=False,

    xaxis_title="Feature Importance",

    yaxis_title=""

)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.caption(
    "Feature importance values are obtained directly from the trained Random Forest Regressor."
)

# ==========================================================
# MODEL PERFORMANCE
# ==========================================================

st.divider()

st.subheader("🏆 Model Performance")

reg, clf = st.columns(2)

# ----------------------------------------------------------
# Regression Model
# ----------------------------------------------------------

with reg:

    st.markdown("### 🌬 Wind Speed Regression")

    c1, c2, c3 = st.columns(3)

    c1.metric("R² Score", "0.955")

    c2.metric("MAE", "2.11")

    c3.metric("RMSE", "2.89")

# ----------------------------------------------------------
# Classification Model
# ----------------------------------------------------------

with clf:

    st.markdown("### 🧭 Wind Direction Classification")

    c1, c2 = st.columns(2)

    c3, c4 = st.columns(2)

    c1.metric("Accuracy", "73%")

    c2.metric("Precision", "72%")

    c3.metric("Recall", "73%")

    c4.metric("F1 Score", "72%")

# ==========================================================
# ABOUT PROJECT
# ==========================================================

st.divider()

with st.expander("ℹ About this Project"):

    st.markdown("""

### 🌪 WindCast AI

WindCast AI predicts **Wind Speed** and **Wind Direction**
using atmospheric parameters extracted from the **IMDAA 3-hourly Weather Dataset**.

### 🤖 Machine Learning Models

- Random Forest Regressor
- Random Forest Classifier

### 📌 Input Features

- Pressure Level
- Geopotential Height
- Temperature
- Relative Humidity
- Latitude
- Longitude
- Date
- Hour
- Season

### 📊 Wind Speed Performance

- **R² Score:** 0.955
- **MAE:** 2.11
- **RMSE:** 2.89

### 📊 Wind Direction Performance

- **Accuracy:** 73%
- **Precision:** 72%
- **Recall:** 73%
- **F1 Score:** 72%

""")

# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.markdown(
"""
<div style="text-align:center;
padding:10px;
color:#CBD5E1;">

❤️ Built with <b>Python</b> |
🌪 <b>Streamlit</b> |
🤖 <b>Scikit-Learn</b> |
📊 <b>Plotly</b> |
🌍 <b>IMDAA 3-hourly Weather Dataset</b>

</div>
""",
unsafe_allow_html=True
)               