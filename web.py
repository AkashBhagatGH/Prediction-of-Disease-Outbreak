import os #interact with file system determine directory of code
import pickle #load pretrained ml model 
import streamlit as st    #creating webapp
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreak',
                   layout='wide',
                   page_icon="doctor")
diabetes_model= pickle.load(open(r"C:\Users\Akash\OneDrive\Desktop\Predection of dieases outbreak\project\training_module\diabetes_model.sav" ,'rb'))
parkinson_model= pickle.load(open(r"C:\Users\Akash\OneDrive\Desktop\Predection of dieases outbreak\project\training_module\parkinson_model.sav",'rb'))
heart_model = pickle.load(open(r"C:\Users\Akash\OneDrive\Desktop\Predection of dieases outbreak\project\training_module\heart_model.sav",'rb'))
with st.sidebar:
    selected = option_menu('Prediction of Disease outbreak system',['Diabetes Prediction','Heart Disease Prediction' ,'Parkinsons Prediction'],
                           menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)

if selected == 'Diabetes Prediction':
   st.title('Diabetes Prediction using ML')
   col1,col2,col3 = st.columns(3)
   with col1:
       Pregnancies =st.text_input('Number of Pregnancies')
   with col2:
       Glucose = st.text_input('Gluclose Level')
   with col3:
       BloodPressure = st.text_input('Blood Pressure Value')
   with col1:
       SkinThickness = st.text_input('Skin Thickness value')
   with col2:
       Insulin = st.text_input('Insulin Level')
   with col3:
       BMI = st.text_input('BMI Value')
   with col1:
       DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
   with col2:
       Age = st.text_input('Age of the Person') 

       diab_diagnosis = ''
       if st.button('Diabetes Test Result'):
           user_input=[Pregnancies,Glucose,BloodPressure , SkinThickness , Insulin ,BMI , DiabetesPedigreeFunction , Age]
           user_input =[float (x)  for x in user_input]
           diab_prediction = diabetes_model.predict([user_input])
           if diab_prediction[0] == 1:
               diab_diagnosis= 'The person is diabetic'
           else:
               diab_diagnosis = 'The person is not diabetic'
           st.success(diab_diagnosis)

#Parkison Diease
if selected == 'Parkinsons Prediction':
   st.title('Parkinsons Prediction using ML')
   col1,col2,col3,col4 = st.columns(4)
   with col1:
       MDVP_Fo_Hz=st.text_input('MDVP:Fo(Hz)')
   with col2:
       MDVP_Fhi_Hz =st.text_input('MDVP:Fhi(Hz)')
   with col3:
       MDVP_Flo_Hz = st.text_input('MDVP_Flo_Hz')
   with col4:
       MDVP_Jitter_percent = st.text_input('MDVP:Jitter(%)')
   with col1:
       MDVP_Jitter_Abs = st.text_input('MDVP_Jitter(Abs)')
   with col2:
       MDVP_RAP = st.text_input('MDVP_RAP')
   with col3:
       MDVP_RAP_percent = st.text_input('MDVP_RAP(%)')
   with col4:
       Jitter_DDP = st.text_input('Jitter_DDP')
   with col1:
       MDVP_Shimmer = st.text_input('MDVP_Shimmer')
   with col2:
       MDVP_Shimmer_dB = st.text_input('MDVP_Shimmer(dB)')
   with col3:
       Shimmer_APQ3 = st.text_input('Shimmer_APQ3')
   with col4:
       Shimmer_APQ5 = st.text_input('Shimmer_APQ5')
   with col1:
       MDVP_APQ = st.text_input('MDVP_APQ')
   with col2:
       Shimmer_DDA = st.text_input('Shimmer_DDA')
   with col3:
       NHR = st.text_input('NHR')
   with col4:
       HNR = st.text_input('HNR')
   with col1:
       RPDE = st.text_input('RPDE')
   with col2:
       DFA = st.text_input('DFA')
   with col3:
       spread1 = st.text_input('spread1')
   with col4:
       spread2 = st.text_input('spread2')
   with col1:
       D2 = st.text_input('D2')
   with col2:
       PPE = st.text_input('PPE')
       
       parkinsons_diagnosis = ''
       if st.button('Parkinsons Test Result'):
           user_input=[MDVP_Fo_Hz,MDVP_Fhi_Hz,MDVP_Flo_Hz,MDVP_Jitter_percent , MDVP_Jitter_Abs ,MDVP_RAP , MDVP_RAP_percent ,Jitter_DDP , MDVP_Shimmer ,MDVP_Shimmer_dB ,Shimmer_APQ3 , Shimmer_APQ5 , MDVP_APQ , Shimmer_DDA, NHR, HNR, RPDE,DFA , spread1 , spread2 ,D2 , PPE]
           user_input =[float (x)  for x in user_input]
           parkinson_prediction = parkinson_model.predict([user_input])
           if parkinson_prediction[0] == 1:
               parkinsons_diagnosis= 'The person has Parkinson'
           else:
               diab_diagnosis = 'The person does not have Parkinson'
           st.success(parkinsons_diagnosis)
       
# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal')

    # code for Prediction
    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_model.predict([user_input])
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
        st.success(heart_diagnosis)