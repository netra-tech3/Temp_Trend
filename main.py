from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the model
model = joblib.load('model.pkl')

# Load the dataset for display purposes
data = pd.read_csv('Agrofood_co2_emission.csv')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get data from form
        data = request.form.to_dict()
        df = pd.DataFrame([data])
        
        # Convert data types as necessary
        for column in df.columns:
            df[column] = pd.to_numeric(df[column])
        
        # Make prediction
        prediction = model.predict(df)[0]
        
        return render_template('prediction_result.html', prediction=prediction)
    
    return render_template('predict.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/prediction_result')
def prediction_result():
    return render_template('prediction_result.html')

@app.route('/solutions')
def solutions():
    return render_template('solutions.html')


@app.route('/data')
def data_page():
    df = pd.read_csv('Agrofood_co2_emission.csv')
    
    # Filter the data for India
    india_data = df[df['Area'] == 'India']
    
    # Convert the filtered data to an HTML table
    india_data_html = india_data.to_html(classes='table table-striped')
    
    return render_template('data.html', tables=[india_data_html])

if __name__ == '__main__':
    app.run(debug=True)
