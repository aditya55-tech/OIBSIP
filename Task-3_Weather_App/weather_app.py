# Basic Weather App
# Oasis Infobyte Internship - Python Programming

weather_data = {
    "delhi": {
        "temperature": 28,
        "condition": "Haze",
        "humidity": 60,
        "wind_speed": 3.2
    },
    "mumbai": {
        "temperature": 30,
        "condition": "Clear Sky",
        "humidity": 70,
        "wind_speed": 4.5
    },
    "pune": {
        "temperature": 26,
        "condition": "Cloudy",
        "humidity": 55,
        "wind_speed": 2.8
    },
    "bangalore": {
        "temperature": 24,
        "condition": "Rainy",
        "humidity": 65,
        "wind_speed": 3.6
    }
}

print("===== Basic Weather Application =====")

city = input("Enter city name: ").lower()

if city in weather_data:
    data = weather_data[city]
    print(f"\nWeather Report for {city.title()}:")
    print(f"Temperature: {data['temperature']}°C")
    print(f"Condition: {data['condition']}")
    print(f"Humidity: {data['humidity']}%")
    print(f"Wind Speed: {data['wind_speed']} m/s")
else:
    print("\nCity not found in database.")
    print("Available cities:", ", ".join(city.title() for city in weather_data.keys()))
