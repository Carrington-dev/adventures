from flask import Flask, json_response

app = Flask(__name__)

@app.route("/")
def home():
  return json_response({
    
  })
