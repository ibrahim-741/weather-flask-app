from flask import Flask, render_template, request
from src.weather import get_weather

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")
        weather_data = get_weather(city)

        if weather_data is None:
            error = f"Could not find weather for '{city}'. Check the spelling and try again."

    return render_template("index.html", weather=weather_data, error=error)


if __name__ == "__main__":
    app.run(debug=True)