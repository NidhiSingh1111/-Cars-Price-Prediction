# -Cars-Price-Prediction

# 🚗 Car Price Prediction Web App

A machine learning-powered web application that predicts the resale price of a used car based on user inputs like brand, model, fuel type, year, and more. The app is built using **Flask**, **Python**, and **a trained regression model**, and features a user-friendly interface.

---

## 🧠 Project Overview

In the automotive industry, accurate pricing is crucial for both buyers and sellers. This project aims to build a predictive model that estimates car prices using a dataset of historical sales and specifications.

### 📊 Problem Statement

Build a machine learning model that:
- Takes car specifications as input
- Predicts the **estimated resale price** of the vehicle
- Provides an easy-to-use interface for users to test predictions

---

## 🚀 Features

- Predict resale prices of used cars instantly
- Dropdown inputs for vehicle make, model, year, fuel type, transmission, etc.
- Trained machine learning model (regression)
- Built using Flask and deployed on Render
- Clean, responsive UI

---

## 🛠️ Tech Stack

- **Python**
- **Flask** (web framework)
- **Pandas**, **NumPy** (data preprocessing)
- **Scikit-learn** (model training and prediction)
- **Pickle** (model serialization)
- **HTML/CSS** (frontend)
- **Render** (deployment)

## 🔍 How It Works

1. Data is collected, cleaned, and processed from a CSV file (`car_data.csv`)
2. A regression model is trained using features like:
   - Company
   - Model
   - Year of purchase
   - Fuel type
   - Transmission
   - Mileage
3. The model is saved using `pickle`
4. User selects input values from dropdowns on the web page
5. The model predicts the estimated price and displays it instantly

🌐 Live Demo
Check it out live here: https://cars-price-prediction-ejhx.onrender.com



 

