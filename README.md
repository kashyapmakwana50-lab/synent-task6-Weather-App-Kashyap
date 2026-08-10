# Weather App 🌤️

A simple Python command-line weather app that uses the OpenWeatherMap API to get current weather information for a city.

## Features

* Search weather by city name
* Shows temperature in °C
* Shows humidity
* Displays API errors
* Uses OpenWeatherMap API

## How to Run

Install the required library:

```bash
pip install requests
```

Then run:

```bash
python weather.py
```

Enter a city name when prompted.

## Example

```text
Enter city name: London

Weather Report
City: London
Temperature: 18.5 °C
Humidity: 72 %
```

## Requirements

* Python 3.x
* `requests`
* OpenWeatherMap API key

## Note

**Do not upload your API key directly to GitHub.** Store it in an environment variable or `.env` file instead.

## License

This project is open source and free to use.
