import os
import requests
from flask import Flask

app = Flask(__name__)

# The endpoint is set to the Kubernetes service name as requested
BACKEND_URL = "http://backend-service:5000/data"

@app.route('/')
def index():
    try:
        response = requests.get(BACKEND_URL, timeout=2)
        data = response.json()
        return f"<h1>Frontend Active</h1><p>Message from Backend: {data['message']}</p>"
    except Exception as e:
        return f"<h1>Frontend Active</h1><p>Error connecting to Backend: {e}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)