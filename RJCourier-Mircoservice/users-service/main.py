from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage
users = {}

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    user_id = len(users) + 1
    users[user_id] = data
    return jsonify({"id": user_id, "data": data}), 201

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

if __name__ == "__main__":
    app.run(port=5001, debug=True)
