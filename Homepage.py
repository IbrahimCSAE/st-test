# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 01:00:51 2023

@author: Marwan
"""

from pathlib import Path

import numpy as np
import pickle
import streamlit as st
import streamlit_authenticator as stauth

# Main Page

st.set_page_config(
    page_title="Heart Disease Prediction ❤️",
    page_icon="❤️",
    )


st.sidebar.success("Select a page above.")




    # User Authentication
names = ["Marwan"]
usernames = ["marwan"]
    
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
        hashed_passwords = pickle.load(file)
        
authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "cookie_name", "abcdef", cookie_expiry_days=0)
    
name, authentication_status, username = authenticator.login("Login", "main")
    
if authentication_status == False:
        st.error("Username/Password is incorrect")
        
if authentication_status == None:
        st.warning("Please enter your username and password")
        
if authentication_status:    



    # Loading the model
    model_path = Path(__file__).parent / "trained_model.sav"
    with model_path.open("rb") as model_file:
            loaded_model = pickle.load(model_file)
    authenticator.logout("Logout", "sidebar")
    # Create a function for prediction
    
    def heart_prediction(input_data):
        
        # change the input data to a numpy array
        input_data_as_numpy_array= np.asarray(input_data)
    
        # reshape the numpy array as we are predicting for only on instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
        prediction = loaded_model.predict(input_data_reshaped)
        print(prediction)
    
        if (prediction[0]== 0):
            return 'The Person does not have a Heart Disease'
        else:
             return 'The Person has Heart Disease'
         
            
         
    def main():
        
        # Set a title for our page
        st.title('❤️ Heart Disease Prediction Web App ❤️')
        
        # Getting input data from the user
        
        age = st.number_input('AGE')
               
        sex = st.radio("Select Gender: ", ('1', '0'))
        if (sex == '1'):
                   st.info("Male")
        else:
                   st.info("Female")

        cp = st.radio("CHEST PAIN TYPE (0 = typical angina,1 = atypical angina,2 = non — anginal pain,3= asymptotic)",['0','1','2','3'])
        trestbps = st.number_input('Resting Blood Pressure')
        chol  = st.number_input('Serum Cholestoral')
        fbs = st.radio("FASTING BLOOD SUGAR( > 120mg/dl : 1, else : 0)",['1','0'])
        restecg = st.radio("RESTING ECG(0-normal, 1-abnormal)",['0','1','2'])
        thalach = st.number_input('Maximum Heart Rate')
        exang = st.radio("EXERCISE INDUCED ANGINA(1-yes, 0-no)",['1','0'])
        oldpeak = st.number_input('oldpeak')
        slope = st.radio("PEAK EXERCISE ST SEGMENT(0 = upsloping,1 = flat,2= downsloping)",['0','1','2'])
        ca  = st.number_input('Number of Major Vessels')
        thal = st.number_input('Thal')
        
        # Prediction
        
        diagnosis = ''
        
        # Creating a button for Prediction
        
        if st.button('Heart Disease Result'):
            # convert all the strings to numbers
            age = int(age)
            sex = int(sex)
            cp = int(cp)
            trestbps = int(trestbps)
            chol = int(chol)
            fbs = int(fbs)
            restecg = int(restecg)
            thalach = int(thalach)
            exang = int(exang)
            oldpeak = float(oldpeak)
            slope = int(slope)
            ca = int(ca)
            thal = int(thal)
            
            diagnosis = heart_prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
            
        st.success(diagnosis)
            
        
    if __name__ == '__main__':
        main()        
    
    
    
    
    
    
    
    
    
    
    
    
