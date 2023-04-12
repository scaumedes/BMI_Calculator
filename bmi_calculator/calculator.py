import streamlit as st

st.header('BMI Calculator')
st.write('Eneter your data below')

#function for calculation
def bmi_calculator(weight, height, units):
    if units == 'inches/lbs':
        return (weight / (height * height)) * 703
    if units == 'meters/kg':
        return weight / (height * height)

#defining form
with st.form(key='columns_in_form', clear_on_submit = True):
    units = st.selectbox('Select your units', ('meters/kg', 'inches/lbs'))
    col1, col2 = st.columns(2)
    with col1:
        height = st.text_input(label='Enter height')
    with col2:
        weight = st.text_input(label = 'Enter weight')
    submitted = st.form_submit_button('Submit')

#calculation after form submission
if submitted:
    try:
        if bmi_calculator(float(weight), float(height), units) < 18.5:
            st.write('Underweight')
        elif 18.5 <= bmi_calculator(float(weight), float(height), units) < 24.9:
            st.write('Normal weight')
        elif  25 <= bmi_calculator(float(weight), float(height), units) < 29.9:
            st.write('Overweight')
        else:
            st.write('Obese')
    except:
        st.write('Please enter correct data')
