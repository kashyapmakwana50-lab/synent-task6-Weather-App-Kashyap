# Weather Application – Project Report

## 1. Objective

The objective of this project is to create a Python application that retrieves and displays current weather information for a city entered by the user.

## 2. Methodology

The program uses the OpenWeatherMap API to request real-time weather data. The user enters a city name, which is included in an API request URL.

The application retrieves the response and converts it into JSON format. It then checks the response status and displays the available weather information.

## 3. Implementation

The program uses Python's `requests` library to communicate with the weather API. The API response is processed to obtain:

* City name
* Temperature in Celsius
* Humidity percentage

If the API returns an error, such as an invalid city name, the program displays the error message provided by the API.

## 4. Testing and Results

The application was tested by entering valid city names and successfully displaying their current temperature and humidity.

Invalid city names were also tested, and the program correctly displayed an error message from the API.

## 5. Conclusion

The Weather Application successfully retrieves and displays current weather information using an external API. The project demonstrates the use of Python, API requests, JSON data processing, user input, and basic error handling.
