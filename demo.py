import streamlit as st
import numpy as np
import pickle
import base64
from streamlit_option_menu import option_menu

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

# Function to load the image and convert to base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Load the model
try:
    with open('model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
except Exception as e:
    st.error(f"Error loading model: {e}")

# Set page configuration
st.set_page_config(page_title="Student Information Form", layout="wide")

# Encode the image to base64 - Replace with your single background image path
img_base64 = get_base64_of_bin_file(r'images\leon-wu-LLfRMRT-9AY-unsplash.jpg')

# Custom CSS for background image and button styles
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{img_base64}");
        background-size: cover;
        background-position: center;
        width: 100%;
        height: 100%;
        box-sizing: border-box;
        display: flex;
        justify-content: center;
        align-items: center;
    }}
    .form-container {{
        background: rgba(0, 0, 0, 0.6);
        padding: 30px;
        border-radius: 10px;
        color: white;
        width: 897px; /* Adjusted width to 897px */
        margin: auto;
        box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.5);
    }}
    .form-container * {{
        font-weight: bold;
    }}
    h2 {{
        color: #FEB941;
        text-shadow: 2px 2px 4px #000000;
        font-size: 3rem;
        text-align: center;
        margin-bottom: 30px;
    }}
    .stTextInput > div > div {{
        font-size: 1rem;
        color: black;
    }}
    .stSelectbox > div > div {{
        font-size: 1rem;
        color: black;
    }}
    .stButton button {{
        height: 3rem;
        width: 100%;
        border-radius: 0.5rem;
        background-color: #FF7F50;
        color: black;
        font-size: 1.2rem;
        border: none;
        display: block;
        cursor: pointer;
        margin-top: 20px;
    }}
    .stButton button:hover {{
        background-color: #FF6347;
    }}
    .stButton button:active {{
        background-color: #FF6347;
        box-shadow: 0 5px #666;
        transform: translateY(4px);
    }}
    .stWarning {{
        color: rgb(0, 0, 0); /* New text color */
        font-weight: bold;
        background-color: rgb(255, 18, 18); /* Background color */
        padding-top: 17px; /* Padding-top */
        padding: 10px; /* Additional padding for better spacing */
        border-radius: 5px; /* Rounded corners */
    }}
    .stSuccess {{
        background-color: rgb(33, 195, 84); /* Background color */
        padding-top: 17px; /* Padding-top */
        padding: 10px; /* Additional padding for better spacing */
        border-radius: 5px; /* Rounded corners */
    }}
    .st-bu {{
        background-color: #00000069;
    }}
    .st-emotion-cache-ue6h4q {{
        font-size: 14px;
        color: black;
        visibility: unset;
    }}
    .st-emotion-cache-1whx7iy p {{
        word-break: initial;
        margin-bottom: 0px;
        font-size: larger;
        margin: 0px 0px 1rem;
        margin-bottom: 1rem;
        padding: 0px;
        font-size: 1rem;
        font-weight: 1000;
    }}
    .st-dg {{
        background-color: rgb(33, 195, 84);
        padding-top: 17px;
        padding: 10px;
        border-radius: 5px;
    }}
    .stTextInput > div > div > label {{
        font-weight: 1000;
        color: black;
    }}
    .stSelectbox > div > div > label {{
        font-weight: 1000;
        color: black;
    }}
    .underlined {{
        position: relative;
    }}
    .underline-mask:after {{
        content: '';
        position: absolute;
        top: 95%;
        width: 150%;
        aspect-ratio: 3 / 1;
        left: 50%;
        transform: translate(-50%, 0);
        border-radius: 50%;
        border: 6px solid hsl(280 80% 50%);
        --spread: 140deg;
        --start: 290deg;
        mask: conic-gradient(from var(--start), white 0 var(--spread), transparent var(--spread));
    }}
    .underline-overflow {{
        display: inline-block;
        overflow: hidden;
        padding-bottom: clamp(1rem, 2vmin, 2rem);
    }}
    .underline-overflow:after {{
        content: '';
        position: absolute;
        top: 100%;
        height: 150%;
        aspect-ratio: 2.5 / 1;
        left: 50%;
        transform: translate(-50%, -10%);
        border-radius: 50%;
        border: 6px solid hsl(10 80% 50%);
    }}
    .underline-clip:after {{
        content: '';
        position: absolute;
        top: 95%;
        width: 150%;
        aspect-ratio: 3 / 1;
        left: 50%;
        transform: translate(-50%, 0);
        border-radius: 50%;
        border: 6px solid hsl(130 80% 50%);
        clip-path: polygon(0 0, 50% 50%, 100% 0);
    }}
    .underlined h2 {{
        font-size: clamp(3rem, 15vmin, 8rem);
        font-family: sans-serif;
        color: hsl(0 0% 98%);
    }}
    
    </style>
""", unsafe_allow_html=True)

# Sidebar with option menu
with st.sidebar:
    selected = option_menu("Choose Your Course", ['INFO', 'MBA', 'ENGINEERING'])

# Show form and prediction only if "INFO" is selected
if selected == 'INFO':
    # Title with underlined style
    st.markdown('<h2 class="underlined underline-clip">Placement Prediction</h2>', unsafe_allow_html=True)
    # Message in the info section
    st.markdown("<div class='st-emotion-cache-1whx7iy p'>Analyzing Placement Trends Across Different Academic Disciplines</div>", unsafe_allow_html=True)

# Show form and prediction only if "MBA" is selected
elif selected == 'MBA':
    # Title with underlined style
    st.markdown('<h2 class="underlined underline-clip">MBA Placement Prediction</h2>', unsafe_allow_html=True)
    # Form
    with st.form(key='student_info_form', clear_on_submit=True):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            gender = st.selectbox('Gender', ['Male', 'Female'], key='gender')
            ssc_p = st.text_input('SSC Percentage', key='ssc_p')
            ssc_b = st.selectbox('SSC Board', ['Central', 'Others'], key='ssc_b')
        
        with col2:
            hsc_p = st.text_input('HSC Percentage', key='hsc_p')
            hsc_b = st.selectbox('HSC Board', ['Central', 'Others'], key='hsc_b')
            hsc_s = st.selectbox('HSC Stream', ['Science', 'Commerce', 'Arts'], key='hsc_s')
        
        with col3:
            degree_p = st.text_input('Degree Percentage', key='degree_p')
            degree_t = st.selectbox('Degree Type', ['Sci&Tech', 'Comm&Mgmt', 'Others'], key='degree_t')
            workex = st.selectbox('Work Experience', ['Yes', 'No'], key='workex')
        
        col4, col5 = st.columns(2)
        
        with col4:
            etest_p = st.text_input('E-test Percentage', key='etest_p')
            specialisation = st.selectbox('Specialisation', ['Mkt&HR', 'Mkt&Fin'], key='specialisation')
        
        with col5:
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
                st.markdown("<div class='stSuccess'>Prediction: You will be Placed</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='stWarning'>Prediction: You will Not be Placed</div>", unsafe_allow_html=True)
                
        except Exception as e:
            st.error(f"Error making prediction: {e}")

