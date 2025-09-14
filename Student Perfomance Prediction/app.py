import streamlit as st
import numpy as np
import joblib
import warnings

warnings.filterwarnings("ignore")

# Load Model
model = joblib.load("final_model.pkl")

# Page Title
st.title("📊 Exam Score Predictor")
st.info("💡 This tool predicts exam scores based on study habits, attendance, mental health, sleep, and part-time job status.")

# --- Layout: Split sliders into two columns ---
col1, col2 = st.columns(2)

with col1:
    study_hours = st.slider("📚 Study Hours per Day", 0.0, 12.0, 2.0)
    attendance = st.slider("📝 Attendance Percentage", 0.0, 100.0, 80.0)

with col2:
    mental_health = st.slider("🧠 Mental Health Rating [1-10]", 1, 10, 5)
    sleep_hours = st.slider("😴 Sleep Hours per Night", 0.0, 12.0, 7.0)

# Part-time Job Input (Radio for better UX)
part_time_job = st.radio("💼 Do you have a Part-Time Job?", ["Yes", "No"])
ptj_encoded = 1 if part_time_job == "Yes" else 0

# --- Prediction Button ---
if st.button("🔮 Predict Exam Score"):
    # Prepare input
    input_data = np.array([[study_hours, attendance, mental_health, sleep_hours, ptj_encoded]])
    prediction = model.predict(input_data)[0]
    prediction = np.clip(prediction, 0, 100)  # Ensure score stays in [0, 100]

    # Show Result
    st.subheader("📈 Prediction Result")
    st.metric("Predicted Exam Score", f"{prediction:.2f}")

    # Progress Bar
    st.progress(int(prediction))

    # Feedback Messages
    if prediction >= 75:
        st.success("🌟 Great! You're likely to perform very well. Keep it up!")
    elif prediction >= 50:
        st.warning("⚠️ You’re on track, but more study hours and consistency can boost your score.")
    else:
        st.error("❌ Risk of low performance. Try improving attendance & study time for better results.")
