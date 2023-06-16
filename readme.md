# Sentiment Analysis API

This project implements a sentiment analysis API using Django and Django REST Framework. The API provides an endpoint `/analyze` that accepts POST requests with JSON payloads for sentiment analysis.

## Installation

1. Clone the repository:

2. Navigate to the project directory:

3. Create a virtual environment:

4. Activate the virtual environment:
- For Windows:
  ```
  venv\Scripts\activate
  ```
- For macOS/Linux:
  ```
  source venv/bin/activate
  ```

5. Install the dependencies:
-pip install -r requirements.txt


## Usage

1. Start the Django development server:
-python manage.py runserver


2. Send a POST request to the `/analyze` endpoint with a JSON payload containing the `text` field:
-curl -X POST -H "Content-Type: application/json" -d '{"text": "I loved the Spiderman movie!"}' http://localhost:8000/analyze