from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)

# Load your model
heart_model = joblib.load('Heart_Attack')
diabetes_model = joblib.load('Diabetes_predictor')
diamond_model = joblib.load('Diamond_Price_Predictor_LGBMr')

@app.route('/')
def default():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve input from form and create DataFrame
        input_data = {
            'Age': [float(request.form['age'])],
            'Gender': [int(request.form['gender'])],
            'Heart rate': [float(request.form['heart_rate'])],
            'Systolic blood pressure': [int(request.form['systolic_bp'])],
            'Diastolic blood pressure': [int(request.form['diastolic_bp'])],
            'Blood sugar': [float(request.form['blood_sugar'])],
            'CK-MB': [float(request.form['ckmb'])],
            'Troponin': [float(request.form['troponin'])]
        }

        input_df = pd.DataFrame(input_data)
        prediction = heart_model.predict(input_df)

        result = "At Risk" if prediction[0] == 1 else "Not at Risk"
        return render_template('heart_attack.html', prediction_text=f"{result}")

    except Exception as e:
        return render_template('heart_attack.html', prediction_text=f"Error: {str(e)}")


@app.route('/predict_diabetes', methods=['POST'])
def predict_diabetes():
    try:
        # Retrieve input from form and create DataFrame
        input_data = {
            'Pregnancies': [int(request.form['pregnancies'])],
            'Glucose': [float(request.form['glucose'])],
            'BloodPressure': [float(request.form['blood_pressure'])],
            'SkinThickness': [float(request.form['skin_thickness'])],
            'Insulin': [float(request.form['insulin'])],
            'BMI': [float(request.form['bmi'])],
            'DiabetesPedigreeFunction': [float(request.form['diabetes_pedigree_function'])],
            'Age': [int(request.form['age'])]
        }

        input_df = pd.DataFrame(input_data)
        prediction = diabetes_model.predict(input_df)

        result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"
        return render_template('diabetes.html', prediction_text=f"{result}")

    except Exception as e:
        return render_template('diabetes.html', prediction_text=f"Error: {str(e)}")

@app.route('/predict_diamond', methods=['POST'])
def predict_diamond():
    try:
        # Retrieve input from form and create DataFrame
        input_data = {
            					
            'carat': [float(request.form['carat'])],
            'cut': [int(request.form['cut'])],
            'color': [int(request.form['color'])],
            'clarity': [int(request.form['clarity'])],
            'depth': [float(request.form['depth'])],
        }

        input_df = pd.DataFrame(input_data)
        prediction = diamond_model.predict(input_df)
        result = prediction * 87.69        

        prediction = round(float(prediction[0]))
        result = round(float(result[0]))
        usd = '$'
        inr = 'rs'



        return render_template('diamond.html', prediction_text=f"{ usd, prediction, inr, result }")

    except Exception as e:
        return render_template('diamond.html', prediction_text=f"Error: {str(e)}")


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/no_project')
def no_project():
    return render_template('no_project.html')

@app.route('/heart_attack')
def heart_attack():
    return render_template('heart_attack.html')

@app.route('/about_heart_attack')
def about_heart_attack():
    return render_template('about_project/about_heart_attack.html')

@app.route('/diabetes')
def diabetes():
    return render_template('diabetes.html')

@app.route('/about_diabetes')
def about_diabetes():
    return render_template('about_project/about_diabetes.html')

@app.route('/water')
def water():
    return render_template('water.html')

@app.route('/about_water')
def about_water():
    return render_template('about_project/about_water.html')

@app.route('/diamond')
def diamond():
    return render_template('diamond.html')

@app.route('/about_diamond')
def about_diamond():
    return render_template('about_project/about_diamond.html')


if __name__ == "__main__":
    app.run(debug=True)