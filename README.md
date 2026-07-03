# 🌪️ WindCast-AI
### AI-Powered Wind Speed & Wind Direction Prediction using Machine Learning

WindCast-AI is an end-to-end Machine Learning project that predicts **Wind Speed** and **Wind Direction** using upper-air atmospheric parameters extracted from the **IMDAA (Indian Monsoon Data Assimilation and Analysis) 3-hourly Pressure Level Dataset** provided by the National Centre for Medium Range Weather Forecasting (NCMRWF).

The project includes the complete machine learning workflow, starting from raw meteorological data preprocessing to feature engineering, exploratory data analysis, model training, and deployment using **Streamlit**.

---

## 📌 Project Overview

This project predicts:

- 🌬️ Wind Speed (Regression)
- 🧭 Wind Direction (Classification)

using atmospheric variables such as:

- Pressure Level
- Geopotential Height
- Temperature
- Relative Humidity
- Latitude
- Longitude
- Date & Time
- Seasonal Features

The trained models are deployed through an interactive Streamlit web application.

---

# 📂 Dataset

This project uses the **IMDAA (Indian Monsoon Data Assimilation and Analysis)** regional reanalysis dataset provided by **NCMRWF (National Centre for Medium Range Weather Forecasting), Ministry of Earth Sciences, Government of India**. IMDAA is a high-resolution (~12 km) regional atmospheric reanalysis designed for studying the Indian monsoon and regional weather. :contentReference[oaicite:0]{index=0}

### Dataset Used

- IMDAA 3-Hourly Pressure Level Dataset
- Years Used: **2019 & 2020**
- Pressure Levels:
  - 50 hPa
  - 70 hPa
  - 100 hPa
  - 150 hPa
  - 200 hPa

### Original Dataset

https://rds.ncmrwf.gov.in/login

Dataset Access:

Users need to register on the NCMRWF Reanalysis Data Server to download the IMDAA dataset. :contentReference[oaicite:1]{index=1}

---

# 📁 Repository Structure

```
WindCast-AI
│
├── app.py
├── utils.py
├── style.css
├── requirements.txt
├── README.md
├── .gitignore
│
├── 01explore_dataset.ipynb
├── 02_featureengineering.ipynb
├── 03_EDA.ipynb
└── 04_ModelTraining.ipynb
```

---

# 🚀 Project Workflow

```
IMDAA Dataset
# 🔄 Project Workflow

The complete workflow of the project is illustrated below:

```text
                 IMDAA 3-Hourly Pressure Level Dataset
                              (2019 - 2020)
                                      │
                                      ▼
                      Data Extraction & Preprocessing
                                      │
                                      ▼
                  Processed Datasets (processed_2019,
                           processed_2020)
                                      │
                                      ▼
                        Feature Engineering
             (Temporal & Seasonal Feature Creation)
                                      │
                                      ▼
                  Feature Engineered Dataset
                         (Feature_engineered)
                                      │
                                      ▼
                  Exploratory Data Analysis (EDA)
      • Distribution Analysis
      • Correlation Analysis
      • Wind Pattern Visualization
      • Feature Importance Analysis
                                      │
                                      ▼
                     Machine Learning Model Training
             ┌────────────────────────────────────┐
             │ Random Forest Regressor            │
             │ → Wind Speed Prediction            │
             └────────────────────────────────────┘
                                      │
                                      ▼
             ┌────────────────────────────────────┐
             │ Random Forest Classifier           │
             │ → Wind Direction Prediction        │
             └────────────────────────────────────┘
                                      │
                                      ▼
                       Model Evaluation & Testing
                                      │
                                      ▼
                  Streamlit Web Application
                                      │
                                      ▼
                 Wind Speed & Direction Prediction
```

## 📒 Project Pipeline

The project follows four sequential notebooks:

### **1. Dataset Exploration & Preprocessing**

**Notebook:** `01explore_dataset.ipynb`

This notebook:

- Loads the raw IMDAA 3-hourly pressure level data.
- Cleans and preprocesses the meteorological variables.
- Extracts the required atmospheric parameters.
- Generates:

```
processed_2019/
processed_2020/
```

---

### **2. Feature Engineering**

**Notebook:** `02_featureengineering.ipynb`

This notebook creates the final machine learning dataset by:

- Creating temporal features
  - Year
  - Month
  - Day
  - Hour
- Creating seasonal features
- Preparing target variables
- Encoding categorical features

Output:

```
Feature_engineered/
```

---

### **3. Exploratory Data Analysis**

**Notebook:** `03_EDA.ipynb`

This notebook performs:

- Data visualization
- Correlation analysis
- Feature importance analysis
- Wind speed distribution
- Wind direction distribution
- Statistical insights

---

### **4. Model Training**

**Notebook:** `04_ModelTraining.ipynb`

This notebook trains two machine learning models:

### Wind Speed Prediction

- Random Forest Regressor

### Wind Direction Prediction

- Random Forest Classifier

The notebook also generates:

```
models/
├── wind_speed_model.pkl
├── wind_direction_model.pkl
└── feature_columns.pkl
```

> **Note:** The `models/` directory is not included in this repository because the trained model files exceed GitHub's file size limit. Running `04_ModelTraining.ipynb` will regenerate all required model files.

---

### **5. Streamlit Deployment**

After generating the trained models, launch the application:

```bash
streamlit run app.py
```

The web application allows users to:

- Input atmospheric parameters
- Predict wind speed
- Predict wind direction
- View prediction confidence
- Visualize feature importance
- Explore model performance
  # 📌 Project Summary

WindCast-AI is an end-to-end Machine Learning application developed to predict **Wind Speed** and **Wind Direction** using upper-air atmospheric observations from the **IMDAA 3-hourly Pressure Level Dataset** provided by **NCMRWF**.

The project demonstrates a complete data science workflow, beginning with raw meteorological data preprocessing, followed by feature engineering, exploratory data analysis, machine learning model development, evaluation, and deployment through an interactive Streamlit web application.

Using atmospheric variables collected at **50, 70, 100, 150, and 200 hPa pressure levels**, the application predicts:

- 🌬️ Wind Speed using a **Random Forest Regressor**
- 🧭 Wind Direction using a **Random Forest Classifier**

The models were trained using **IMDAA data from the years 2019 and 2020**, achieving:

| Model | Performance |
|--------|-------------|
| Wind Speed Regression | **R² = 0.955** |
| Wind Direction Classification | **Accuracy = 73%** |

The repository includes the complete workflow required to reproduce the project—from downloading the original IMDAA dataset, preprocessing the raw meteorological data, generating engineered features, training the machine learning models, and finally deploying the prediction system using Streamlit.

Large processed datasets and trained model files are intentionally excluded from the repository due to GitHub's file size limitations. However, the provided notebooks enable users to regenerate every intermediate dataset and trained model from scratch.

This project demonstrates practical applications of **Machine Learning**, **Meteorological Data Analysis**, **Feature Engineering**, and **Interactive Web Deployment**, making it suitable for atmospheric data analytics, educational purposes, and future research in weather forecasting.
---

## 👨‍💻 Author

**Kritika Oberoi**

- 📧 Email: kritikaoberoi1023@gmail.com
- 💼 LinkedIn: https://www.linkedin.com/in/kritika-oberoi-14353a356/
- 💻 GitHub: https://github.com/kritikaoberoi23
- 🧩 LeetCode: https://leetcode.com/u/kritikaoberoi1023/

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!
