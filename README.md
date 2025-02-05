# End-to-End Machine Learning Project

## 📌 Overview

This project demonstrates the **complete lifecycle of a machine learning application**, from **data collection to deployment using Flask**. The goal is to build a **structured, modular, and scalable** machine learning pipeline while following best practices.

## 📖 Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Dataset](#dataset)
- [Technologies and Libraries Used](#technologies-and-libraries-used)
- [Machine Learning Models Used](#machine-learning-models-used)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Running Tests](#running-tests)

---

## 📂 Project Structure

```plaintext
End_to_End_ML_project/
├── artifacts/                 # Directory for storing intermediate artifacts
├── catboost_info/             # Information related to CatBoost model training
├── logs/                      # Log files generated during execution
├── mlproject.egg-info/        # Package metadata
├── notebook/                  # Jupyter notebooks for experimentation
├── src/                       # Source code for the project
│   ├── __init__.py            # Initializes the src module
│   ├── components/            # Modular components of the pipeline
│   ├── pipeline/              # Scripts to run the ML pipeline
│   ├── utils/                 # Utility functions
├── templates/                 # HTML templates for web application
├── tests/                     # Unit tests for the project
├── .gitignore                 # Specifies files to ignore in version control
├── README.md                  # Project documentation
├── app.py                     # Flask application for model deployment
├── requirements.txt           # List of project dependencies
└── setup.py                   # Setup script for packaging
```

---

## 🚀 Features

✔ **Data Ingestion**: Automatically fetches and preprocesses data.  
✔ **Data Preprocessing**: Handles missing values, feature engineering, and transformations.  
✔ **Model Selection & Training**: Implements various machine learning models.  
✔ **Model Evaluation**: Uses **cross-validation, RMSE, and R2 score** to assess models.  
✔ **Web Deployment**: Provides a **Flask-based web interface** for model inference.  
✔ **Logging & Monitoring**: Implements logging to track pipeline performance.

---

## 📊 Dataset

The dataset used in this project is **"Student Performance in Exams"**, which contains student exam scores along with various features.

### **Features:**

- **Gender**: Male/Female
- **Race/Ethnicity**: Group A, B, C, D, E
- **Parental Education**: Highest education level of parents
- **Lunch Type**: Free/Reduced or Standard
- **Test Preparation Course**: Completed or Not
- **Math Score** (Target Variable)
- **Reading Score**
- **Writing Score**

📌 **Target:** Predicting **Math Score** based on other student attributes.

---

## 🛠️ Technologies and Libraries Used

**Programming:**

- Python 3.9.5

**Libraries & Frameworks:**

- **Machine Learning:** Scikit-Learn, CatBoost
- **Data Processing:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Web Framework:** Flask
- **Logging:** Python Logging Module
- **Version Control:** Git

---

## 🤖 Machine Learning Models Used

The following **ML models** were trained and evaluated:

1️⃣ **Linear Regression** – Baseline model to predict math scores.  
2️⃣ **Decision Tree Regressor** – A non-linear model to capture interactions.  
3️⃣ **Random Forest Regressor** – An ensemble method for better generalization.  
4️⃣ **Gradient Boosting (GBM)** – Boosted trees for improved accuracy.  
5️⃣ **CatBoost Regressor** – Best-performing model with auto-handling of categorical features.

---

## ⚙️ Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/sidhu7777/End_to_End_ML_project.git
   cd End_to_End_ML_project
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

### 🔹 Running the Application

1. **Start the Flask application**:

   ```bash
   python app.py
   ```

2. **Access the application** at `http://localhost:5000`.

### 🔹 Running Tests

1. **Execute unit tests**:
   ```bash
   pytest tests/
   ```

---

🎯 **This project is designed for individuals looking to learn and implement end-to-end machine learning solutions.** Happy Coding! 🚀
