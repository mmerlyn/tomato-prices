# 🍅 Analysis of Tomato Prices in Karnataka

This project analyzes tomato prices in Karnataka from 2016 to 2018 and forecasts future prices using a machine learning model. The aim is to help farmers make informed decisions about crop planning and sales based on historical pricing patterns and supply trends.

[🌐 Demo](https://drive.google.com/file/d/15CCHZwvlRhmBjlY5jUqNidPYYGhNCo3c/view?usp=sharing) 

## 💡 Motivation & Impact

Analysis of tomato prices in Karnataka from 2016 to 2018/4

- It is heartbreaking to learn that farmers in India sometimes have to let their harvests rot in the field, due to low market prices.
- This is more commonly seen in tomato harvests, where during some particular months, due to very low market prices, the cost of harvesting and transporting is higher than the expected return.
- Hence most farmers let the fruits to rot/throw them on roads, let cattle eat them, etc.
- This problem is due to the supply demand imbalance, where increase in supply, reduces demand, leading to low prices.
- Using machine learning techniques, we can predict the expected price for tomatoes, at a particular market, when supply is a certain number of tonnes.
- This knowledge, can help farmers, plan ahead, and may be opt for a different crop, if the predicted selling price is low.

## 🛠 Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn (Gradient Boosting)
- Matplotlib, Seaborn (Visualization)
- Flask (Web application)
- HTML/CSS (UI)

## Approach

- **Data Preprocessing:** Cleaned and processed supply and price data on a monthly basis.
- **Model Training:** Used Gradient Boosting Regression (Scikit-learn) to predict price from features like  Month, Market Area, Supply (Tonnes), Min/Max Prices (optional).
- **Visualization:** Insightful plots help understand seasonal and regional price trends.
- **Web Interface:** Built with Flask. Users input month, market, and average tonnes — the app returns a predicted price.

## 📊 Key Insights from the Data

- Most markets receive ~60 tonnes/month — prices crash when supply exceeds this.
- **Kolar market** is the largest and most influential in the dataset.
- Price is highly sensitive to small changes in supply.
- Modal, Max, and Min prices are **~80% correlated**, making price prediction easier but less robust.
- Identical supply quantities can yield different prices across markets and dates - indicating market inefficiency.

## 📈 Results

- ✅ **Training Score**: 99%  
- ✅ **Test Score**: 98% (when including Max/Min prices — which are strongly correlated to target)

- ❗ **Realistic Model (without Max/Min features)**:
  - Training Score: 83%
  - Test Score: 65%
  - RMSE: ₹320

Including external variables like weather, pest activity, or market access could improve real-world performance.

## 🌐 Web Application

A Flask-based interface allows users to input:
- Month
- Market area
- Estimated supply (in tonnes)

The app returns a **predicted price**, allowing farmers and analysts to assess profitability.

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

The Templates branch contains 2 html files: 
1. monthly_tomato_home - Home page that takes in user inputs Month, Market Area, Average Tonnes per month for that market 
2. tomato_result - Displays the predicted values

## Learnings

- How to apply machine learning to a real-world problem with practical impact  
- The importance of cleaning and preparing data to improve model accuracy  
- Some input features (like max/min prices) can give very high accuracy, but don't always reflect real-world conditions  
- Building a simple web interface with Flask helps users easily try out our model

## Future Work

- Add real-time data like weather or pest alerts to improve prediction  
- Recommend better months or markets for selling produce  
- Visualize trends in a more interactive way (dashboards or maps)  
- Help farmers estimate profits for different harvest levels 

## 📜 License
© All rights reserved.  
This project was completed as part of the Project-Based Learning (PBL) contest at **BMS Institute of Technology and Management**, Bengaluru, India.

**Team Members:**
1. Merlyn Mercylona Maki Reddy  
2. Aishwarya M



