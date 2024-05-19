# Task-Management-API-Assessment
Backend Developer Assessment(NIYO Group)
This documentation covers the setup, configuration, and usage of a Task Management application built with Django and Django Channels for real-time functionality.

Project Setup
Prerequisites
Python 3.9+
Git
Redis

git clone <repository-url>
cd <repository-name>

Install Python Dependencies
Create a virtual environment and install the required packages:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

1. Ensure redis server is on
redis-server(5.0 and above)

2. Apply Migrations

python manage.py migrate

3. Collect Static Files
python manage.py collectstatic --noinput
4. Run Development Server
python manage.py runserver
5. App should be running by now. Navigate to your localhost:8000/real_data

AUTHENTICATION

The app uses JWT token with the django built authentication system.
LOGIN
To login, send a post request to /api/token with the following payload:
{
  "username": "your_username",
  "password": "your_password",
  "email": "your_email@example.com"
}

You will receive this response:
{
    "id": 8,
    "username": "froggly",
    "email": "wfroggly@taske.com"
}

TOKEN(JWT)
To get your token to login, send a post request to /api/token/ with the following payload:
{
  "username": "your_username",
  "password": "your_password",
  "email": "your_email@example.com"
}
You will receive this response:
"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNjE5NTQ5OSwiaWF0IjoxNzE2MTA5MDk5LCJqdGkiOiI0MzE4NjRhOGEwMDU0ZWY5YmM1YThkN2VlMDExMTM0ZSIsInVzZXJfaWQiOjh9.WsBTe212pGAcUxRm7g9mQUkbgsH71t4zZxNJ0fgIrXJ",
"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MTE2Mjk5LCJpYXQiOjE3MTYxMDkwOTksImp0aSI6ImQyMDM5ZTUxN2VlMzQzNDFhMGM3MDJjZDRjNTQ2YmZjIiwidXNlcl9pZCI6OH0.L21wgDwYMILnPu0eaKTQroU62kZNpMUr2meXcNtyW8J"

REFRESH(The token expires in 5mins for my dev preference.Ensure to adjust it to production timing as suited)

To get your token to login, send a post request to /api/token/refresh with the following payload:
{
  "username": "your_username",
  "password": "your_password",
  "email": "your_email@example.com"
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNjE5NTQ5OSwiaWF0IjoxNzE2MTA5MDk5LCJqdGkiOiI0MzE4NjRhOGEwMDU0ZWY5YmM1YThkN2VlMDExMTM0ZSIsInVzZXJfaWQiOjh9.WsBTe212pGAcUxRm7g9mQUkbgsH71t4zZxNJ0fgIrXJ"
}
Note: The refresh value is gotten from the above /api/token/ endpoint
You will receive this response:
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2MTE2NTY3LCJpYXQiOjE3MTYxMDkwOTksImp0aSI6IjkyMDRkOGUwOGY2ZjRlMzc4MDEzYTA3ZmYxYmU1YzRhIiwidXNlcl9pZCI6OH0.RVh_DUNtLOkAFQwxQfT_1qIxNNY2nf-MdbQfJ35sR0c"
}

This will then be used for subsequent connections depending on your ACCESS_TOKEN_LIFETIME which should be configured in the settings.py for production


USER REGISTRATION
To register a new user, send a POST request to /api/register/ with the following payload:
{
  "username": "your_username",
  "password": "your_password",
  "email": "your_email@example.com"
}

Documentation available at http://127.0.0.1:8000/swagger/ or http://127.0.0.1:8000/swagger/


