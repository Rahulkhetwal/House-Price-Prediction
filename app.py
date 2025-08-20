import pandas as pd
import streamlit as st
import joblib

# Load the model
model = joblib.load('XGBhouseprice_model.jb')
st.title('House Price Prediction')
st.write('Enter the features of the house to predict its price')

# Input fields for the features (use a list to preserve order)
features = [
    'OverallQual', 'GrLivArea', 'GarageArea', '1stFlrSF',
    'FullBath', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'Fireplaces',
    'BsmtFinSF1', 'LotFrontage', 'WoodDeckSF', 'OpenPorchSF', 'LotArea',
    'CentralAir'
]

input_data = {}
for feature in features:
    if feature == 'CentralAir':
        input_data[feature] = st.selectbox(feature, ['Yes', 'No'], index=0)
    else:
        input_data[feature] = st.number_input(
            f"{feature}",
            value=0.0,
            step=1.0 if feature in ['OverallQual', 'FullBath', 'Fireplaces'] else 0.01
        )

if st.button('Predict price'):

    # Convert input data to DataFrame
    input_data['CentralAir'] = 1 if input_data['CentralAir'] == 'Yes' else 0
    input_df = pd.DataFrame([input_data], columns=features)
    
    # Make prediction
    prediction = model.predict(input_df)
    st.write(f"The predicted price of the house is: ${prediction[0]:,.2f}")