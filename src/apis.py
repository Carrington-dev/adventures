from flask import jsonify
from src import app

users = []

@app.route("/api/home")
def api_home():
    return jsonify({
        "message": "Hi Carrington, my name is Wonderful"
    })

@app.route("/api/about")
def api_about():
    return jsonify({
        "message": "About Us"
    }) 

@app.route("/api/users")
def get_all_users():
    return users

@app.route("/api/users")
def create_a_user():
    return users


@app.route("/subscribe")
def subscribe():
    return jsonify({
        "message": "You are now subscribed to our newsletter!."
    })