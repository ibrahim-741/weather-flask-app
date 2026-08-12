# Weather Checker

A simple Flask web app that fetches real-time weather data for any city using the OpenWeatherMap API.

## Features

- Search weather by city name
- Displays temperature, feels-like, humidity, wind speed, and condition
- Graceful error handling for invalid cities and network failures
- Clean, responsive UI

## Screenshot

*(add a screenshot here once you take one)*

## Tech Stack

- Python
- Flask
- OpenWeatherMap API
- HTML/CSS (Jinja2 templating)

## Setup

1. Clone the repo
   \`\`\`bash
   git clone https://github.com/YOUR_USERNAME/weather-flask-app.git
   cd weather-flask-app
   \`\`\`

2. Create and activate a virtual environment
   \`\`\`bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   \`\`\`

3. Install dependencies
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. Add your API key
   - Copy \`.env.example\` to \`.env\`
   - Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)
   - Add it to \`.env\`:
     \`\`\`
     OPENWEATHER_API_KEY=your_key_here
     \`\`\`

5. Run the app
   \`\`\`bash
   python app.py
   \`\`\`

6. Open http://127.0.0.1:5000 in your browser

## Project Structure

\`\`\`
weather-flask-app/
├── app.py                 # Flask routes
├── src/
│   └── weather.py         # Weather API logic
├── templates/
│   └── index.html         # Main page template
├── static/
│   └── css/style.css      # Styling
├── requirements.txt
├── .env.example
└── .gitignore
\`\`\`