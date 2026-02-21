💳 Online Payments Fraud Detection Using Machine Learning
📌 Project Overview

Online payment fraud is increasing rapidly with the growth of digital transactions. This project uses Machine Learning techniques to detect fraudulent transactions and classify them as Fraud or Legitimate.

The system analyzes transaction data and predicts whether a payment is suspicious based on different features.

🎯 Objective

To build a machine learning model that detects fraudulent online payments.

To reduce financial loss by identifying suspicious transactions.

To improve transaction security using predictive analytics.

📂 Dataset

The dataset contains transaction details such as:

Transaction Type

Amount

Old Balance

New Balance

Destination Account

Transaction Time

The target variable:

1 → Fraud

0 → Legitimate

⚙️ Technologies Used

Python

Pandas

NumPy

Scikit-learn

Matplotlib

Seaborn

Flask (for web application)

🔄 Project Workflow

Data Collection
Collected online payment transaction dataset.

Data Preprocessing

Handling missing values

Encoding categorical variables

Feature scaling

Exploratory Data Analysis (EDA)

Univariate analysis

Bivariate analysis

Multivariate analysis

Model Building & Training

Decision Tree

Random Forest

Logistic Regression

Model Evaluation

Accuracy

Confusion Matrix

Classification Report

Model Deployment

Saved model using Pickle

Integrated with Flask web application

📊 Model Performance

The Random Forest model achieved better accuracy compared to other models and was selected for deployment.

🚀 How to Run the Project

Clone the repository:

git clone https://github.com/your-username/your-repo-name.git

Install required libraries:

pip install -r requirements.txt

Run the Flask app:

python app.py

Open in browser:

http://127.0.0.1:5000/
📌 Future Improvements

Use Deep Learning models

Implement real-time fraud detection

Deploy on cloud platforms

Improve model accuracy with feature engineering
