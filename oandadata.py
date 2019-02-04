import requests

key = ''
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + key,
}

params = [
    ['count', '1'],
    ['price', 'M'],
    ['granularity', 'D'],
]


# Function to get the OPEN, CLOSE value for today
def today():
    response = requests.get('https://api-fxtrade.oanda.com/v3/instruments/XAU_USD/candles', headers=headers,
                            params=params)
    data = response.json()
    candles = data['candles']
    for candle in candles:
        candle_open = candle['mid']['o']
        candle_close = candle['mid']['c']

    return candle_open, candle_close


# Function to calculate SimpleMovingAverage
def SMA(period):
    params[0][1] = period
    response = requests.get('https://api-fxtrade.oanda.com/v3/instruments/XAU_USD/candles', headers=headers,
                            params=params)
    data = response.json()
    candles = data['candles']
    totalprice = 0

    for candle in candles:
        candleprice = candle['mid']['c']
        totalprice += float(candleprice)

    finalsma = float(totalprice)/float(period)
    return finalsma


# Function to calculate a base EMA to build upon
def EMAref(period):
    # To get the SMA 201 days from the present-day
    params[0][1] = period + 200
    response = requests.get('https://api-fxtrade.oanda.com/v3/instruments/XAU_USD/candles', headers=headers,
                            params=params)
    data = response.json()
    candles = data['candles']
    candles = candles[0:20]
    totalprice = 0

    for candle in candles:
        candleprice = candle['mid']['c']
        totalprice += float(candleprice)

    refsma = float(totalprice)/float(period)
    return refsma


# Function to calculate ExponentialMovingAverage
def EMA(period):
    #Calculating 20EMA of 200 days from the present day
    params[0][1] = 200
    response = requests.get('https://api-fxtrade.oanda.com/v3/instruments/XAU_USD/candles', headers=headers,
                            params=params)
    data = response.json()
    candles = data['candles']
    multiplier = (2 / (period + 1))
    emaref = float(EMAref(period))
    old_ema = float(emaref)

    for candle in candles:
        candleprice = float(candle['mid']['c'])
        emaprice = ((candleprice - old_ema) * multiplier + old_ema)
        old_ema = emaprice

    return old_ema

