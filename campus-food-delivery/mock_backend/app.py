# mock_backend/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import string

app = Flask(__name__)
CORS(app)

# Mock Data
stores = [
    {
        "id": "store1",
        "name": "Pizza Palace",
        "image": "https://via.placeholder.com/150",
        "opening_hours": "10:00 AM - 10:00 PM",
        "is_open": True
    },
    {
        "id": "store2",
        "name": "Burger Hub",
        "image": "https://via.placeholder.com/150",
        "opening_hours": "9:00 AM - 9:00 PM",
        "is_open": True
    },
    {
        "id": "store3",
        "name": "Sushi World",
        "image": "https://via.placeholder.com/150",
        "opening_hours": "11:00 AM - 11:00 PM",
        "is_open": False
    },
    # Add more stores as needed
]

items = {
    "store1": {
        "categories": [
            {"id": "cat1", "name": "Veg"},
            {"id": "cat2", "name": "Non-Veg"}
        ],
        "items": [
            {
                "id": "item1",
                "name": "Margherita Pizza",
                "description": "Classic delight with 100% real mozzarella cheese",
                "price": 250,
                "image": "https://via.placeholder.com/100",
                "is_available": True,
                "available_quantity": 10,
                "category_id": "cat1"
            },
            {
                "id": "item2",
                "name": "Pepperoni Pizza",
                "description": "Loaded with pepperoni and cheese",
                "price": 300,
                "image": "https://via.placeholder.com/100",
                "is_available": False,
                "available_quantity": 0,
                "category_id": "cat2"
            },
            # Add more items as needed
        ]
    },
    "store2": {
        "categories": [
            {"id": "cat1", "name": "Veg"},
            {"id": "cat2", "name": "Non-Veg"}
        ],
        "items": [
            {
                "id": "item3",
                "name": "Veg Burger",
                "description": "Delicious veggie patty with fresh lettuce",
                "price": 150,
                "image": "https://via.placeholder.com/100",
                "is_available": True,
                "available_quantity": 15,
                "category_id": "cat1"
            },
            {
                "id": "item4",
                "name": "Chicken Burger",
                "description": "Juicy chicken patty with mayo",
                "price": 200,
                "image": "https://via.placeholder.com/100",
                "is_available": True,
                "available_quantity": 20,
                "category_id": "cat2"
            },
            # Add more items as needed
        ]
    },
    # Add more stores' items as needed
}

users = {
    "1234567890": {
        "phone": "1234567890",
        "pin": "1234",
        "name": "John Doe",
        "email": "johndoe@example.com"
    },
    # Add more users as needed
}

delivery_locations = [
    {"id": "loc1", "name": "Library"},
    {"id": "loc2", "name": "Cafeteria"},
    {"id": "loc3", "name": "Dormitory"},
    # Add more locations as needed
]

admin_credentials = {
    "admin_id": "admin123",
    "admin_password": "password123"
}

# Helper function to generate OTP
def generate_otp(length=6):
    return ''.join(random.choices(string.digits, k=length))

# API Endpoints

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    phone = data.get('phone')
    pin = data.get('pin')

    user = users.get(phone)
    if user and user['pin'] == pin:
        return jsonify({"success": True, "message": "Login successful."}), 200
    else:
        return jsonify({"success": False, "message": "Invalid phone number or PIN."}), 401

@app.route('/api/auth/signup', methods=['POST'])
def signup():
    data = request.get_json()
    phone = data.get('phone')
    email = data.get('email')
    otp = data.get('otp')

    # For simplicity, assume OTP is always correct
    if phone in users:
        return jsonify({"success": False, "message": "User already exists."}), 400
    else:
        users[phone] = {
            "phone": phone,
            "pin": "0000",  # Default PIN
            "name": "New User",
            "email": email
        }
        return jsonify({"success": True, "message": "Signup successful."}), 201

@app.route('/api/auth/send-otp', methods=['POST'])
def send_otp():
    data = request.get_json()
    email = data.get('email')

    # Simulate sending OTP
    otp = generate_otp()
    print(f"OTP for {email}: {otp}")  # In real application, send via email

    return jsonify({"success": True, "message": "OTP sent."}), 200

@app.route('/api/stores', methods=['GET'])
def get_stores():
    return jsonify({"stores": stores}), 200

@app.route('/api/stores/<store_id>', methods=['GET'])
def get_store(store_id):
    store = next((store for store in stores if store['id'] == store_id), None)
    if store:
        return jsonify(store), 200
    else:
        return jsonify({"message": "Store not found."}), 404

@app.route('/api/stores/<store_id>/items', methods=['GET'])
def get_store_items(store_id):
    store_items = items.get(store_id)
    if store_items:
        return jsonify(store_items), 200
    else:
        return jsonify({"message": "Items not found for this store."}), 404

@app.route('/api/delivery-locations', methods=['GET'])
def get_delivery_locations():
    return jsonify({"locations": delivery_locations}), 200

@app.route('/api/user/profile', methods=['GET'])
def get_user_profile():
    # For testing, return a dummy user
    return jsonify({
        "name": "John Doe",
        "email": "johndoe@example.com",
        "phone": "1234567890"
    }), 200

@app.route('/api/user/update-phone', methods=['POST'])
def update_phone():
    data = request.get_json()
    new_phone = data.get('phone')
    # For testing, simply return success
    return jsonify({"success": True, "message": "Phone number updated."}), 200

if __name__ == '__main__':
    app.run(debug=True)
