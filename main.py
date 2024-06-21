import streamlit as st
import numpy as np
import pickle

# Function to preprocess input data
def preprocess_input(gender, ssc_p, ssc_b, hsc_p, hsc_b, hsc_s, degree_p, degree_t, workex, etest_p, specialisation, mba_p):
    # Encode categorical variables
    ssc_b_encoded = 1 if ssc_b == 'Central' else 0
    hsc_b_encoded = 1 if hsc_b == 'Central' else 0
    hsc_s_encoded = {'Science': 2, 'Commerce': 1, 'Arts': 0}.get(hsc_s, 0)
    degree_t_encoded = {'Sci&Tech': 2, 'Comm&Mgmt': 1, 'Others': 0}.get(degree_t, 0)
    specialisation_encoded = {'Mkt&HR': 1, 'Mkt&Fin': 0}.get(specialisation, 0)
    workex_encoded = 1 if workex == 'Yes' else 0
    
    # Convert input to numeric format
    gender_num = 1 if gender == 'Male' else 0
    input_data = np.array([[gender_num, float(ssc_p), ssc_b_encoded, float(hsc_p), hsc_b_encoded, hsc_s_encoded,
                            float(degree_p), degree_t_encoded, workex_encoded, float(etest_p),
                            specialisation_encoded, float(mba_p)]])
    
    return input_data

# Load the model
try:
    with open('model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
except Exception as e:
    st.error(f"Error loading model: {e}")

# Set page configuration
st.set_page_config(page_title="Student Information Form", layout="wide")

# Custom CSS for background image and button styles
st.markdown("""
    <style>
    body {
        background-image: url('C:/Users/user/Desktop/IT vedant/ml project/1 campuse placement/campus.jpg');
        background-size: cover;
        background-position: center;
    }
    .stApp {
        width: 100%;
        height: 100%;
        padding: 20px;
        box-sizing: border-box;
    }
    .form-container {
        background: rgba(0, 0, 0, 0.5);
        padding: 20px;
        border-radius: 10px;
        color: white;
        width: 300px;
        margin: auto;
        margin-top: 50px;
    }
    h2 {
        color: #FEB941;
        text-shadow: 2px 2px 4px #000000;
        font-size: 3rem;
        text-align: center;
    }
    .stButton button {
        height: 3rem;
        width: 10rem;
        margin: auto;
        border-radius: 0.5rem;
        background-color: #FF7F50;
        color: white;
        font-size: 1.2rem;
        border: none;
        display: block;
    }
    .stButton button:hover {
        background-color: #FF6347;
    }
    .stButton button:active {
        background-color: #FF6347;
        box-shadow: 0 5px #666;
        transform: translateY(4px);
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h2 style='color: white;'>Placement Prediction</h2>", unsafe_allow_html=True)

# Form
with st.form(key='student_info_form'):
    gender = st.selectbox('Gender', ['Male', 'Female'], key='gender')
    ssc_p = st.text_input('SSC Percentage', key='ssc_p')
    ssc_b = st.selectbox('SSC Board', ['Central', 'Others'], key='ssc_b')
    hsc_p = st.text_input('HSC Percentage', key='hsc_p')
    hsc_b = st.selectbox('HSC Board', ['Central', 'Others'], key='hsc_b')
    hsc_s = st.selectbox('HSC Stream', ['Science', 'Commerce', 'Arts'], key='hsc_s')
    degree_p = st.text_input('Degree Percentage', key='degree_p')
    degree_t = st.selectbox('Degree Type', ['Sci&Tech', 'Comm&Mgmt', 'Others'], key='degree_t')
    workex = st.selectbox('Work Experience', ['Yes', 'No'], key='workex')
    etest_p = st.text_input('E-test Percentage', key='etest_p')
    specialisation = st.selectbox('Specialisation', ['Mkt&HR', 'Mkt&Fin'], key='specialisation')
    mba_p = st.text_input('MBA Percentage', key='mba_p')

    # Submit button
    submit_button = st.form_submit_button(label='Predict Status')

# Handle form submission
if submit_button:
    try:
        # Preprocess input data
        input_data = preprocess_input(gender, ssc_p, ssc_b, hsc_p, hsc_b, hsc_s, degree_p, degree_t, workex, etest_p, specialisation, mba_p)
        
        # Make prediction
        prediction = model.predict(input_data)
        
        # Interpret prediction
        if prediction[0] == 1:
            st.write("Prediction: Placed")
        else:
            st.write("Prediction: Not Placed")
            
    except Exception as e:
        st.error(f"Error making prediction: {e}")
