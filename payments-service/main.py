from flask import Flask, request, jsonify

app = Flask(__name__)

payments = {}

@app.route("/payments", methods=["POST"])
def make_payment():
    data = request.json
    payment_id = len(payments) + 1
    payments[payment_id] = data
    return jsonify({"id": payment_id, "data": data, "status": "Paid"}), 201

if __name__ == "__main__":
    app.run(port=5003, debug=True)
