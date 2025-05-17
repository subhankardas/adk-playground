# 🌦️ Weather Agent using Google ADK

This project is a weather agent built using the Google Agent Development Kit (ADK). It enables users to fetch current weather information for any city worldwide by integrating with the OpenWeatherMap APIs.

### 1. Set up Environment & Install ADK

Create & Activate Virtual Environment (Recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install Google ADK:

```bash
pip install google-adk
```

## 🛠️ Usage

### Run the agent locally/web

```bash
adk run weather_agent
adk web
```

### CLI Response

```
[user]: How's the weather in London?
[weather_agent]: Well, hold on to your hats, folks! It's a partly cloudy day in London with a temperature of 8.95 degrees Celsius. The wind is blowing at a speed of 3.6 meters per second, so you might want to avoid wearing a Marilyn Monroe dress. The humidity is at 82%, so it's not quite a rainforest, but your hair might get a little frizzy.

[user]: How's the temperature in Dhaka?
[weather_agent]: Alright, let's check Dhaka! The temperature in Dhaka is 33.99 degrees Celsius. So, it's hot. The humidity is 49%, so it's not too bad. The wind speed is 2.57 meters per second.
```

![weather_agent](../docs/weather_agent.png)
