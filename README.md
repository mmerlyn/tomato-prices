# Analysis of Tomato Prices in Karnataka

## 📈 A tool that predicts the prices of tomato crops in Karnataka based on market conditions

This project analyzes tomato prices in Karnataka from 2016 to 2018 and forecasts future prices using a machine learning model. The motivation comes from the challenges faced by farmers when market prices drop so low that harvesting becomes unprofitable.

[🌐 Demo](https://drive.google.com/file/d/15CCHZwvlRhmBjlY5jUqNidPYYGhNCo3c/view?usp=sharing) 

### Problem Statement

Analysis of tomato prices in Karnataka from 2016 to 2018/4

- It is heartbreaking to learn that farmers in India sometimes have to let their harvests rot in the field, due to low market prices.
- This is more commonly seen in tomato harvests, where during some particular months, due to very low market prices, the cost of harvesting and transporting is higher than the expected return.
- Hence most farmers let the fruits to rot/throw them on roads, let cattle eat them, etc.
- This problem is due to the supply demand imbalance, where increase in supply, reduces demand, leading to low prices.
- Using machine learning techniques, we can predict the expected price for tomatoes, at a particular market, when supply is a certain number of tonnes.
- This knowledge, can help farmers, plan ahead, and may be opt for a different crop, if the predicted selling price is low.

### Machine Learning Approach

- A **Gradient Boosting Regression** model was used to forecast monthly tomato prices based on supply data.
- Achieved **~80% accuracy**.
- Developed a **Flask web application** that allows users to input expected monthly supply and get predicted prices for different market areas.

---

## 📂 Files Overview

| File | Description |
|------|-------------|
| `Price of Tomato Karnataka (2016–2018).csv` | Raw dataset sourced from [Kaggle](https://www.kaggle.com/vinayreddy4034/vegetablepricetomato) |
| `monthly_tomato.csv` | Cleaned and preprocessed dataset |
| `Tomato2.ipynb` | Data exploration, analysis, and visualizations |
| `monthly_tomato.ipynb` | Machine learning model building |
| `monthly_gbr_model3.pkl` | Pickled machine learning model obtained from monthly_tomato notebook |
| `tomato_app/` | Flask web app for demo interface |
| `templates/` | HTML templates used by the Flask app |
| `requirements.txt` | List of Python libraries required to run the app |

---

The Templates branch contains 2 html files: 
1. monthly_tomato_home - Home page that takes in user inputs Month, Market Area, Average Tonnes per month for that market 
2. tomato_result - Displays the predicted values

## Working

- **Data Preprocessing:** Cleaned and aggregated supply and price data on a monthly basis.
- **Model Training:** Used Gradient Boosting to predict price from features like month, supply (tonnes), and market location.
- **Visualization:** Insightful plots help understand seasonal and regional price trends.
- **Web Interface:** Built with Flask. Users input month, market, and average tonnes — the app returns a predicted price.

## 🛠 Technologies Used

- **Python**, **Pandas**, **NumPy**
- **Matplotlib**, **Seaborn** (for data visualization)
- **Scikit-learn**, **Gradient Boosting Regression**
- **Flask** (for web app)

## Results

- **Training Accuracy:** ~80%
- Price trends were learned well from structured data, but could be further improved with real-time or external market variables (e.g., weather, demand indicators).

## Learnings

- Importance of matching real-world domain knowledge with machine learning.
- Effective preprocessing and feature engineering dramatically improve performance.
- Flask is a powerful tool to rapidly deploy ML models for real-world users.



