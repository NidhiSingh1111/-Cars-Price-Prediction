import pandas as pd
import numpy as np
import pickle
import openpyxl
from flask import Flask, render_template, request, redirect
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
model = pickle.load(open('Linear_Regression_Model.pkl', 'rb'))
car = pd.read_excel('car_data.xlsx')


@app.route('/', methods=['GET', 'POST'])
def index():
    vehicle = sorted(car['Vehicle_Type'].unique())
    company = sorted(car['Company'].unique())
    vehicle_model = sorted(car['Vehicle_Name'].astype(str).unique())
    year = sorted(car['Year'].unique(), reverse=True)
    fuel_type = sorted(car['Fuel_Type'].unique())
    seller_type = sorted(car['Seller_Type'].unique())
    transmission = sorted(car['Transmission'].unique())

    vehicle_model.insert(0, 'Select Company Vehicle Model')
    return render_template('index.html', vehicle=vehicle, company=company, vehicle_model=vehicle_model, year=year,
                           fuel_type=fuel_type, seller_type=seller_type, transmission=transmission, data=car)


@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    try:
        vehicle = request.form.get('vehicle')
        company = request.form.get('company')
        vehicle_model = request.form.get('vehicle_model')
        year = int(request.form.get('year'))
        present_price = float(request.form.get('present_price'))
        kms_driven = int(request.form.get('kms_driven'))
        fuel_type = request.form.get('fuel_type')
        seller_type = request.form.get('seller_type')
        transmission = request.form.get('transmission')
        owner = int(request.form.get('owner'))

        prediction = pd.DataFrame(
            columns=['Vehicle_Type', 'Company', 'Vehicle_Name', 'Year', 'Present_Price', 'Kms_Driven',
                     'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner'],
            data=np.array([vehicle, company, vehicle_model, year, present_price, kms_driven, fuel_type, seller_type, transmission,
                 owner]).reshape(1, 10))

        predictions = model.predict(prediction)
        predicted_price = np.round(predictions[0], 2)
        print("Predictions:", predicted_price)

        if predicted_price < 0:
            return " Invalid Specifications"

        return str(predicted_price)


    except Exception as e:
        print("Error during predictions:", e)
        return "Error during predictions:" + str(e)


if __name__ == '__main__':
    app.run()
