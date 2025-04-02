from flask import Flask

app = Flask(__name__, static_url_path="/static", static_folder="../static", template_folder='../templates')


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  # Using SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional but recommended