from flask import Flask, render_template
import requests
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
app = Flask(__name__)

@app.route('/')
def index():
    #Api for data
    api_key = '49e2bf11151133ab3c0d1e702a7d59e5'
    city = 'Bogotá'
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'

    response = requests.get(url)
    data = response.json()
    data_list = []

    for forecast in data['list']:
        temp = forecast['main']['temp']
        temp_min = forecast['main']['temp_min']
    
        data_list.append({
            'temp_min': temp_min,
            'temp': temp,
    })

    df = pd.DataFrame(data_list)
    x = df[['temp_min']]
    y = df['temp']

    #Model regression
    x_train, x_test, y_train, y_test = train_test_split (x, y, test_size = 0.2, random_state = 42)
    model = LinearRegression()
    model.fit(x_train, y_train)

    new_temp_min_value = df[['temp_min']].mean() + 1.0
    temp_pred = model.predict([new_temp_min_value])
    return render_template('index.html', predict = temp_pred[0])

app.run(host='0.0.0.0', port= 3000, debug= True)

