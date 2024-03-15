from flask import Flask, jsonify
import requests
import socket
import datetime

app = Flask(__name__)

@app.route('/api/hello')
def hello():
    hostname = socket.gethostname()
    now = datetime.datetime.now().strftime('%Y%m%d%H%M')
    version = "1.0"
    weather_data = get_weather()
    return jsonify({
        "hostname": hostname,
        "datetime": now,
        "version": version,
        "weather": weather_data
    })

@app.route('/api/health')
def health_check():
    return "API is healthy!"

def get_weather():
    weather_api_url = "http://api.weatherapi.com/v1/current.json?key=88aa8def511e442fa4c170548241403&q=Dhaka"
    response = requests.get(weather_api_url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['current']['temp_c']
        temp_unit = "c"
        return {
            "dhaka": {
                "temperature": temperature,
                "temp_unit": temp_unit
            }
        }
    else:
        return {
            "error": "Unable to fetch weather data"
        }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
