# 🩺 Blood Pressure Risk Predictor

A lightweight machine learning web application built with **Flask** and **Scikit-learn** that predicts whether a person is at risk of high blood pressure based on their **age** and **blood pressure reading**.

---

## 🚀 Demo

> Enter your age and blood pressure value — the model instantly tells you if you're at risk.

| Input | Valid Range |
|---|---|
| Age | 0 – 120 |
| Blood Pressure (mmHg) | 50 – 300 |

---

## 🧠 How It Works

1. On startup, a **Logistic Regression** model is trained on `data.csv` (501 labeled records).
2. Missing values are imputed using column means.
3. Class imbalance is handled via `class_weight="balanced"`.
4. A user submits Age + Blood Pressure via a web form.
5. The model returns a binary prediction: **"You have BP"** or **"You don't have BP"**.

```
User Input → Validation → Logistic Regression Model → Prediction Result
```

---

## 🗂️ Project Structure

```
prediction/
├── main.py              # Flask app + ML model training & prediction
├── data.csv             # Training dataset (501 samples)
└── templates/
    └── index.html       # Jinja2 frontend template
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| Web Framework | Flask |
| Machine Learning | Scikit-learn (Logistic Regression) |
| Data Processing | Pandas, NumPy |
| Frontend | HTML, CSS, Jinja2 |

---

## 🛠️ Getting Started

### Prerequisites

Make sure you have **Python 3.8+** installed.

### 1. Clone the Repository

```bash
git clone https://github.com/nqtexd/Basic-BP-Predictor.git
cd Basic-BP-Predictor
```

### 2. Install Dependencies

```bash
pip install flask scikit-learn pandas numpy
```

### 3. Run the App

```bash
python main.py
```

The server will start at **`http://127.0.0.1:5000`**

> **Note:** The CSV path in `main.py` is set to `prediction/data.csv`. If you're running from inside the `prediction/` folder, update line 31 to just `"data.csv"`.

---

## 📊 Dataset

The training data (`data.csv`) contains **501 records** with the following columns:

| Column | Description |
|---|---|
| `age` | Patient's age (integer) |
| `blood_pressure` | Systolic blood pressure reading (integer) |
| `result` | `1` = has BP, `0` = no BP |

---

## ✅ Input Validation

The app validates all user input before making a prediction:

- **Age** must be between `0` and `120` — otherwise an alert is shown.
- **Blood Pressure** must be between `50` and `300` — otherwise an alert is shown.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

Made with ❤️ by **[Your Name](https://github.com/your-username)**
