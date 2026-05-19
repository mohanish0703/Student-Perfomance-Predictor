

# 🎓 Student Performance Predictor

An end-to-end Machine Learning project that predicts students' academic performance based on demographic and socio-economic factors — built with **Python**, **Scikit-learn**, and **Jupyter Notebook**.

---

## 📸 App Preview

![Student Performance Predictor](https://raw.githubusercontent.com/mohanish0703/Student-Perfomance-Predictor/main/Student%20Perfomance%20Prediction/screenshot.png)

---

## 📌 Overview

This project builds a machine learning pipeline to predict a student's exam score based on factors such as gender, parental education level, lunch type, and test preparation course completion. It covers the full ML lifecycle — data exploration, preprocessing, model training, evaluation, and a web-based prediction interface.

---

## 🎯 Objectives

- Perform Exploratory Data Analysis (EDA) to understand how various factors affect student performance
- Preprocess and engineer features for model training
- Train and compare multiple regression/classification models
- Evaluate models using appropriate metrics (R², RMSE, Accuracy)
- Deploy an interactive web app for real-time predictions

---

## 🗂️ Repository Structure

```
Student-Perfomance-Predictor/
│
└── Student Perfomance Prediction/
    ├── student_performance.ipynb   # Main Jupyter Notebook (EDA + ML pipeline)
    ├── app.py                      # Flask / Streamlit web application
    ├── model.pkl                   # Serialised trained model
    ├── dataset.csv                 # Student performance dataset
    ├── screenshot.png              # Web app preview
    └── requirements.txt            # Python dependencies
│
└── README.md
```

> **Note:** Update this structure to match your exact files if any differ.

---

## 🛠️ Tech Stack

| Tool / Library | Purpose |
|----------------|---------|
| **Python 3.x** | Core programming language |
| **Pandas / NumPy** | Data manipulation and analysis |
| **Matplotlib / Seaborn** | Data visualisation and EDA |
| **Scikit-learn** | ML models, preprocessing, evaluation |
| **Flask / Streamlit** | Web application for predictions |
| **Jupyter Notebook** | Development and experimentation |
| **Pickle** | Model serialisation |

---

## 📊 ML Pipeline

### 1. 🔍 Exploratory Data Analysis
- Distribution of scores across gender, ethnicity, and parental education
- Correlation heatmaps between features
- Identifying outliers and missing values

### 2. 🧹 Data Preprocessing
- Handling categorical variables with One-Hot Encoding / Label Encoding
- Feature scaling using StandardScaler
- Train-test split (80/20)

### 3. 🤖 Models Trained
| Model | Description |
|-------|-------------|
| Linear Regression | Baseline regression model |
| Ridge Regression | Regularised linear model |
| Lasso Regression | Feature selection via L1 penalty |
| Decision Tree | Non-linear tree-based model |
| Random Forest | Ensemble of decision trees |
| Gradient Boosting | Sequential boosting approach |

### 4. 📈 Evaluation Metrics
- **R² Score** — Variance explained by the model
- **Mean Absolute Error (MAE)**
- **Root Mean Squared Error (RMSE)**

---

## 📁 Dataset

The dataset contains information about students including:

| Feature | Description |
|---------|-------------|
| `gender` | Student's gender (male / female) |
| `race_ethnicity` | Ethnic group (Group A–E) |
| `parental_level_of_education` | Parent's highest education level |
| `lunch` | Lunch type (standard / free/reduced) |
| `test_preparation_course` | Whether the student completed prep course |
| `math_score` | Math exam score (0–100) |
| `reading_score` | Reading exam score (0–100) |
| `writing_score` | Writing exam score (0–100) |

---

## 🔍 Key Insights

- Students who completed the **test preparation course** scored significantly higher across all subjects
- **Parental education level** has a positive correlation with student scores
- **Standard lunch** students outperform those on free/reduced lunch
- **Female students** tend to score higher in reading and writing; males in math
- Scores across math, reading, and writing are **highly correlated** with each other

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/mohanish0703/Student-Perfomance-Predictor.git
cd Student-Perfomance-Predictor/Student\ Perfomance\ Prediction/
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Jupyter Notebook
```bash
jupyter notebook student_performance.ipynb
```

### 4. Launch the Web App
```bash
# For Flask
python app.py

# For Streamlit
streamlit run app.py
```

Then open your browser at `http://localhost:5000` (Flask) or `http://localhost:8501` (Streamlit).

---

## 👤 Author

**Mohanish**  
B.Tech Computer Science & Engineering  
Vellore Institute of Technology (VIT)  
[GitHub Profile](https://github.com/mohanish0703)
