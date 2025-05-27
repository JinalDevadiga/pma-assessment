from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import requests
import json
from datetime import datetime

app2 = Flask(__name__)
app2.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app2.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app2)

API_KEY = 'd52f7f37b98ec662e2f882f7114936ec'

class WeatherRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.String(10), nullable=False)
    end_date = db.Column(db.String(10), nullable=False)
    data = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Ensure database tables are created
with app2.app_context():
    db.create_all()

@app2.route('/')
def index():
    return render_template('index2.html')

@app2.route('/submit', methods=['POST'])
def submit_record():
    location = request.form['location']
    start_date = request.form['start_date']
    end_date = request.form['end_date']

    # Fetch forecast and filter by date range
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}&units=metric"
    resp = requests.get(url)
    if resp.status_code != 200:
        return render_template('result2.html', error="Location not found or API error")

    forecast_list = resp.json()['list']
    filtered = [entry for entry in forecast_list
                if start_date <= entry['dt_txt'][:10] <= end_date]

    record = WeatherRecord(
        location=location,
        start_date=start_date,
        end_date=end_date,
        data=json.dumps(filtered)
    )
    db.session.add(record)
    db.session.commit()

    return render_template('result2.html', weather=filtered, location=location,
                           start_date=start_date, end_date=end_date)

@app2.route('/history')
def history():
    records = WeatherRecord.query.order_by(WeatherRecord.created_at.desc()).all()
    return render_template('history2.html', records=records)

@app2.route('/edit/<int:record_id>', methods=['GET', 'POST'])
def edit(record_id):
    record = WeatherRecord.query.get_or_404(record_id)
    if request.method == 'POST':
        record.location = request.form['location']
        record.start_date = request.form['start_date']
        record.end_date = request.form['end_date']
        # Optionally refetch data
        resp = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?q={record.location}"
                            f"&appid={API_KEY}&units=metric")
        filtered = [entry for entry in resp.json()['list']
                    if record.start_date <= entry['dt_txt'][:10] <= record.end_date]
        record.data = json.dumps(filtered)
        db.session.commit()
        return redirect(url_for('history'))
    return render_template('edit2.html', record=record)

@app2.route('/delete/<int:record_id>')
def delete(record_id):
    record = WeatherRecord.query.get_or_404(record_id)
    db.session.delete(record)
    db.session.commit()
    return redirect(url_for('history'))

if __name__ == '__main__':
    app2.run(debug=True)
