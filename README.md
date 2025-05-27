# 🌦️ PMA Weather App – Technical Assessment

This project contains two Flask-based web applications developed as part of a technical assessment. Each application demonstrates API integration, user interaction, and optional extended functionality using public APIs.

---

## 📁 Project Structure

pma-assessment/<br>
├── app.py # Assessment 1 - Basic Weather App<br>
├── app2.py # Assessment 2 - Extended Version with DB<br>
├── templates/ # HTML templates (index.html, result.html, etc.)<br>
├── instance/ # Contains SQLite DB for assessment 2<br>
├── requirements.txt # Python package dependencies<br>
├── README.md # Project documentation<br>


---

## ✅ Assessment 1 (`app.py`) – Basic Weather App

- Accepts a **location** as input.
- Fetches:
  - **Current weather**
  - **5-day forecast** from the OpenWeatherMap API
- Displays results in a user-friendly format.
- Embeds:
  - 🌍 **Google Maps** for the location
  - 🎥 **YouTube videos** about the location

---

## ✅ Assessment 2 (`app2.py`) – Extended Weather App with Database

- Accepts:
  - Location
  - Start Date
  - End Date
- Fetches and stores weather forecast in a **SQLite database**
- Displays stored results in a history page.
- Uses **Flask-SQLAlchemy** for ORM
- Supports:
  - 🌍 Google Maps

---

## 🔧 How to Run the Apps

1. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2. **Run the app**:
    ```bash
    # For Assessment 1
    python app.py

    # For Assessment 2
    python app2.py
    ```

3. **Open in browser**:
    ```
    http://localhost:5000
    ```

---

## 🔑 API Configuration

> You need an OpenWeatherMap API key.

Add your API key in both files:
```python
API_KEY = 'your_openweathermap_api_key'
```

---

## 📦 Tech Stack
Python 3.x

Flask

SQLAlchemy

SQLite

OpenWeatherMap API

---

## 👤 Developer Info

Developed by **Jinal Prakash Devadiga** as part of the PMA Technical Assessment.

---
## Product Manager Accelerator
The Product Manager Accelerator Program is designed to support PM professionals through every stage of their careers. From students looking for entry-level jobs to Directors looking to take on a leadership role, our program has helped over hundreds of students fulfill their career aspirations.

Our Product Manager Accelerator community are ambitious and committed. Through our program they have learnt, honed and developed new PM and leadership skills, giving them a strong foundation for their future endeavors.

Here are the examples of services we offer. Check out our website (link under my profile) to learn more about our services.

🚀 PMA Pro
End-to-end product manager job hunting program that helps you master FAANG-level Product Management skills, conduct unlimited mock interviews, and gain job referrals through our largest alumni network. 25% of our offers came from tier 1 companies and get paid as high as $800K/year. 

🚀 AI PM Bootcamp
Gain hands-on AI Product Management skills by building a real-life AI product with a team of AI Engineers, data scientists, and designers. We will also help you launch your product with real user engagement using our 100,000+ PM community and social media channels. 

🚀 PMA Power Skills
Designed for existing product managers to sharpen their product management skills, leadership skills, and executive presentation skills

🚀 PMA Leader
We help you accelerate your product management career, get promoted to Director and product executive levels, and win in the board room. 

🚀 1:1 Resume Review
We help you rewrite your killer product manager resume to stand out from the crowd, with an interview guarantee.Get started by using our FREE killer PM resume template used by over 14,000 product managers. https://www.drnancyli.com/pmresume

🚀 We also published over 500+ free training and courses. Please go to my YouTube channel https://www.youtube.com/c/drnancyli and Instagram @drnancyli to start learning for free today.