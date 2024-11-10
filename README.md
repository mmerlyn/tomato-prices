# tomato-prices

## A tool that predicts the prices of tomato crops in Karnataka based on market conditions

### Problem Statement

Analysis of tomato prices in Karnataka from 2016 to 2018/4

- It is heartbreaking to learn that farmers in India sometimes have to let their harvests rot in the field, due to low market prices.
- This is more commonly seen in tomato harvests, whre during some particular months, due to very low market prices, the cost of harvesting and transporting is higher than the expected return.
- Hence most farmers let the fruits to rot/throw them on roads, let cattle eat them, etc.
- This problem is due to the supply demand imbalance, where increase in supply, reduces demand, leading to low prices.
- Using machine learning techniques, we can predict the expected price for tomatoes, at a particular market, when supply is a certain number of tonnes.
- This knowledge, can help farmers, plan ahead, and may be opt for a different crop, if the predicted selling price is low.

Application demonstration:

- https://quartz14.github.io/Tomato-Prices/

### Files:

- Price of Tomato Karnataka(2016-2018).csv file contains the raw data obtained from Kaggle URL: https://www.kaggle.com/vinayreddy4034/vegetablepricetomato
- The modified data is stored in monthly_tomato.csv file
- Tomato2 is a python notebook containing the data exploration, analysis and visualizations, to identify trends in data
- monthly_tomato notebook contains the machine learning part of code
- monthly_gbr_model3 is the pickled machine learning model obtained from monthly_tomato notebook
- The tomato_app file is the web page made from flask. It uses the HTML files in templates. Templates can be found in the templates branch
- monthly_tomato_app file is a flask app that uses the pickled model to predict the prices.
  The Templates branch contains 2 html files: 1) monthly_tomato_home - Home page that takes in user inputs Month, Market Area, Average Tonnes per month for that market 2) tomato_result - Displays the predicted values
- Requirements contains the python libraries required to run the program
