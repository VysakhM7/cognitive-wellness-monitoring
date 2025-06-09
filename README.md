🧠 Cognitive Wellness Monitoring System

This project explores how data-driven tools can support individuals experiencing cognitive or memory-related challenges—such as older adults or those in the early stages of dementia—by analyzing user behavior, health trends, and safety events.

🎯 Project Objectives

The system is designed to:

- Promote independence by assisting users in maintaining daily routines (medication, hydration, physical activity) through automated reminders.

- Support caregivers with alerts and summaries based on the user's interactions and health data, helping them make timely decisions.

- Ensure safety by detecting critical incidents like falls or abnormal vitals, allowing early interventions that may prevent complications.

- Provide insights through exploratory data analysis (EDA) to understand behavioral patterns and relationships between physical health and engagement.

By addressing these objectives, the project contributes to the growing need for compassionate, scalable support systems in aging societies—where many families face the challenge of ensuring safety and well-being for their loved ones without constant supervision.

📁 Datasets Used

- **daily_reminder.csv** – Contains logs of reminders including type, timing, delivery status, and user acknowledgment.

- **health_monitoring.csv** – Includes heart rate, blood pressure, glucose levels, oxygen saturation, and alerts when values exceed thresholds.

- **safety_monitoring.csv** – Contains data related to movement, falls, impact severity, and inactivity after falls.

---

### Summary of Approach

- Combined and cleaned data from multiple sources, handling missing values and dropping irrelevant columns.

- Engineered binary features such as `Missed_Reminder`, `Vitals_Abnormal`, and `Fall_Event` per patient.

- Aggregated features per patient ID to create a summary dataset for modeling.

- Defined a target variable `Has_Disorder` based on thresholds of abnormal vitals or fall events.

- Trained a Random Forest classifier to predict likelihood of cognitive disorders.

- Evaluated the model using train/test split and cross-validation, achieving perfect or near-perfect accuracy on this dataset.

- Identified feature importances, with `Fall_Event` being the most significant predictor.

- Saved the trained model for potential future deployment.

This workflow illustrates how combining health and behavioral monitoring data can support early identification of cognitive health risks, contributing to safer and more independent living.

---

### Application link

- https://cognitivewellnessmonitor.streamlit.app/

### Future plan

- Associate with hospitals. I am already in talks with some of them.

- Use their real time data to train the model better and help them to foresee cognitive issues in their patients who consult with other departments.
