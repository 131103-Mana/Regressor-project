import streamlit as st
import pickle
import numpy as np

# Load model
with open("random_forest_regressor.pkl", "rb") as file:
    model = pickle.load(file) 

st.title("Random Forest Regression App")

age = st.number_input("Age", 18, 70, 25)
experience = st.number_input("Experience Years", 0, 40, 2)
education = st.number_input("Education Years", 5, 25, 16)
hours = st.number_input("Hours Per Week", 1, 100, 40)
projects = st.number_input("Projects Completed", 0, 100, 5)
certifications = st.number_input("Certifications", 0, 20, 2)
performance = st.number_input("Performance Score", 0.0, 100.0, 75.0)

if st.button("Predict"):

    input_data = np.array([[
        age,
        experience,
        education,
        hours,
        projects,
        certifications,
        performance
    ]])

    prediction = model.predict(input_data)

    st.success(f"Predicted Value: {prediction[0]:.2f}")

