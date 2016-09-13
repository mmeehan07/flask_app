from flask import Flask, render_template, request
import weather
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

app = Flask(__name__)


@app.route("/")
def index():
    city = request.values.get('city')
    forecast = None
    if city:
        forecast = weather.get_weather(city)
    return render_template('index.html', forecast=forecast)


@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run()