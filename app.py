import streamlit as st
import pickle
import datetime
import pandas as pd

model=pickle.load(open('electricity_prediction_model_copy.pkl','rb'))



st.set_page_config(page_title="Electricity Demand Forecasting", page_icon="⚡")



st.title('Electricity Demand Prediction')

st.info(
    """
    **Model Information**
    - 📊 Model: XGBoost Regressor
    - 📅 Training Data: January 2020 – December 2024
    - ✅ Mean Absolute Error (MAE): 102.55
    - 🎯 Average Percentage Error (MAE %): 2.05%
    - Features Used: Date, Time, Temperature, and Humidity

    
    """
)

date=st.date_input("Enter a Date :", value=datetime.date(2025, 2, 6),min_value=datetime.date(2020, 1, 1), max_value='today')

hour=st.number_input("Enter a Hour :",value=7, min_value=0, max_value=23 )

temperature = st.number_input(label="Enter temperature (°C):",min_value=1.0, max_value=51.0,value=27.0000,step=0.1,format="%.4f")

humidity = st.number_input("Enter Relative Humidity (%):", min_value=0.0, max_value=100.0, value=60.1155, step=0.5,format="%.4f")

if st.button('Predict the Demand'):
   timestamp=pd.to_datetime(date)
   dayofweek=timestamp.dayofweek
   month= timestamp.month
   year= timestamp.year
   dayofyear= timestamp.dayofyear
   weekofyear= timestamp.isocalendar().week
   quarter= timestamp.quarter
   is_weekend= int(dayofweek>=5)

   x_pred = pd.DataFrame({
    'hour':[hour],
    'dayofweek':[dayofweek],
    'month':[month],
    'year':[year],
    'dayofyear':[dayofyear],
    'weekofyear':[weekofyear],
    'quarter':[quarter],
    'is_weekend':[is_weekend],
    'Temperature':[temperature],
    'Humidity':[humidity],
   })
   res=model.predict(x_pred)
   res=res[0]

   st.header(f"Predicted Demand: {res:.2f}")


   