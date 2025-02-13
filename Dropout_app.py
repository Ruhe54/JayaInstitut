import streamlit as st
import pandas as pd
from preprocessing import prediction, data_preprocessing

col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png", width=130)
with col2:
    st.header('Status Prediction App (Prototype)')

data = pd.DataFrame()

col1, col2, col3 = st.columns(3)

with col1:
    Marital_status = int(st.number_input(label="Marital_status"))
    data["Marital_status"] = [Marital_status]

with col2:
    Application_mode = int(st.number_input(label="Application_mode"))
    data["Application_mode"] = [Application_mode]

with col3:
    Application_order = int(st.number_input(label="Application_order"))
    data["Application_order"] = Application_order

col1, col2, col3 = st.columns(3)

with col1:
    Course = int(st.number_input(label='Course', value=0))
    data["Course"] = Course

with col2:
    Daytime_evening_attendance = int(st.number_input(label='Daytime_evening_attendance', value=0))
    data["Daytime_evening_attendance"] = Daytime_evening_attendance

with col3:
    Previous_qualification = int(st.number_input(label='Previous_qualification', value=0))
    data["Previous_qualification"] = Previous_qualification


col1, col2, col3 = st.columns(3)

with col1:
    Previous_qualification_grade = int(st.number_input(label='Previous_qualification_grade', value=0))
    data["Previous_qualification_grade"] = Previous_qualification_grade

with col2:
    Nacionality = int(st.number_input(label='Nacionality', value=0))
    data["Nacionality"] = Nacionality

with col3:
    Admission_grade = float(st.number_input(label='Admission_grade', value=0))
    data["Admission_grade"] = Admission_grade


col1, col2, col3, col4 = st.columns(4)

with col1:
    Mothers_qualification = float(st.number_input(label='Mothers_qualification', value=0))
    data["Mothers_qualification"] = Mothers_qualification

with col2:
    Mothers_occupation = float(st.number_input(label='Mothers_occupation', value=0))
    data["Mothers_occupation"] = Mothers_occupation

with col3:
    Fathers_qualification = float(st.number_input(label='Fathers_qualification', value=0))
    data["Fathers_qualification"] = Fathers_qualification

with col4:
    Fathers_occupation = float(st.number_input(label='Fathers_occupation', value=0))
    data["Fathers_occupation"] = Fathers_occupation

col1, col2, col3 = st.columns(3)

with col1:
    Displaced = int(st.number_input(label='Displaced', value=0))
    data["Displaced"] = Displaced

with col2:
    Educational_special_needs = int(st.number_input(label='Educational_special_needs', value=0))
    data["Educational_special_needs"] = Educational_special_needs

with col3:
    Debtor = float(st.number_input(label='Debtor', value=0))
    data["Debtor"] = Debtor

col1, col2, col3, col4 = st.columns(4)

with col1:
    Tuition_fees_up_to_date = float(st.number_input(label='Tuition_fees_up_to_date', value=0))
    data["Tuition_fees_up_to_date"] = Tuition_fees_up_to_date

with col2:
    Gender = float(st.number_input(label='Gender', value=0))
    data["Gender"] = Gender

with col3:
    Scholarship_holder = float(st.number_input(label='Scholarship_holder', value=0))
    data["Scholarship_holder"] = Scholarship_holder

with col4:
    Age_at_enrollment = float(st.number_input(label='Age_at_enrollment', value=0))
    data["Age_at_enrollment"] = Age_at_enrollment

col1, col2, col3, col4 = st.columns(4)

with col1:
    International = float(st.number_input(label='International', value=0))
    data["International"] = International

with col2:
    Unemployment_rate = float(st.number_input(label='Unemployment_rate', value=0))
    data["Unemployment_rate"] = Unemployment_rate

with col3:
    Inflation_rate = float(st.number_input(label='Inflation_rate', value=0))
    data["Inflation_rate"] = Inflation_rate

with col4:
    GDP = float(st.number_input(label='GDP', value=0))
    data["GDP"] = GDP

col1, col2, col3 = st.columns(3)

with col1:
    Curricular_units_1st_sem_credited = float(st.number_input(label='Curricular_units_1st_sem_credited', value=0))
    data["Curricular_units_1st_sem_credited"] = Curricular_units_1st_sem_credited

with col2:
    Curricular_units_1st_sem_enrolled = float(st.number_input(label='Curricular_units_1st_sem_enrolled', value=0))
    data["Curricular_units_1st_sem_enrolled"] = Curricular_units_1st_sem_enrolled

with col3:
    Curricular_units_1st_sem_evaluations = float(st.number_input(label='Curricular_units_1st_sem_evaluations', value=0))
    data["Curricular_units_1st_sem_evaluations"] = Curricular_units_1st_sem_evaluations

col1, col2, col3 = st.columns(3)

with col1:
    Curricular_units_1st_sem_approved = float(st.number_input(label='Curricular_units_1st_sem_approved', value=0))
    data["Curricular_units_1st_sem_approved"] = Curricular_units_1st_sem_approved

with col2:
    Curricular_units_1st_sem_grade = float(st.number_input(label='Curricular_units_1st_sem_grade', value=0))
    data["Curricular_units_1st_sem_grade"] = Curricular_units_1st_sem_grade

with col3:
    Curricular_units_1st_sem_without_evaluations = float(st.number_input(label='Curricular_units_1st_sem_without_evaluations', value=0))
    data["Curricular_units_1st_sem_without_evaluations"] = Curricular_units_1st_sem_without_evaluations

col1, col2, col3 = st.columns(3)

with col1:
    Curricular_units_2nd_sem_credited = float(st.number_input(label='Curricular_units_2nd_sem_credited', value=0))
    data["Curricular_units_2nd_sem_credited"] = Curricular_units_2nd_sem_credited

with col2:
    Curricular_units_2nd_sem_enrolled = float(st.number_input(label='Curricular_units_2nd_sem_enrolled', value=0))
    data["Curricular_units_2nd_sem_enrolled"] = Curricular_units_2nd_sem_enrolled

with col3:
    Curricular_units_2nd_sem_evaluations = float(st.number_input(label='Curricular_units_2nd_sem_evaluations', value=0))
    data["Curricular_units_2nd_sem_evaluations"] = Curricular_units_2nd_sem_evaluations

col1, col2, col3 = st.columns(3)

with col1:
    Curricular_units_2nd_sem_approved = float(st.number_input(label='Curricular_units_2nd_sem_approved', value=0))
    data["Curricular_units_2nd_sem_approved"] = Curricular_units_2nd_sem_approved

with col2:
    Curricular_units_2nd_sem_grade = float(st.number_input(label='Curricular_units_2nd_sem_grade', value=0))
    data["Curricular_units_2nd_sem_grade"] = Curricular_units_2nd_sem_grade

with col3:
    Curricular_units_2nd_sem_without_evaluations = float(st.number_input(label='Curricular_units_2nd_sem_without_evaluations', value=0))
    data["Curricular_units_2nd_sem_without_evaluations"] = Curricular_units_2nd_sem_without_evaluations


with st.expander("View the Raw Data"):
    st.dataframe(data=data, width=800, height=10)

if st.button('Predict'):
    new_data = data_preprocessing(data=data)
    with st.expander("View the Preprocessed Data"):
        st.dataframe(data=new_data, width=800, height=10)
    st.write("Credit Scoring: {}".format(prediction(new_data)))
