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




def preprocess_engineering_input( stream, internships, cgpa, history_of_backlogs):
    # Encode categorical variables
    stream_encoded = {'Computer Science': 1, 'Information Technology': 4, 'Mechanical': 5, 'Civil': 3, 'Electronics And Communication': 3 ,'Electrical' :2 , 'Civil' :0}.get(stream, 0)
    history_of_backlogs_encoded = 1 if history_of_backlogs == 'Yes' else 0
    internships_encoded = 1 if internships == "yes" else 0
    # Convert input to numeric format
    input_data_2 = np.array([[stream_encoded, internships_encoded, float(cgpa), history_of_backlogs_encoded]])

    return input_data_2


# Function to load the image and convert to base64
# Function to load the image and convert to base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Load the models

# model 1
try:
    with open('model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
except Exception as e:
    st.error(f"Error loading model: {e}")
# model 2
try:
    with open('engi.pkl', 'rb') as model_file:
        model_2 = pickle.load(model_file)
except Exception as e:
    st.error(f"Error loading model: {e}")

# Set page configuration
st.set_page_config(page_title="Student Information Form", layout="wide")

# Encode the image to base64 - Replace with your single background image path
img_base64 = get_base64_of_bin_file(r'C:\Users\user\Desktop\IT vedant\ml project\1 campuse placement\images\leon-wu-LLfRMRT-9AY-unsplash.jpg')

# Custom CSS for background image and button styles
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
    .st-emotion-cache-1whx7iy {{
    font-family: 'Poppins', sans-serif; /* Use the imported Google Font */
    font-size: 1.2rem; /* Adjust font size as needed */
    line-height: 1.6; /* Adjust line height as needed */
    background: rgba(0, 0, 0, 0.5); /* Black background with 50% opacity */
    color: #ffffff; /* White text */
    padding: 20px; /* Padding around the content */
    border-radius: 10px; /* Rounded corners */
    font-weight: 300; /* Lighter font weight */
    }}
    

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
        color: white;
        visibility: unset;
    }}
    .st-emotion-cache-1whx7iy p {{
        word-break: initial;
        margin-bottom: 0px;
        font-size: larger;
        margin: 0px 0px 1rem;
        margin-bottom: 0rem;
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
        font-weight: 800;
        color: black;
    }}
    
    
    
    .shimmer {{
        font-family: "Lato";
        font-weight: 300;
        font-size: 3rem;
        text-align: center;
        margin-bottom: 0;
        color: rgba(255, 255, 255, 0.1);
        background: -webkit-gradient(linear, left top, right top, from(#222), to(#222), color-stop(0.5, #fff));
        background: -moz-gradient(linear, left top, right top, from(#222), to(#222), color-stop(0.5, #fff));
        background: gradient(linear, left top, right top, from(#222), to(#222), color-stop(0.5, #fff));
        background-size: 125px 100%;
        background-clip: text;
        animation-name: shimmer;
        animation-duration: 2s;
        animation-iteration-count: infinite;
        background-repeat: no-repeat;
        background-position: 0 0;
        background-color: #222;
    }}

    

    @keyframes shimmer {{
        0% {{
            background-position: top left;
        }}
        100% {{
            background-position: top right;
        }}
    }}
    </style>
""", unsafe_allow_html=True)

# Sidebar with option menu
with st.sidebar:
    selected = option_menu("Choose Your Course", ['INFO', 'MBA', 'ENGINEERING'])

# Show form and prediction only if "INFO" is selected
if selected == 'INFO':
    # Title with underlined style
    st.markdown('<h2 class="underlined underline-clip shimmer"">Welcome to Placement Prediction Application</h2>', unsafe_allow_html=True)
    # Message in the info section
    st.markdown("<h2 class = 'fancy' >  About </h2>" , unsafe_allow_html=True)
    st.markdown("<h3 class='st-emotion-cache-1whx7iy'>Welcome to our Placement Prediction Application! This tool is designed to predict the likelihood of a student getting placed based on various educational and personal factors. Whether you're a student planning your career path or an academic advisor guiding students, this application provides valuable insights derived from machine learning models.</h3>", unsafe_allow_html=True)
    st.markdown('<a href="https://drive.google.com/drive/home">Documentation</a>', unsafe_allow_html=True)         

# Show form and prediction only if "MBA" is selected
elif selected == 'MBA':
    # Title with underlined style
    st.markdown('<h2 class="underline-clip shimmer">MBA Placement Prediction</h2>', unsafe_allow_html=True)
    # Form
    with st.form(key='mba_student_info_form'):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            gender = st.selectbox('Gender', ['Male', 'Female'], key='gender')
            hsc_p = st.number_input('HSC Percentage', min_value=0.00, max_value=100.00, key='hsc_p')
            degree_p = st.number_input('Degree Percentage', min_value=0.00, max_value=100.00, key='degree_p')
        
        with col2:
            ssc_p = st.number_input('SSC Percentage', min_value=0.00, max_value=100.00, key='ssc_p')
            hsc_s = st.selectbox('HSC Stream', ['Science', 'Commerce', 'Arts'], key='hsc_s')
            degree_t = st.selectbox('Degree Type', ['Sci&Tech', 'Comm&Mgmt', 'Others'], key='degree_t')
            
        with col3:
            ssc_b = st.selectbox('SSC Board', ['Central', 'Others'], key='ssc_b')
            hsc_b = st.selectbox('HSC Board', ['Central', 'Others'], key='hsc_b')
            workex = st.selectbox('Work Experience', ['Yes', 'No'], key='workex')
        
        col4, col5 = st.columns(2)
        
        with col4:
            etest_p = st.number_input('E-test Percentage', min_value=0.00, max_value=100.00, key='etest_p')
            specialisation = st.selectbox('Specialisation', ['Mkt&HR', 'Mkt&Fin'], key='specialisation')
        
        with col5:
            mba_p = st.number_input('MBA Percentage', min_value=0.00, max_value=100.00, key='mba_p')
        
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


elif selected == 'ENGINEERING':
       # Title with underlined style
    st.markdown('<h2 class="underline-clip shimmer">Engineering Placement Prediction</h2>', unsafe_allow_html=True)

    with st.form(key='engi_student_info_form'):
        col1, col2 = st.columns(2)
    
        # Input fields in form
        with col1:
            stream_options = ['Electronics And Communication', 'Computer Science', 'Information Technology', 'Mechanical', 'Electrical', 'Civil']
            stream = st.selectbox('Stream', stream_options)
            internships = st.selectbox('Done Any Internships', ['Yes', 'No'])
        
        with col2:
            
            cgpa = st.number_input('CGPA', min_value=0.0, max_value=10.0, step=0.1)
            history_of_backlogs = st.selectbox('Do you have any backlog', ['Yes', 'No'])
     # Preprocess data on form submission
        submit_button_2 =  st.form_submit_button('Predict Status')

    if submit_button_2:
            try:
                # Preprocess input data
                input_data_2 = preprocess_engineering_input( stream, internships, cgpa, history_of_backlogs)
                
                # Make prediction
                prediction = model_2.predict(input_data_2)
                
                # Interpret prediction
                if prediction[0] == 1:
                    st.markdown("<div class='stSuccess'>Prediction: You will be Placed</div>", unsafe_allow_html=True)
                else:
                    st.markdown("<div class='stWarning'>Prediction: You will Not be Placed</div>", unsafe_allow_html=True)
                    
            except Exception as e:
                st.error(f"Error making prediction: {e}")

           
            



    


