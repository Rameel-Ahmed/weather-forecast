# weather_forecast_app.py

import streamlit as st
import plotly.express as px
from backend import get_data  # Function to fetch weather data from OpenWeatherMap API

# Set the title of the web app
st.title("Weather Forecast for the Next Days")

# Input field for user to enter a location
place = st.text_input("Place: ")

# Slider to select number of days for forecast (1 to 5)
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")

# Dropdown to choose between viewing temperature or sky condition
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

# Subheader displays user choices
st.subheader(f"{option} for the next {days} days in {place}")

# If a location is provided
if place:
    try:
        # Fetch data from API using custom backend function
        filtered_data = get_data(place, days)

        if option == "Temperature":
            # Extract temperature and date for plotting
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]  # Convert Kelvin to Celsius
            dates = [dict["dt_txt"] for dict in filtered_data]

            # Create and display line chart using Plotly
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            # Map weather conditions to local image paths
            images = {
                "Clear": "images/clear.png",
                "Clouds": "images/cloud.png",
                "Rain": "images/rain.png",
                "Snow": "images/snow.png"
            }
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]

            # Display corresponding sky images
            st.image(image_paths, width=115)

    except KeyError:
        # Handle errors if the location is invalid
        st.write("That place does not exist.")