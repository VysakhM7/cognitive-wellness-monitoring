import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("random_forest_model.pkl")

# App title
st.title("🧠 Cognitive Health Risk Predictor")

st.markdown("""
This app analyzes patient health and safety data to **predict risk of cognitive issues**, 
supporting early detection and caregiver action.
""")

# File upload
uploaded_file = st.file_uploader("Upload a CSV file with patient data", type="csv")

if uploaded_file:
    data = pd.read_csv(uploaded_file)

    expected_cols = [
        'Missed_Reminder', 'Vitals_Abnormal', 'Fall_Event',
        'Health_Alerts_Notified', 'Safety_Alerts_Notified'
    ]

    if all(col in data.columns for col in expected_cols):
        predictions = model.predict(data[expected_cols])
        data['Predicted_Disorder'] = predictions

        st.subheader("Patients Predicted to Have Cognitive Issues")
        st.write(data[data['Predicted_Disorder'] == 1][['Device-ID/User-ID']])

        csv = data.to_csv(index=False).encode('utf-8')
        st.download_button("Download Full Results", csv, "predictions.csv", "text/csv")
    else:
        st.error("Uploaded file is missing required columns.")
