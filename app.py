import streamlit as st
import numpy as np
import pickle

# Load the trained model (Ensure the path is correct)
with open('vehicle_rental_price_modelV2.pickle', 'rb') as f:
    model = pickle.load(f)

def get_vehicle_type_numeric(vehicle_type):
    vehicle_type_mapping = {"Premium": 1, "Economy": 0}
    return vehicle_type_mapping.get(vehicle_type)

def predict_price(number_of_riders, number_of_drivers, vehicle_type, expected_ride_duration):
    vehicle_type_numeric = get_vehicle_type_numeric(vehicle_type)
    if vehicle_type_numeric is None:
        return "Invalid vehicle type"
    input_data = np.array([[number_of_riders, number_of_drivers, vehicle_type_numeric, expected_ride_duration]])
    return model.predict(input_data)[0]

# Streamlit UI
st.title('Dynamic Cab Fair Prediction')

number_of_riders = st.number_input('Number of Riders', min_value=1, value=1)
number_of_drivers = st.number_input('Number of Drivers', min_value=1, value=1)
vehicle_type = st.selectbox('Vehicle Type', ['Premium', 'Economy'])
expected_ride_duration = st.slider('Expected Ride Duration (in minutes)', 0, 120, 30)

if st.button('Predict Price'):
    predicted_price = predict_price(number_of_riders, number_of_drivers, vehicle_type, expected_ride_duration)
    st.write(f'Predicted Price: ${predicted_price}')
