# In-Every-Sip-a-Prediction
# 🍷 Wine Quality Prediction using Machine Learning

> *"Every bottle tells a story. This project uses Machine Learning to predict it."*

## Overview

Wine quality is traditionally evaluated through sensory analysis by experienced tasters. This project leverages Machine Learning to classify red wine as **Good Quality** or **Bad Quality** based on its physicochemical properties.

A **Random Forest Classifier** is trained on the Wine Quality dataset and deployed using **Streamlit**, providing an interactive web application for real-time predictions.

---

## Project Objective

The objective of this project is to build an end-to-end Machine Learning application that:

- Predicts wine quality using physicochemical features
- Classifies wines into Good or Bad quality
- Provides an intuitive interface for user interaction
- Demonstrates the complete ML workflow from data preprocessing to deployment

---

## Dataset

The dataset contains **11 physicochemical features** and **1 target variable**.

### Input Features

- Fixed Acidity
- Volatile Acidity
- Citric Acid
- Residual Sugar
- Chlorides
- Free Sulfur Dioxide
- Total Sulfur Dioxide
- Density
- pH
- Sulphates
- Alcohol

### Target Variable

The original quality score ranges from **0 to 10**.

For this project:

- **Good Quality Wine:** Quality ≥ 7
- **Bad Quality Wine:** Quality < 7

---

## Machine Learning Pipeline

- Data Loading
- Data Preprocessing
- Feature Selection
- Binary Classification
- Train-Test Split
- Model Training
- Model Evaluation
- Streamlit Deployment

---

## Model

**Algorithm Used**

- Random Forest Classifier

**Evaluation Metric**

- Accuracy Score

---

## Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit

---

## Project Structure

```text
Wine-Quality-Prediction/
│── app.py
│── winequality-red.csv
│── requirements.txt
│── README.md
```

---

## Key Features

- Interactive Streamlit Interface
- Real-Time Predictions
- Clean and Simple User Experience
- Binary Wine Quality Classification
- Random Forest-Based Prediction Model

---

## Future Enhancements

- Hyperparameter Optimization
- Model Comparison with Other Algorithms
- Feature Importance Visualization
- Explainable AI (SHAP)
- Model Serialization
- Cloud Deployment Enhancements

---

## Conclusion

This project demonstrates how Machine Learning can be applied to solve a real-world classification problem. By combining data preprocessing, model training, evaluation, and deployment into a single application, it provides a complete example of an end-to-end Machine Learning workflow.

---

## Author

**Spartoon Lite**

*If you found this project useful, consider giving it a ⭐ on GitHub.*
