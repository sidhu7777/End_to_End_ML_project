
# End-to-End Machine Learning Project

## Overview

This project guides you through the complete lifecycle of a machine learning application, from initial setup to deployment. The primary objective is to build a structured and modular codebase that facilitates the development and deployment of machine learning models.

## Project Structure

```
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

## Features

1. **Data Ingestion**: Scripts to load and validate data from various sources.
2. **Data Preprocessing**: Handling missing values, feature engineering, and scaling.
3. **Model Training**: Training machine learning models with hyperparameter tuning.
4. **Model Evaluation**: Assessing model performance using appropriate metrics.
5. **Model Deployment**: Deploying the trained model using a Flask web application.
6. **Logging and Monitoring**: Implementing logging to monitor the pipeline's performance.

## Installation

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

## Usage

### Running the Application

1. **Start the Flask application**:
   ```bash
   python app.py
   ```

2. **Access the application** at `http://localhost:5000`.

### Training the Model

1. **Navigate to the source directory**:
   ```bash
   cd src/pipeline
   ```

2. **Run the training script**:
   ```bash
   python train_pipeline.py
   ```

### Running Tests

1. **Execute unit tests**:
   ```bash
   pytest tests/
   ```

