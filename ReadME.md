# 🌦️ Weather Forecast Web App

This project is a simple and interactive **weather forecasting app** built with [Streamlit](https://streamlit.io/) and [Plotly](https://plotly.com/python/). It uses the **OpenWeatherMap API** to fetch real-time weather data and display either the temperature trends or sky conditions (like clear, clouds, rain, or snow) for the next few days.

---

## 📌 Features

- 📍 Input any city name to get forecast
- 📅 Select number of forecast days (1 to 5)
- 🌡️ Visualize temperature trends with interactive line charts
- ☁️ Display sky conditions using icons (images)

---

## 🚀 Installation & Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/weather-forecast-app.git
   cd weather-forecast-app
   ```

2. **Install dependencies**:

   Make sure you have Python 3.7+ installed.

   ```bash
   pip install streamlit plotly requests
   ```

3. **Set up your `backend.py`**:

   Create a `backend.py` file that fetches weather data using your **OpenWeatherMap API key**:

   ```python
   import requests

   def get_data(place, days):
       url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid=YOUR_API_KEY"
       response = requests.get(url)
       data = response.json()
       filtered = data["list"][:8 * days]  # 8 intervals per day (3-hour gaps)
       return filtered
   ```

   Replace `YOUR_API_KEY` with your actual API key from [https://openweathermap.org/api](https://openweathermap.org/api).

4. **Ensure images exist**:

   Place the following icons in an `images/` folder:
   - `clear.png`
   - `cloud.png`
   - `rain.png`
   - `snow.png`

---

## 💻 Running the App

To launch the app:

```bash
streamlit run weather_forecast_app.py
```

---

## 📁 Project Structure

```
weather-forecast-app/
│
├── weather_forecast_app.py       # Main Streamlit application
├── backend.py                    # Function to fetch API data
├── images/                       # Folder containing sky condition icons
│   ├── clear.png
│   ├── cloud.png
│   ├── rain.png
│   └── snow.png
└── README.md                     # Project documentation
```

---

## 📷 App Preview

- Temperature plot using Plotly line chart  
- Sky condition shown using corresponding images (e.g., ☀️ Clear, ☁️ Cloudy)

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – for building the UI
- **Plotly** – for interactive data visualization
- **OpenWeatherMap API** – for fetching real-time weather data

---

