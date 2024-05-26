from flask import Flask, request, render_template
import pickle
import pandas as pd
import xgboost as xgb

app = Flask(__name__)

model = xgb.Booster(model_file='model_file_name.json') 

@app.route('/')
def home():
    return render_template('index.html', data={})

@app.route('/predict', methods=['POST'])

def predict():
    # Get input data as a dictionary from the form
    data = request.form.to_dict()
    
    # Convert values to float
    data = {k: float(v) for k, v in data.items()}
    
    # Convert dictionary to Pandas DataFrame
    df = pd.DataFrame([data])
    
    # Convert DataFrame to DMatrix
    data_dmatrix = xgb.DMatrix(df)
    
    # Make predictions
    prediction = model.predict(data_dmatrix)
    
    # Interpret the prediction
    result = 'Failure' if prediction[0] == 1 else 'No Failure'
    
    # Render the template with the prediction result and original data
    return render_template('index.html', prediction_text=f'Prediction: {result}', data=data)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
