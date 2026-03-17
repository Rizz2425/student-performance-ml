# Student Performance Prediction System 🎓🤖

A full-stack Machine Learning application that predicts whether a student will pass or fail based on their academic habits and attendance.

## 🚀 Project Overview
This project demonstrates the complete lifecycle of a Machine Learning product:
1. **Model Training:** Logistic Regression model trained on Google Colab.
2. **Backend:** Django web framework to handle user inputs and model predictions.
3. **Cloud Deployment:** Hosted on an **Azure Virtual Machine (Ubuntu)** for global access.

## 🛠️ Tech Stack
- **Machine Learning:** Python, Scikit-learn, Pandas, NumPy
- **Backend:** Django
- **Model Serialization:** Pickle
- **Deployment:** Microsoft Azure (VM), Gunicorn
- **Tools:** VS Code, Git/GitHub, Google Colab

## 📊 Model Features
The classification model uses the following features to predict the outcome:
* **Study Hours:** Number of hours spent studying daily.
* **Attendance:** Percentage of classes attended.
* **Previous Score:** Last academic performance record.

## 📁 Project Structure
```text
├── predictor/             # Django App for prediction logic
│   ├── templates/         # HTML UI (index.html)
│   ├── views.py           # Logic to load .pkl and predict
│   └── urls.py            # App-level routing
├── student_predictor/     # Main Django Project settings
├── student_model.pkl      # The Trained ML Model (Pickle file)
├── manage.py              # Django CLI
└── requirements.txt       # Project dependencies


⚙️ How It Works
Input: User provides academic data through a web form.

Processing: The Django backend captures the data and passes it to the student_model.pkl file.

Output: The model performs binary classification and returns "Pass" or "Fail" to the UI.

🌐 Deployment Details
The application is successfully deployed on an Azure VM.

Server: Ubuntu 22.04 LTS

Access: Public IP via Port 8000

Scaling: Uses a Virtual Environment for dependency isolation.

🧑‍💻 Author
Rizwan Ahmed Data Engineer Trainee
