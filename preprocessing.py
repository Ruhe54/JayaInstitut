import joblib
import numpy as np
import pandas as pd

scaler_Admission = joblib.load("model/scaler_Admission_grade.joblib")
scaler_Age = joblib.load("model/scaler_Age_at_enrollment.joblib")
scaler_App_Mode = joblib.load("model/scaler_Application_mode.joblib")
scaler_App_Order = joblib.load("model/scaler_Application_order.joblib")
scaler_Course = joblib.load("model/scaler_Course.joblib")
scaler_1st_Approved = joblib.load("model/scaler_Curricular_units_1st_sem_approved.joblib")
scaler_1st_Credited = joblib.load("model/scaler_Curricular_units_1st_sem_credited.joblib")
scaler_1st_Enrolled = joblib.load("model/scaler_Curricular_units_1st_sem_enrolled.joblib")
scaler_1st_Eval = joblib.load("model/scaler_Curricular_units_1st_sem_evaluations.joblib")
scaler_1st_Grade = joblib.load("model/scaler_Curricular_units_1st_sem_grade.joblib")
scaler_1st_Without_Eval = joblib.load("model/scaler_Curricular_units_1st_sem_without_evaluations.joblib")
scaler_2nd_Approved = joblib.load("model/scaler_Curricular_units_2nd_sem_approved.joblib")
scaler_2nd_Credited = joblib.load("model/scaler_Curricular_units_2nd_sem_credited.joblib")
scaler_2nd_Enrolled = joblib.load("model/scaler_Curricular_units_2nd_sem_enrolled.joblib")
scaler_2nd_Eval = joblib.load("model/scaler_Curricular_units_2nd_sem_evaluations.joblib")
scaler_2nd_Grade = joblib.load("model/scaler_Curricular_units_2nd_sem_grade.joblib")
scaler_2nd_Without_Eval = joblib.load("model/scaler_Curricular_units_2nd_sem_without_evaluations.joblib")
scaler_Daytime_Eve_Attendance = joblib.load("model/scaler_Daytime_evening_attendance.joblib")
scaler_Debtor = joblib.load("model/scaler_Debtor.joblib")
scaler_Displaced = joblib.load("model/scaler_Displaced.joblib")
scaler_Edu_Special_Need = joblib.load("model/scaler_Educational_special_needs.joblib")
scaler_Father_Occupation = joblib.load("model/scaler_Fathers_occupation.joblib")
scaler_Father_Qualification = joblib.load("model/scaler_Fathers_qualification.joblib")
scaler_GDP = joblib.load("model/scaler_GDP.joblib")
scaler_Gender = joblib.load("model/scaler_Gender.joblib")
scaler_Inflation = joblib.load("model/scaler_Inflation_rate.joblib")
scaler_International = joblib.load("model/scaler_International.joblib")
scaler_Marital_status = joblib.load("model/scaler_Marital_status.joblib")
scaler_Mother_occupation = joblib.load("model/scaler_Mothers_occupation.joblib")
scaler_Mother_qualification = joblib.load("model/scaler_Mothers_qualification.joblib")
scaler_Nacionality = joblib.load("model/scaler_Nacionality.joblib")
scaler_Prev_qual = joblib.load("model/scaler_Previous_qualification.joblib")
scaler_Prev_qual_grade = joblib.load("model/scaler_Previous_qualification_grade.joblib")
scaler_Scholarship = joblib.load("model/scaler_Scholarship_holder.joblib")
scaler_Tuition = joblib.load("model/scaler_Tuition_fees_up_to_date.joblib")
scaler_Unemployment_rate = joblib.load("model/scaler_Unemployment_rate.joblib")
model = joblib.load("model/rdf_model.joblib")
result_target = joblib.load("model/encoder_target.joblib")


def data_preprocessing(data):

    data = data.copy()
    df = pd.DataFrame()

    df["Marital_status"] = scaler_Marital_status.transform(np.asarray(data["Marital_status"]).reshape(-1, 1))[0]
    df["Application_mode"] = scaler_App_Mode.transform(np.asarray(data["Application_mode"]))
    df["Application_order"] = scaler_App_Order.transform(np.asarray(data["Application_order"]).reshape(-1, 1))[0]
    df["Course"] = scaler_Course.transform(np.asarray(data["Course"]).reshape(-1, 1))[0]
    df["Daytime_evening_attendance"] = scaler_Daytime_Eve_Attendance.transform(np.asarray(data["Daytime_evening_attendance"]).reshape(-1, 1))[0]
    df["Previous_qualification"] = scaler_Prev_qual.transform(np.asarray(data["Previous_qualification"]).reshape(-1, 1))[0]
    df["Previous_qualification_grade"] = scaler_Prev_qual_grade.transform(np.asarray(data["Previous_qualification_grade"]).reshape(-1, 1))[0]
    df["Nacionality"] = scaler_Nacionality.transform(np.asarray(data["Nacionality"]).reshape(-1, 1))[0]
    df["Mothers_qualification"] = scaler_Mother_qualification.transform(np.asarray(data["Mothers_qualification"]).reshape(-1, 1))[0]
    df["Fathers_qualification"] = scaler_Father_Qualification.transform(np.asarray(data["Fathers_qualification"]).reshape(-1, 1))[0]
    df["Mothers_occupation"] = scaler_Mother_occupation.transform(np.asarray(data["Mothers_occupation"]).reshape(-1, 1))[0]
    df["Fathers_occupation"] = scaler_Father_Occupation.transform(np.asarray(data["Fathers_occupation"]).reshape(-1, 1))[0]
    df["Admission_grade"] = scaler_Admission.transform(np.asarray(data["Admission_grade"]).reshape(-1, 1))[0]
    df["Displaced"] = scaler_Displaced.transform(np.asarray(data["Displaced"]).reshape(-1, 1))[0]
    df["Educational_special_needs"] = scaler_Edu_Special_Need.transform(np.asarray(data["Educational_special_needs"]).reshape(-1, 1))[0]
    df["Debtor"] = scaler_Debtor.transform(np.asarray(data["Debtor"]).reshape(-1, 1))[0]
    df["Tuition_fees_up_to_date"] = scaler_Tuition.transform(np.asarray(data["Tuition_fees_up_to_date"]).reshape(-1, 1))[0]
    df["Gender"] = scaler_Gender.transform(np.asarray(data["Gender"]).reshape(-1, 1))[0]
    df["Scholarship_holder"] = scaler_Scholarship.transform(np.asarray(data["Scholarship_holder"]).reshape(-1, 1))[0]
    df["Age_at_enrollment"] = scaler_Age.transform(np.asarray(data["Age_at_enrollment"]).reshape(-1, 1))[0]
    df["International"] = scaler_International.transform(np.asarray(data["International"]).reshape(-1, 1))[0]
    df["Curricular_units_1st_sem_credited"] = scaler_1st_Credited.transform(np.asarray(data["Curricular_units_1st_sem_credited"]).reshape(-1, 1))[0]
    df["Curricular_units_1st_sem_enrolled"] = scaler_1st_Enrolled.transform(np.asarray(data["Curricular_units_1st_sem_enrolled"]).reshape(-1, 1))[0]
    df["Curricular_units_1st_sem_evaluations"] = scaler_1st_Eval.transform(np.asarray(data["Curricular_units_1st_sem_evaluations"]).reshape(-1, 1))[0]
    df["Curricular_units_1st_sem_approved"] = scaler_1st_Approved.transform(np.asarray(data["Curricular_units_1st_sem_approved"]).reshape(-1, 1))[0]
    df["Curricular_units_1st_sem_grade"] = scaler_1st_Grade.transform(np.asarray(data["Curricular_units_1st_sem_grade"]).reshape(-1, 1))[0]
    df["Curricular_units_1st_sem_without_evaluations"] = scaler_1st_Without_Eval.transformdf(np.asarray(data["Curricular_units_1st_sem_without_evaluations"]).reshape(-1, 1))[0]
    df["Curricular_units_2nd_sem_credited"] = scaler_2nd_Credited.transform(np.asarray(data["Curricular_units_2nd_sem_credited"]).reshape(-1, 1))[0]
    df["Curricular_units_2nd_sem_enrolled"] = scaler_2nd_Enrolled.transform(np.asarray(data["Curricular_units_2nd_sem_enrolled"]).reshape(-1, 1))[0]
    df["Curricular_units_2nd_sem_evaluations"] = scaler_2nd_Eval.transform(np.asarray(data["Curricular_units_2nd_sem_evaluations"]).reshape(-1, 1))[0]
    df["Curricular_units_2nd_sem_approved"] = scaler_2nd_Approved.transform(np.asarray(data["Curricular_units_2nd_sem_approved"]).reshape(-1, 1))[0]
    df["Curricular_units_2nd_sem_grade"] = scaler_2nd_Grade.transform(np.asarray(data["Curricular_units_2nd_sem_grade"]).reshape(-1, 1))[0]
    df["Curricular_units_2nd_sem_without_evaluations"] = scaler_2nd_Without_Eval.transform(np.asarray(data["Curricular_units_2nd_sem_without_evaluations"]).reshape(-1, 1))[0]
    df["Unemployment_rate"] = scaler_Unemployment_rate.transform(np.asarray(data["Unemployment_rate"]).reshape(-1, 1))[0]
    df["Inflation_rate"] = scaler_Inflation.transform(np.asarray(data["Inflation_rate"]).reshape(-1, 1))[0]
    df["GDP"] = scaler_GDP.transform(np.asarray(data["GDP"]).reshape(-1, 1))[0]

    return df


def prediction(data):

    result = model.predict(data)
    final_result = result_target.inverse_transform(result)[0]
    return final_result

