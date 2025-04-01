from datetime import datetime
from flask import render_template, jsonify
from src import app

@app.context_processor
def inject_globals():
    company = "Thrifty Adventures"
    return {
        "company": company,
        "year": 2025,
        "phone": '067 735 2242',
        "email": 'hello@thriftyadventures.co.za',
        "address": "395 Francis Baard Street</p><p>Pretoria Central, 0001/2</p><p>South Africa",
        "copyright_notice": f"© {datetime.now().year} { company }. All rights reserved.",
        "copyright": f"""© <span>{datetime.now().year}</span><strong class="px-1 sitename">{ company }.</strong> <span>All Rights Reserved.</span>""",
    }

@app.route("/")
def home():
    return render_template("index.html")

# @app.route("/pricing")
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

# @app.route("/features")
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")