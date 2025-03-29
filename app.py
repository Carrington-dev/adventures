from flask import render_template
from src import app

@app.route("/")
def home():
    return render_template("index.html")

# @app.route("/pricing")
# @app.route("/features")
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
