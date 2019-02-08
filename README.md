# Directional Predictor for XAU_USD pair

GET request initiated to oanda API instrument endpoint, subsequently fed to functions in oandadata.py to calculate SMA and EMA.

Main program utilises Machine Learning Methods, LOGISTIC REGRESSION and CLASSIFICATION AND REGRESSION TREES on a dataset of XAU-USD over 5 years to predict the directional change of XAU-USD in a week's(7 candles) time and month's(30 days) time.
An accuracy of 80.0% and 88.4% were achieved on a cross-validation set of size 20% for the week and end-of-month prediction.

Insert API key in oandadata.py.

This is also my first code on GitHub.