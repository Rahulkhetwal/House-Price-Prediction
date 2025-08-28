# 🏡 House Price Prediction

Predict house prices with high accuracy using machine learning and XGBoost!  
This project provides a complete pipeline: from data cleaning and feature engineering to model training and a user-friendly Streamlit web app for instant predictions.

---

## 🚀 Features

- **Data Preprocessing:** Handles missing values, encodes categorical features, and removes highly correlated columns.
- **Model Training:** Uses XGBoost Regressor for robust and accurate predictions.
- **Interactive Web App:** Enter house features and get instant price predictions.
- **Visualization:** Correlation heatmaps and feature analysis included in the notebook.
- **Easy Deployment:** Ready for Streamlit Cloud or local use.

---

## 📊 Example

![Correlation Heatmap Example](https://raw.githubusercontent.com/Rahulkhetwal/House-Price-Prediction/main/images/output.png)
*Visualize feature relationships before model training.*

---

## 🛠️ How to Use

### 1. Clone the Repository
```sh
git clone https://github.com/Rahulkhetwal/House-Price-Prediction.git
cd House-Price-Prediction
```

### 2. Install Requirements
```sh
pip install -r requirements.txt
```

### 3. Run the Streamlit App
```sh
streamlit run app.py
```
Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📝 Project Structure

- `app.ipynb` — Data cleaning, EDA, feature engineering, and model training.
- `app.py` — Streamlit web app for predictions.
- `XGBhouseprice_model.jb` — Trained XGBoost model.
- `requirements.txt` — All dependencies for easy setup.

---

## ✨ Demo

Try the live app: [house-price-prediction11.streamlit.app](https://house-price-prediction11.streamlit.app)

---

## 📥 Input Features

- OverallQual, GrLivArea, GarageArea, 1stFlrSF, FullBath, YearBuilt, YearRemodAdd, MasVnrArea, Fireplaces, BsmtFinSF1, LotFrontage, WoodDeckSF, OpenPorchSF, LotArea, CentralAir

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the MIT License.

---

> **Made with ❤️ by [Rahulkhetwal](https://github.com/Rahulkhetwal)**