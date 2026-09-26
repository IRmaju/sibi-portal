# 🌡️ Sibi Climate & Civic Action Portal

> **An automated real-time extreme weather monitoring and community safety advisory system tailored for Sibi, Balochistan.**
> Developed for the **Imaginathon Hackathon**.

---

## 📌 Overview

**Sibi, Balochistan** is historically renowned as one of the hottest regions in South Asia, where summer temperatures regularly cross **50 °C**. Extreme heatwaves pose severe health risks (heatstroke, dehydration) to local residents, daily wage workers, and livestock.

The **Sibi Climate & Civic Action Portal** is a lightweight, responsive web application designed to serve as an **Early Warning & Civic Support System**. It monitors live weather metrics via OpenWeather API, automatically triggers heatwave alerts based on critical temperature thresholds, and provides localized advice across health, agriculture, and cultural heritage.

---

## ✨ Key Features

- **📊 Real-Time Weather Dashboard:** Fetches live **Current Temperature**, **Feels-Like Temperature**, **Humidity**, and **Sky Conditions** for Sibi.
- **🚨 Automated Heatwave Alert System:**
  - **Critical Heatwave Alert ($\ge 40^\circ\text{C}$):** Red high-priority warning with immediate safety protocols.
  - **High Heat Advisory ($35^\circ\text{C} - 39^\circ\text{C}$):** Yellow caution warning for high temperature risks.
  - **Moderate Climate Notice ($< 35^\circ\text{C}$):** Green informational indicator for normal conditions.
- **🛡️ Interactive Prototype Mode (Fallback):** Built-in fail-safe mechanism that loads demo data ($42^\circ\text{C}$) if no OpenWeather API key is provided, ensuring 100% demo stability during hackathon evaluations.
- **📑 Civic Knowledge Hub (Tabs):**
  - **🏛️ Sibi Profile & Heritage:** Insights into Sibi's unique climate history, Sibi Mela, and socio-economic importance.
  - **🛡️ Heatstroke Safety Guidelines:** Practical, localized steps to avoid heat exhaustion and dehydration.
  - **🌾 Agriculture & Livestock Advice:** Protection measures for crops, livestock, and local farming communities during extreme heat.

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.10+
- **Framework:** Streamlit
- **API Integration:** OpenWeatherMap API & `requests`
- **Environment Management:** `python-dotenv`
- **Deployment Platform:** Streamlit Community Cloud

---

## 🚀 Local Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/IRmaju/sibi-portal.git](https://github.com/IRmaju/sibi-portal.git)
   cd sibi-portal
