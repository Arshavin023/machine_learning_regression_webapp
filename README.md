# Student Math Score Prediction Web App
![ML Pipeline](https://img.shields.io/badge/Machine_Learning-Regression-blue)
![Python](https://img.shields.io/badge/Python-3.10+-yellow)
![Flask](https://img.shields.io/badge/Web_App-Flask-lightgrey)
![Docker](https://img.shields.io/badge/Container-Docker-blue)
![CI/CD](https://img.shields.io/badge/CI/CD-GitHub%20Actions-green)

![System Architecture](images/ml_architecture.png)

---

## Overview
A **production-ready Machine Learning regression pipeline** that predicts student math scores based on demographic and academic factors. This project transitioned from experimental notebooks to a **modular Python architecture**, with:

- Automated data ingestion and transformation  
- Multi-model training & evaluation (**Scikit-Learn**, **XGBoost**, **CatBoost**)  
- Flask-based web interface for real-time predictions  
- Fully automated **CI/CD pipeline** for testing, staging, and deployment  
- Containerized deployment with **Docker**  

---

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [CI/CD & Deployment](#cicd--deployment)
- [Modular Components](#modular-components)
- [Authors & Acknowledgements](#authors--acknowledgements)
- [License](#license)

---

## Introduction <a name="introduction"></a>
The **Math Score Prediction Web App** analyzes student demographics, parental education, test preparation, and other features to forecast math performance.  
It ensures **consistent preprocessing, model training, and prediction** through a custom Python pipeline and provides a **real-time web interface** for inference.  

---

## Project Structure <a name="project-structure"></a>
```text
├── .github/workflows/       # CI/CD pipelines (Test → Staging → Deployment)
├── artifacts/               # Serialized models (.pkl) & datasets
├── images/                  # Documentation & diagrams
├── infra/                   # Infrastructure as Code (Terraform)
├── notebook/                # EDA and model experimentation notebooks
│   └── data/                # Raw datasets for research
├── src/                     # Core source code
│   ├── components/          # Data ingestion, transformation, training
│   ├── pipeline/            # Prediction and training pipelines
│   ├── templates/           # Flask HTML frontend
│   ├── logger.py            # Custom execution logging
│   ├── exception.py         # Standardized error handling
│   ├── utils.py             # Helper functions (model saving/loading)
│   └── app.py               # Flask application entry point
├── tests/                   # Unit & integration tests
├── Dockerfile               # Containerization configuration
├── requirements.txt         # Python dependencies
└── setup.py                 # Package metadata

```

---

## 📦 Tech Stack

- **Language:** Python 3.10+
- **Web Framework:** Flask 
- **ML Frameworks:** Scikit-Learn, XGBoost, CatBoost
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Logging & Monitoring:** Python Logging Module
- **Dev Tools:** Swagger, Git, VSCode, Linux

---


## 📖 Getting Started
### Installation <a name="installation"></a>
#### Prerequisites <a name="prerequisites"></a>
Before running this repo, ensure you have the following prerequisites installed:
- Python 3.8+

### 1. Clone the Repo <a name="Clone the Repo"></a>
```bash
git clone https://github.com/Arshavin023/machine_learning_regression_webapp.git
cd machine_learning_regression_webapp
```

### 2. Create and Activate Virtual Environment <a name="create and activate virtual environment"></a>
```bash
python3 -m venv ml_venv
source ml_venv/bin/activate  # On Windows: ml_venv\Scripts\activate
pip install -e .
```

### 3. Install Python Packages <a name="Install the required Python packages"></a>
```bash
pip install -r requirements.txt
```

### 4. Usage <a name="usage"></a>
#### a. Run Training Pipeline <a name=" Ingestion, transformation, and model selection process"></a>
```bash
python3 src/components/data_ingestion.py
```
#### b. Run Flask Web App <a name="Run Web App Locally"></a>
```bash
python3 src/app.py
```

### 5. CI/CD & Deployment <a name="cicd--deployment"></a>
```bash
# Build Docker image
docker build -t math-score-app:latest .
# Push to Your Docker Hub
docker tag math-score-app:latest <your_dockerhub_username>/math-score-app:latest
docker push <your_dockerhub_username>/math-score-app:latest
# Pull & Run on server
docker pull <your_dockerhub_username>/math-score-app:latest
docker run -d -p 1759:8000 math-score-app:latest
```

## Modular Components <a name="modular-components"></a>
- Data Ingestion & Transformation → Handles raw data and prepares it for modeling
- Model Training & Evaluation → Trains multiple models and selects the best
- Prediction Pipeline → Standardizes input, predicts, and returns results
- Web Interface (Flask) → Allows users to input data and get real-time predictions

## Authors & Acknowledgements <a name="authors--acknowledgements"></a>
- Developed by Uche Nnodim
- Inspired by best practices in ML pipelines, Flask deployment, and CI/CD automation

## License <a name="license"></a>
- MIT License