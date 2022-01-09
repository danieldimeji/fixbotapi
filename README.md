# Fix Bot API
Code test from Fix Bot Technologies.
A Django REST API that provides data to the Frontend service and implements the following

1. An endpoint that creates telemetric data (like engine temperature, car speed, car longitude, car latitude, fuel consumption rate).
2. An endpoint that updates the telemetric data you created in 1
3. An endpoint that deletes the telemetric data you created in 1
4. An endpoint that returns the telemetric data you created in 1

# Dependencies
* Python 3.5 and higher
* Django 4.0 
* Channels 3.1
* Channels Redis 3.3.1
* Django REST framework 3.13.1
* Redis server 

# Run on local server
* Download repository files
* run: "pipenv shell" in your shell
* run: pipenv install -r requirements.txt
* run: docker run -p 6379:6379 -d redis:5
* run: python manage.py runserver

