import pickle

# Loading the trained model and LabelEncoder
with open('clf_model.pkl', 'rb') as file:
    clf = pickle.load(file)

with open('label_encoder.pkl', 'rb') as file:
    le = pickle.load(file)

# Defining functions for making predictions
def predict(features):
  
    features = [features]
    prediction = clf.predict(features)
    return prediction[0]


import streamlit as st
# Streamlit app
st.title("Malaria Hotspot Prediction by Country")

st.write("""
# Predict the likelihood of malaria hotspots based on various factors.
Choose values from the features below:
""")

# Creating input fields for the features
rural_population = st.number_input("Rural population (% of total population)", min_value=0, max_value=100, value=50, step=1)
rural_population_growth = st.number_input("Rural population growth (annual %)", min_value=-10, max_value=10, value=0, step=1)
urban_population = st.number_input("Urban population (% of total population)", min_value=0, max_value=100, value=50, step=1)
urban_population_growth = st.number_input("Urban population growth (annual %)", min_value=-10, max_value=10, value=0, step=1)
basic_drinking_water_services = st.number_input("People using at least basic drinking water services (% of population)", min_value=0, max_value=100, value=80, step=1)
basic_drinking_water_services_rural = st.number_input("People using at least basic drinking water services, rural (% of rural population)", min_value=0, max_value=100, value=70, step=1)
basic_drinking_water_services_urban = st.number_input("People using at least basic drinking water services, urban (% of urban population)", min_value=0, max_value=100, value=90, step=1)
basic_sanitation_services = st.number_input("People using at least basic sanitation services (% of population)", min_value=0, max_value=100, value=60, step=1)
basic_sanitation_services_rural = st.number_input("People using at least basic sanitation services, rural (% of rural population)", min_value=0, max_value=100, value=50, step=1)
basic_sanitation_services_urban = st.number_input("People using at least basic sanitation services, urban  (% of urban population)", min_value=0, max_value=100, value=70, step=1)
year = st.number_input("Year", min_value=1900, max_value=2100, value=2023, step=1)
malaria_incidence = st.number_input("Incidence of malaria (per 1,000 population at risk)", min_value=0, max_value=1000, value=10, step=1)

# Collecting all the features into a list
features = [
    rural_population,
    rural_population_growth,
    urban_population,
    urban_population_growth,
    basic_drinking_water_services,
    basic_drinking_water_services_rural,
    basic_drinking_water_services_urban,
    basic_sanitation_services,
    basic_sanitation_services_rural,
    basic_sanitation_services_urban,
    year,
    malaria_incidence
]

# Making prediction when the button is pressed
if st.button("Predict"):
    prediction = predict(features)
    predicted_country = le.inverse_transform([prediction])[0]
    st.write(f"The predicted country is: {predicted_country}")
