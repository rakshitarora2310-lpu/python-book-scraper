import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def generate_synthetic_data(num_samples=500):
    """Generates synthetic e-commerce/service customer retention data."""
    np.random.seed(42)
    
    tenure_months = np.random.randint(1, 48, size=num_samples)
    monthly_charges = np.round(np.random.uniform(20.0, 120.0, size=num_samples), 2)
    support_calls = np.random.randint(0, 7, size=num_samples)
    
    # Logic: Lower tenure + higher monthly charge + more support calls = higher churn probability
    churn_prob = (0.5 - (tenure_months / 100) + (monthly_charges / 300) + (support_calls / 10))
    churn = (churn_prob > 0.6).astype(int)
    
    data = pd.DataFrame({
        "Tenure_Months": tenure_months,
        "Monthly_Charges_$": monthly_charges,
        "Support_Calls": support_calls,
        "Churn": churn
    })
    return data

def run_churn_prediction_pipeline():
    print("🤖 Running Customer Churn Prediction Machine Learning Pipeline...\n")
    
    # 1. Prepare Dataset
    df = generate_synthetic_data()
    X = df[["Tenure_Months", "Monthly_Charges_$", "Support_Calls"]]
    y = df["Churn"]
    
    # 2. Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 3. Model Training
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    
    # 4. Model Evaluation
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"✅ Model Training Complete. Test Accuracy: {accuracy * 100:.2f}%\n")
    
    # 5. Predict on New Live Customer Profiles
    print("🔮 Predicting Churn Risk for New Sample Customers:")
    new_customers = pd.DataFrame([
        {"Customer": "Customer A", "Tenure_Months": 3, "Monthly_Charges_$": 115.00, "Support_Calls": 5},
        {"Customer": "Customer B", "Tenure_Months": 36, "Monthly_Charges_$": 45.00, "Support_Calls": 1},
        {"Customer": "Customer C", "Tenure_Months": 12, "Monthly_Charges_$": 85.00, "Support_Calls": 4}
    ])
    
    features = new_customers[["Tenure_Months", "Monthly_Charges_$", "Support_Calls"]]
    predictions = model.predict(features)
    probabilities = model.predict_proba(features)[:, 1]
    
    results = new_customers.copy()
    results["Churn_Prediction"] = ["🚨 HIGH RISK" if pred == 1 else "✅ RETAINED" for pred in predictions]
    results["Churn_Probability"] = [f"{prob * 100:.1f}%" for prob in probabilities]
    
    print(results.to_string(index=False))

if __name__ == "__main__":
    run_churn_prediction_pipeline()