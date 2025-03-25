
import streamlit as st

# Unit conversion laga rahe hn
def convert_length(value, from_unit, to_unit):
    units = {'meters': 1, 'kilometers': 1000, 'centimeters': 0.01, 'millimeters': 0.001, 'miles': 1609.34, 'yards': 0.9144, 'feet': 0.3048}
    value_in_meters = value * units[from_unit]
    return value_in_meters / units[to_unit]

def convert_mass(value, from_unit, to_unit):
    units = {'grams': 1, 'kilograms': 1000, 'milligrams': 0.001, 'pounds': 453.592, 'ounces': 28.3495}
    value_in_grams = value * units[from_unit]
    return value_in_grams / units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return (value * 9/5) + 32
    if from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (value - 32) * 5/9
    if from_unit == 'Celsius' and to_unit == 'Kelvin':
        return value + 273.15
    if from_unit == 'Kelvin' and to_unit == 'Celsius':
        return value - 273.15
    if from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
        return (value - 32) * 5/9 + 273.15
    if from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
        return (value - 273.15) * 9/5 + 32

#  tite bnyt
st.title("🌏Unit converter")     
st.markdown("### convert lenght,mass,temperature")
st.write("welcome")

# Unit length wgera choose krne k liye
conversion_type = st.selectbox("Conversion Type", ["Length", "Mass", "Temperature"])

# Input dalne k liye
value = st.number_input("Enter Value", min_value=0.0, step=0.01)

if conversion_type == "Length":
    from_unit = st.selectbox("From Unit", ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet"])
    to_unit = st.selectbox("To Unit", ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet"])
    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result} {to_unit}😃")

elif conversion_type == "Mass":
    from_unit = st.selectbox("From Unit", ["grams", "kilograms", "milligrams", "pounds", "ounces"])
    to_unit = st.selectbox("To Unit", ["grams", "kilograms", "milligrams", "pounds", "ounces"])
    if st.button("Convert"):
        result = convert_mass(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result} {to_unit}😃")

elif conversion_type == "Temperature":
    from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result} {to_unit}😃")

