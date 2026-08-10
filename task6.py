import requests

api_key = "dae9fd370e2e49436a86c49eb9d3eb9c"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

print(data)  

if str(data.get("cod")) == "200":
    print("\nWeather Report")
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
else:
    print("Error:", data.get("message"))
