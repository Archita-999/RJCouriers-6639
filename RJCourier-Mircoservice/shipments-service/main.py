from flask import Flask, request, jsonify
import random, string

app = Flask(__name__)

shipments = {}

@app.route("/shipments", methods=["POST"])
def create_shipment():
    data = request.json
    tracking_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    data["id"] = tracking_id
    data["status"] = "Created"
    shipments[tracking_id] = data
    return jsonify(data), 201

@app.route("/shipments/<tracking_id>", methods=["GET"])
def get_shipment(tracking_id):
    shipment = shipments.get(tracking_id)
    if not shipment:
        return jsonify({"error": "Shipment not found"}), 404
    return jsonify(shipment)

@app.route("/shipments/<tracking_id>/status", methods=["PUT"])
def update_status(tracking_id):
    shipment = shipments.get(tracking_id)
    if not shipment:
        return jsonify({"error": "Shipment not found"}), 404
    new_status = request.json.get("status")
    shipment["status"] = new_status
    return jsonify(shipment)

if __name__ == "__main__":
    app.run(port=5002, debug=True)
