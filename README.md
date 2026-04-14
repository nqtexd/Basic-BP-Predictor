# 🩺 BP-Predictor: ML-Powered Health Insight

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/framework-Flask-lightgrey.svg)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange.svg)

[cite_start]An intuitive web application that leverages **Logistic Regression** to predict high blood pressure based on user demographics and vitals. [cite_start]Built with a Flask backend and a responsive frontend, this project demonstrates a complete end-to-end Machine Learning pipeline.

---

## 🌟 Key Features

**Intelligent Prediction:** Utilizes a `LogisticRegression` model with `class_weight="balanced"` to handle data distribution effectively.
**Automated Data Cleaning:** The system automatically fills missing values in the dataset with the column mean during the training phase.
**Input Guardrails:** Server-side validation ensures age inputs are between 0–120 and blood pressure readings are between 50–300.
**Dynamic UI:** Displays results with color-coded alerts—Red for "You have BP!" and Green for "You dont have BP!".

---

## 🛠️ Technology Stack

| Component | Technology |
| :--- | :--- |
| **Language** | [cite_start]Python 3.x  |
| **Web Framework** | [cite_start]Flask  |
| **Data Analysis** | [cite_start]Pandas, NumPy  |
| **Machine Learning** | [cite_start]Scikit-Learn  |
| **Frontend** | [cite_start]HTML5, CSS3, Jinja2  |

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have the following libraries installed:
```bash
pip install flask pandas numpy scikit-learn
