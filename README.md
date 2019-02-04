# Directional Predictor for XAU_USD pair

GET request initiated to oanda API instrument endpoint, subsequently fed to functions in oandadata.py to calculate SMA and EMA.

Main program utilises a Machine Learning Method, K-Nearest-Neighbours on a dataset of XAU-USD over 5 years to predict the directional change of XAU-USD in a week's time and at the end of the calendar month.
An accuracy of 80.5% and 84.5% were achieved on a cross-validation set of size 20% for the week and end-of-month prediction.

This is also my first code on GitHub.