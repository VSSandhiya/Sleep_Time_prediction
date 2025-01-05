import streamlit as st 
import pandas as pd
import pickle

st.title("Sleep Time Prediction")

WorkoutTime=st.number_input("Enter the WorkoutTime")
ReadingTime=st.number_input("Pick Your ReadingTime")
PhoneTime=st.number_input("Select the PhoneTime")
WorkHours=st.number_input('Select the WorkHours')
CaffeineIntake=st.number_input("Enter the CaffeineIntake")
RelaxationTime=st.number_input("Enter the RelaxationTime")
#x=st.number_input("Enter the x")
#z=st.number_input("Enter z")
submit=st.button("Submit")

with open('modellinear.pkl', 'rb') as file:  
    model = pickle.load(file)

if submit==True:
    
    prediction_data=pd.DataFrame({
        'WorkoutTime':[WorkoutTime],
        'ReadingTime':[ReadingTime],
        'PhoneTime':[PhoneTime],
        'WorkHours':[WorkHours],
        'CaffeineIntake':[CaffeineIntake],
        'RelaxationTime':[RelaxationTime],
        #'x':[x],
        #'#z':[z]
    })
    
    prediction=model.predict(prediction_data)

    st.text_area('Result',prediction)
