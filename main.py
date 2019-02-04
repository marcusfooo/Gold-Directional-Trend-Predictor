import pandas as pd
from sklearn import model_selection
from sklearn.neighbors import KNeighborsClassifier
from oandadata import SMA
from oandadata import EMA
from oandadata import today


# Load dataset
def load_data():
    week_dataset = pd.read_csv('week-dataset.csv')
    week_dataset.fillna(week_dataset.median(), inplace=True)
    month_dataset = pd.read_csv('month-dataset.csv')
    month_dataset.fillna(month_dataset.median(), inplace=True)

    # Split dataset
    week_x = week_dataset.iloc[:, 1:13]
    week_y = week_dataset.iloc[:, 0]
    month_x = month_dataset.iloc[:, 1:13]
    month_y = month_dataset.iloc[:, 0]
    validation_size = 0.20
    seed = 7

    # Use only training data
    x_weektrain, x_validation, y_weektrain, y_validation = model_selection.train_test_split(week_x, week_y, test_size=validation_size, random_state=seed)
    x_monthtrain, x_validation, y_monthtrain, y_validation = model_selection.train_test_split(month_x, month_y, test_size=validation_size, random_state=seed)
    return x_weektrain, y_weektrain, x_monthtrain, y_monthtrain


# Loading in value for prediction
def load_x():

    new_x = {

        'OPEN': [today()[0]],
        'CLOSE': [today()[1]],
        'MA20': [SMA(20)],
        '20CLOSE': [],
        'MA60': [SMA(60)],
        '60CLOSE': [],
        'MA200': [SMA(200)],
        '200CLOSE': [],
        '20-60': [],
        '20-200': [],
        '60-200': [],
        'EMA20': [EMA(20)],

    }
    if float(new_x['MA20'][0]) > float(new_x['CLOSE'][0]):
        new_x['20CLOSE'].append(1)
    else:
        new_x['20CLOSE'].append(0)

    if float(new_x['MA60'][0]) > float(new_x['CLOSE'][0]):
        new_x['60CLOSE'].append(1)
    else:
        new_x['60CLOSE'].append(0)

    if float(new_x['MA200'][0]) > float(new_x['CLOSE'][0]):
        new_x['200CLOSE'].append(1)
    else:
        new_x['200CLOSE'].append(0)

    if float(new_x['MA20'][0]) > float(new_x['MA60'][0]):
        new_x['20-60'].append(1)
    else:
        new_x['20-60'].append(0)

    if float(new_x['MA20'][0]) > float(new_x['MA200'][0]):
        new_x['20-200'].append(1)
    else:
        new_x['20-200'].append(0)

    if float(new_x['MA60'][0]) > float(new_x['MA200'][0]):
        new_x['60-200'].append(1)
    else:
        new_x['60-200'].append(0)
    return new_x


def predict():
    new_x = load_x()
    x_weektrain, y_weektrain, x_monthtrain, y_monthtrain = load_data()

    # Prediction on new dataset
    week_knn = KNeighborsClassifier()
    week_knn.fit(x_weektrain, y_weektrain)
    month_knn = KNeighborsClassifier()
    month_knn.fit(x_monthtrain, y_monthtrain)
    data_x = pd.DataFrame(data=new_x)
    week_prediction = week_knn.predict(data_x)
    month_prediction = month_knn.predict(data_x)

    prediction_array = []
    for prediction in week_prediction, month_prediction:
        if prediction == 1:
            prediction = 'RISE'
            prediction_array.append(prediction)
        else:
            prediction = 'FALL'
            prediction_array.append(prediction)

    print('GOLD is expected to %s in a week, and also %s at the end of this month!' % (
    prediction_array[0], prediction_array[1]))


predict()



