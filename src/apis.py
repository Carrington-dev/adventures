import uuid
from flask import request, jsonify
from src import app, db, User

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
    users = User.query.all()  # Query all users from the database
    
    return users

@app.route('/api/users', methods=['POST'])
def add_user():
    """
    Creates a new user
    ---
    tags:
      - Users
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - username
            - last_name
            - first_name
            - email
          properties:
            first_name:
              type: string
              example: Maanda
            last_name:
              type: string
              example: Muleya
            username:
              type: string
              example: johndoe
            email:
              type: string
              example: johndoe@example.com
    responses:
      201:
        description: User registered successfully
      400:
        description: User with this username or email already exists
    """
    # Get data from the incoming POST request
    data = request.get_json()
    id = str(uuid.uuid4())
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    username = data.get('username')
    email = data.get('email')

    # Check if username and email are provided
    if not username or not email:
        return jsonify({'message': 'Username and email are required'}), 400
        
    if not id:
        return jsonify({"message": 'Id is required'}), 400
        

    # Create a new user and save it to the database
    try:
        new_user = User(username=username, email=email, first_name=first_name, last_name=last_name)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User added successfully'}), 201
    except:
        return jsonify({'message': 'User with similar credentials already exists'}), 400

@app.route("/subscribe")
def subscribe():
    return jsonify({
        "message": "You are now subscribed to our newsletter!."
    })

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user_fast(user_id):
    user = User.query.get(user_id)  # Returns None if user not found
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user)