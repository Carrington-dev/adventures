from flask import jsonify
from src import app

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