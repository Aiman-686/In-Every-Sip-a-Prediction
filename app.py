import numpy as np
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Wine Quality Prediction",
    page_icon="🍷",
    layout="centered"
)

# ------------------ LOAD DATA ------------------
wine_df = pd.read_csv("winequality-red.csv")

# ------------------ PREPARE DATA ------------------
X = wine_df.drop("quality", axis=1)
y = wine_df["quality"].apply(lambda x: 1 if x >= 7 else 0)

# ------------------ SPLIT DATA ------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=3
)

# ------------------ TRAIN MODEL ------------------
model = RandomForestClassifier(random_state=3)
model.fit(X_train, y_train)

# ------------------ MODEL ACCURACY ------------------
accuracy = accuracy_score(y_test, model.predict(X_test))

# ------------------ UI ------------------
st.title("🍷 Wine Quality Prediction")
st.write("Predict whether a wine is **Good** or **Bad** based on its physicochemical properties.")

st.info(f"Model Accuracy: **{accuracy:.2%}**")

st.markdown("### Enter Wine Features")

col1, col2 = st.columns(2)

with col1:
    fixed_acidity = st.number_input("Fixed Acidity", value=7.4)
    volatile_acidity = st.number_input("Volatile Acidity", value=0.70)
    citric_acid = st.number_input("Citric Acid", value=0.00)
    residual_sugar = st.number_input("Residual Sugar", value=1.90)
    chlorides = st.number_input("Chlorides", value=0.076)
    free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", value=11.0)

with col2:
    total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", value=34.0)
    density = st.number_input("Density", value=0.9978, format="%.4f")
    ph = st.number_input("pH", value=3.51)
    sulphates = st.number_input("Sulphates", value=0.56)
    alcohol = st.number_input("Alcohol", value=9.4)

# ------------------ PREDICTION ------------------
if st.button("🍷 Predict Wine Quality"):

    features = np.array([[
        fixed_acidity,
        volatile_acidity,
        citric_acid,
        residual_sugar,
        chlorides,
        free_sulfur_dioxide,
        total_sulfur_dioxide,
        density,
        ph,
        sulphates,
        alcohol
    ]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("✅ Good Quality Wine")
        st.balloons()
    else:
        st.error("❌ Bad Quality Wine")