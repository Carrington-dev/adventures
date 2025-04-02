from flask import Flask
from flasgger import Swagger

app = Flask(__name__, static_url_path="/static", static_folder="../static", template_folder='../templates')

app.config['SWAGGER'] = {
    'title': 'TravelEase API',
    'uiversion': 3,  # Use Swagger UI version 3
    'description': 'The ultimate travel booking and management solution',
    'version': '1.0.0'
}

swagger = Swagger(app)  # Initialize Swagger
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  # Using SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional but recommended