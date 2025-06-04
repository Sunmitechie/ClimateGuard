# ClimateGuard

ClimateGuard is an AI-powered weather forecast platform designed to predict and alert users about extreme weather events in Africa. The platform uses advanced machine learning algorithms and hyperlocal data to provide accurate predictions and safety recommendations.

## Features

- **Hyperlocal Weather Predictions**: Precise weather forecasts based on user location
- **Risk Assessment**: Color-coded risk levels (Green, Yellow, Red) for different locations
- **Early Warning System**: Advanced notifications for extreme weather events
- **Safety Recommendations**: Customized safety guidelines and precautions
- **Interactive Maps**: Visual representation of weather patterns and risk zones
- **Real-time Updates**: Continuous monitoring and updates of weather conditions
- **Emergency Directions**: Guidance for safe routes and shelter locations
- **AI-Powered Insights**: Machine learning models for accurate predictions

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the root directory with:
```
SECRET_KEY=your_django_secret_key
DEBUG=True
WEATHER_API_KEY=your_weather_api_key
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

## Project Structure

- `ai_predict/`: ML models for weather prediction
- `ai_assist/`: AI-powered user assistance
- `weather/`: Weather data management
- `users/`: User authentication and profiles
- `dashboard/`: User interface and visualization
- `notifications/`: Alert system for weather events

## API Documentation

### Weather Endpoints
- `GET /api/weather/current/`: Get current weather data
- `GET /api/weather/forecast/`: Get weather forecast
- `GET /api/weather/risks/`: Get location-based risk assessment

### User Endpoints
- `POST /api/users/register/`: Register new user
- `POST /api/users/login/`: User login
- `GET /api/users/profile/`: Get user profile

### Notification Endpoints
- `GET /api/notifications/`: Get user notifications
- `POST /api/notifications/subscribe/`: Subscribe to alerts

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License.
