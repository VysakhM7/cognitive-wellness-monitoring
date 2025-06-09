{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "beae2a67-28d6-4597-8236-14f72236e7dc",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-06-10 00:45:18.683 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\shara\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import joblib\n",
    "\n",
    "# Load model\n",
    "model = joblib.load(\"random_forest_model.pkl\")\n",
    "\n",
    "# App title\n",
    "st.title(\"🧠 Cognitive Health Risk Predictor\")\n",
    "\n",
    "st.markdown(\"\"\"\n",
    "This app analyzes patient health and safety data to **predict risk of cognitive issues**, supporting early detection and caregiver action.\n",
    "\"\"\")\n",
    "\n",
    "# Upload CSV\n",
    "uploaded_file = st.file_uploader(\"Upload a CSV file with patient data\", type=\"csv\")\n",
    "\n",
    "if uploaded_file:\n",
    "    data = pd.read_csv(uploaded_file)\n",
    "\n",
    "    # Check required columns\n",
    "    expected_cols = ['Missed_Reminder', 'Vitals_Abnormal', 'Fall_Event', \n",
    "                     'Health_Alerts_Notified', 'Safety_Alerts_Notified']\n",
    "    \n",
    "    if all(col in data.columns for col in expected_cols):\n",
    "        # Predict\n",
    "        predictions = model.predict(data[expected_cols])\n",
    "        data['Predicted_Disorder'] = predictions\n",
    "\n",
    "        # Display results\n",
    "        st.subheader(\"Predicted Patients with Cognitive Issues\")\n",
    "        st.write(data[data['Predicted_Disorder'] == 1][['Device-ID/User-ID']])\n",
    "\n",
    "        # Optionally download results\n",
    "        csv = data.to_csv(index=False).encode('utf-8')\n",
    "        st.download_button(\"Download Full Results\", csv, \"predictions.csv\", \"text/csv\")\n",
    "    else:\n",
    "        st.error(\"Uploaded file is missing required columns.\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
