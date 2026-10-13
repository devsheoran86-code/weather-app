# Weather App (Python + Django)

A beginner-friendly Django weather app that fetches current weather for a city using OpenWeatherMap and stores recent searches in SQLite.

## Features
- Search weather by city name
- Show temperature, humidity, pressure, weather description, and icon
- Save successful searches to the database
- Display the five most recent searches

## Requirements
- Python 3.10 or newer
- An OpenWeatherMap API key

## Setup on Windows

1. Open Command Prompt inside this folder.
2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set your API key in the terminal before running the app:

   ```bat
   set OPENWEATHER_API_KEY=put_your_real_api_key_here
   ```

   Do not upload your real API key to GitHub.

5. Create the database tables:

   ```bash
   python manage.py makemigrations main
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Open http://127.0.0.1:8000/ in your browser.

## GitHub
This repository contains the source code. The Django development server runs locally; uploading to GitHub does not automatically host the live website.
