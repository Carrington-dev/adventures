from flask import render_template
from src import app

@app.context_processor
def inject_globals():
    return {
        "company": "Thrifty Adventures",
        "year": 2025,
        "phone": '067 735 2242',
        "email": 'hello@thriftyadventures.co.za',
        "address": "A108 Adam Street</p><p>New York, NY 535022",
    }

@app.route("/")
def home():
    return render_template("index.html")

# @app.route("/pricing")
# @app.route("/features")
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
