import requests
import json

BASE_URL = 'http://127.0.0.1:8000/api'

def register_user():
    url = f'{BASE_URL}/users/register/'
    data = {
        'email': 'test2@example.com',
        'username': 'testuser2',
        'password': 'Test123!',
        'password2': 'Test123!'
    }
    response = requests.post(url, json=data)
    print('Registration Response:', response.status_code)
    print(response.json())
    return response.json()

def login_user():
    url = f'{BASE_URL}/users/login/'
    data = {
        'username': 'testuser2',
        'password': 'Test123!'
    }
    response = requests.post(url, json=data)
    print('Login Response:', response.status_code)
    print(response.json())
    return response.json()

def get_weather_forecast(token):
    url = f'{BASE_URL}/weather/forecast/'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(url, headers=headers)
    print('Weather Forecast Response:', response.status_code)
    print(response.json())

if __name__ == '__main__':
    # Step 1: Register
    register_user()
    
    # Step 2: Login and get token
    login_response = login_user()
    if 'access' in login_response:
        # Step 3: Get weather forecast with token
        get_weather_forecast(login_response['access']) 