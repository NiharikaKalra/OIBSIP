import requests

def fetch_weather_report():
    # -------------------------------------------------------------
    # 1. API Key Setup
    
    api_key = "648e75ba42cde732a305574f45e38560"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    # -------------------------------------------------------------

    print("=== Real-Time Weather Application ===")
    
    # 2. Input Validation (Checks for empty string or just spaces)
    city_input = input("Enter City Name or ZIP Code: ").strip()
    
    if not city_input:
        print("Error: Input fields cannot be empty. Please enter a location name.")
        return

    # 3. Parameters configuration
    # units='metric' keeps temperature in Celsius
    query_parameters = {
        'q': city_input,
        'appid': api_key,
        'units': 'metric'
    }

    # 4. API Request and Error Handling
    try:
        response = requests.get(base_url, params=query_parameters, timeout=8)
        
        # Checking HTTP Status Codes
        if response.status_code != 200:
            if response.status_code == 404:
                print("Error: Location not found. Please verify the city name or ZIP code.")
            elif response.status_code == 401:
                print("Error: Authentication failed. Invalid API Key or it is not active yet.")
            else:
                print(f"Error: Server returned unexpected status code ({response.status_code})")
            return
            
        # Parse the JSON response
        weather_json = response.json()

    # Network exceptions
    except requests.exceptions.Timeout:
        print("Error: Request timed out. The server took too long to reply.")
        return
    except requests.exceptions.ConnectionError:
        print("Error: Failed to connect. Please check your internet connection.")
        return
    except Exception as general_error:
        print(f"An unexpected error occurred during execution: {general_error}")
        return

    # 5. Extracting and Displaying Data (As per Feature Checklist)
    try:
        name_of_city = weather_json['name']
        temp_in_celsius = weather_json['main']['temp']
        humidity_level = weather_json['main']['humidity']
        wind_speed_value = weather_json['wind']['speed']
        
        # Weather arrays typically contain an object at index 0
        weather_description = weather_json['weather'][0]['description'].capitalize()

        # Converting Celsius to Fahrenheit manually: (C * 9/5) + 32
        temp_in_fahrenheit = (temp_in_celsius * 9/5) + 32

        # Final Formatting Output
        print(f"\n[ Weather Details for: {name_of_city} ]")
        print(f"Current Condition : {weather_description}")
        print(f"Temperature       : {temp_in_celsius:.1f}°C / {temp_in_fahrenheit:.1f}°F")
        print(f"Humidity Ratio    : {humidity_level}%")
        print(f"Wind Velocity     : {wind_speed_value} m/s")
        
    except KeyError:
        print("Error: The API structure changed or data is missing from the weather server.")

# Runner block
if __name__ == "__main__":
    fetch_weather_report()
 