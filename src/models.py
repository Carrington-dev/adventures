from dataclasses import dataclass
from src import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

# Define a model (Table) for the database
@dataclass
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), unique=False, nullable=False)
    last_name = db.Column(db.String(100), unique=False, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
    
    id: str
    first_name: str
    last_name: str
    username: str
    email: str

# Create the database tables (if they don't exist)
with app.app_context():
    db.create_all()

