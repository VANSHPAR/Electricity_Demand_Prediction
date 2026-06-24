# ⚡ Electricity Demand Prediction

A machine learning-based web application for forecasting electricity demand using an **XGBoost Regressor**. The application allows users to predict electricity demand by providing the date, hour, temperature, and humidity.

## 🚀 Features

- Predict electricity demand in real time.
- Interactive web interface built with Streamlit.
- Automatic extraction of date-based features.
- Trained on historical electricity demand data from **2020–2024**.
- Average prediction error of approximately **2.05%**.

---

## 📊 Model Information

- **Model:** XGBoost Regressor
- **Training Data:** January 2020 – December 2024
- **Mean Absolute Error (MAE):** 102.55 units
- **Root Mean Squared Error (RMSE):** 151.24 units
- **Average Percentage Error:** 2.05%

---

## 🛠️ Features Used

The model uses the following features:

- Hour
- Day of Week
- Month
- Year
- Day of Year
- Week of Year
- Quarter
- Weekend Indicator
- Temperature (°C)
- Humidity (%)

Date-related features are automatically extracted from the selected date.

---

## 📁 Project Structure

```
.
├── app.py                                # Streamlit application
├── electricity_prediction_model_copy.pkl # Trained XGBoost model
├── requirements.txt                      # Dependencies
├── Electricity_Demand_Dataset.csv        # Dataset
├── project_copy.ipynb
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/electricity-demand-prediction.git
cd electricity-demand-prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

Open your browser and visit:

```
http://localhost:8501
```

---

## 📈 Model Training

### Train-Test Split

The data is split chronologically:

- **Training Data:** Up to December 31, 2023
- **Testing Data:** January 1, 2024 onward

This approach prevents data leakage and preserves the time-series nature of the problem.

### Algorithm

- **XGBoost Regressor**

---

## 📸 Application Inputs

Users provide:

- 📅 Date
- 🕒 Hour (0–23)
- 🌡️ Temperature (°C)
- 💧 Relative Humidity (%)

The application automatically generates additional calendar-based features and predicts electricity demand.

---

## 📊 Performance

| Metric | Value |
|----------|-------:|
| MAE | 102.55 |
| RMSE | 151.24 |
| Average Demand | 5000.67 |
| Average Percentage Error | 2.05% |

---

## 🔧 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- Streamlit
- Joblib


## 👨‍💻 Author

**Vansh Parmar**

If you found this project helpful, feel free to ⭐ the repository.
