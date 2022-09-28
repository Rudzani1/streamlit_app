

import pickle
import streamlit as st
from streamlit_option_menu import option_menu



diabetes_model = pickle.load(open("diabetes_model.sav", "rb"))


with st.sidebar:
  selected = option_menu("Prediction Model",
                         ["Diabetes Prediction"],
                         icons=["activity", "heart", "person"],
                         default_index=0)



if (selected == "Diabetese Prediction"):

  # page title
  st.title("Smart Diabetes Assistant")

  # getting the input data from the user
  col1, col2, col3 = st.columns(3)

  with col1:
    Pregnancies = st.text_input("Number of Pregnancies")

  with col2:
    Glucose = st.text_input("Glucose Level")

  with col3:
    BloodPressure = st.text_input("Blood Pressure Value")

  with col1:
    SkinThickness = st.text_input("Skin Thickness Value")

  with col2:
    Insulin = st.text_input("Insulin Level")

  with col3:
    BMI = st.text_input("BMI Value")

  with col1:
    DiabetesPedigreeFuntion = st.text_input("Diabetes Pedigree Function Value")

  with col2:
   Age  = st.text_input("Age of the Person")



diab_diagnosis = ""



if st.button("Diabetes Test Result"):
  diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFuntion, Age]])

  if (diab_prediction[0] == 1):
    diab_diagnosis = "The person is diabetic"
  else:
    diab_diagnosis = "The person is not diabetic"

st.success(diab_diagnosis)
