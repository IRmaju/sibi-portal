import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="Sibi Heatwave & Civic Portal", page_icon="🌡️", layout="wide"
)

# Title & Header
st.title("🌡️ Sibi Climate & Civic Action Portal")
st.caption(
    "Real-time Extreme Weather Monitoring & Community Advisory System |"
    " Imaginathon Hackathon"
)

# OpenWeather API Setup
API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = "Sibi"


def fetch_sibi_weather(city, api_key):
  if not api_key or api_key == "your_openweather_api_key_here":
    return None
  url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
  try:
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
      return response.json()
  except Exception:
    return None
  return None


data = fetch_sibi_weather(CITY, API_KEY)

# Display Weather Data or Demo Prototype View
if data:
  temp = data["main"]["temp"]
  feels_like = data["main"]["feels_like"]
  humidity = data["main"]["humidity"]
  weather_desc = data["weather"][0]["description"].title()

  col1, col2, col3, col4 = st.columns(4)
  col1.metric("Current Temp", f"{temp} °C")
  col2.metric("Feels Like", f"{feels_like} °C")
  col3.metric("Humidity", f"{humidity}%")
  col4.metric("Condition", weather_desc)

  st.divider()

  st.subheader("🔥 Heatwave & Safety Advisory")
  if temp >= 40:
    st.error(
        "⚠️ **CRITICAL HEATWAVE ALERT**: Extreme temperatures detected. Avoid"
        " direct sun exposure between 11 AM and 4 PM."
    )
  elif temp >= 35:
    st.warning(
        "⚡ **HIGH HEAT ADVISORY**: High heat index. Ensure adequate hydration"
        " and shelter for livestock."
    )
  else:
    st.success(
        "✅ **MODERATE CLIMATE**: Current weather conditions are safe for"
        " outdoor activity in Sibi."
    )

else:
  st.info(
      "ℹ️ Showing Sibi Interactive Prototype Framework. Add your OpenWeather API"
      " key in .env for live API updates."
  )

  col1, col2, col3, col4 = st.columns(4)
  col1.metric("Current Temp", "42 °C")
  col2.metric("Feels Like", "45 °C")
  col3.metric("Humidity", "38%")
  col4.metric("Condition", "Clear Sky")

  st.divider()
  st.error(
      "⚠️ **CRITICAL HEATWAVE ALERT**: Extreme temperatures detected. Avoid"
      " direct sun exposure between 11 AM and 4 PM."
  )

# Tabs for Civic Context & Local Heritage
tab1, tab2, tab3 = st.tabs([
    "🏛️ Sibi Profile & Heritage",
    "🛡️ Heatstroke Safety Guidelines",
    "🌾 Agriculture & Livestock Advice",
])

with tab1:
  st.markdown("""
    ### About Sibi, Balochistan
    * **Climatic Importance:** Sibi is famous for holding historical temperature records in South Asia, routinely exceeding 50°C during peak summer.
    * **Cultural Heritage:** Home to the historical **Sibi Mela**, an annual livestock fair and socio-economic gathering celebrated for centuries.
    * **Strategic Location:** Serves as a key junction connecting Quetta with Sindh.
    """)

with tab2:
  st.markdown("""
    ### Heatstroke Prevention & Precautions
    1. **Hydration:** Consume plenty of fluids, water, and traditional cooling drinks.
    2. **Outdoor Protection:** Keep heads covered with light cotton scarves or umbrellas.
    3. **Emergency Response:** If experiencing dizziness, move immediately to a shaded place and apply cold water compresses.
    """)

with tab3:
  st.markdown("""
    ### Agri & Livestock Protection Tips
    * **Livestock Care:** Provide shaded enclosures and clean drinking water for cattle during midday heat.
    * **Crop Advisory:** Adjust irrigation timings to early mornings or late evenings to reduce water evaporation loss.
    """)