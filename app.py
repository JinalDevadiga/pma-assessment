from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Enter your API key
API_KEY = ''

@app.route('/')
def home():
    """
    Render the application's home page.

    This view function handles requests to the root URL ("/") of the Flask app
    and returns the rendered 'index.html' template.

    :return: Rendered HTML content for the home page.
    :rtype: str
    """
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    """Handle weather data requests for a given location.

    This view function receives a location from a POST request, fetches the current
    weather and 5-day forecast from the OpenWeatherMap API, and renders the result
    page with the retrieved data.

    If the location is invalid or the weather API returns an error, it renders the
    result page with an error message.

    :return: Rendered HTML page displaying current weather and forecast (if available).
    :rtype: str
    """
    location = request.form['location']

    # Current weather
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    weather_resp = requests.get(weather_url)
    if weather_resp.status_code != 200:
        return render_template('result.html', weather=None, error="Location not found")
    data = weather_resp.json()
    weather = {
        'location': location,
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon']
    }

    # 5-day forecast
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}&units=metric"
    forecast_resp = requests.get(forecast_url)
    forecast = []
    if forecast_resp.status_code == 200:
        fdata = forecast_resp.json()['list']
        daily = {}
        for entry in fdata:
            date = entry['dt_txt'].split(' ')[0]
            if date not in daily:
                daily[date] = entry
            if len(daily) == 5:
                break
        for date, entry in daily.items():
            forecast.append({
                'date': date,
                'temp': entry['main']['temp'],
                'description': entry['weather'][0]['description'],
                'icon': entry['weather'][0]['icon']
            })

    return render_template('result.html', weather=weather, forecast=forecast)

if __name__ == '__main__':
    app.run(debug=True)
