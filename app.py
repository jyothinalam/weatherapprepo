from flask import Flask, render_template, request 
import requests

app = Flask(__name__)

@app.route("/weather_app")
def homepage():
    return render_template("index.html")


#apikey='3ee03b8ff1b57db01677cd385775519f' # my key

@app.route("/weatherapp",methods=['POST','GET'])
def get_weatherdata():
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    param = {'q':request.form.get("city"), 
    'appid': request.form.get("appid"),
    'units':request.form.get("units")
    }

    response =  requests.get(url, params=param)
    data = response.json()

    return f"data:{data}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)