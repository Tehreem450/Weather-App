import requests
def get_weather(api_key,city):
    base_url="http://api.openweathermap.org/data/2.5/weather" 
    params={"q":city,"appid":api_key,"units":"metric"}

    try:
        response=requests.get(base_url,params=params)
        data=response.json()

        if response.status_code==200:
            return data 
        else:
            print(f"Error:{data['message']}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error:{e}")
        return None
def display_weather(weather_data):
    if weather_data:
        print("\nWeather Information")
        print(f"City:{weather_data['name']}")
        print(f"Temperature:{weather_data['main']['temp']}°C")
        print(f"Weather: {weather_data['weather'][0]['description']}")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        print("Failed to retrieve weather information.")

if __name__ == "__main__":
    api_key = '85ac200afa373d0b3936d074deb71f01'  # Replace with your OpenWeatherMap API key
    city = input("Enter the city name: ")

    weather_data = get_weather(api_key, city)

    display_weather(weather_data)