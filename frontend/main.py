from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

USERS_API = "http://127.0.0.1:5001"
SHIPMENTS_API = "http://127.0.0.1:5002"
PAYMENTS_API = "http://127.0.0.1:5003"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/book", methods=["GET", "POST"])
def book():
    if request.method == "POST":
        sender = request.form["sender"]
        receiver = request.form["receiver"]
        weight = request.form["weight"]
        address = request.form["address"]

        # Call shipments API
        res = requests.post(f"{SHIPMENTS_API}/shipments", json={
            "sender": sender,
            "receiver": receiver,
            "weight": weight,
            "address": address
        })
        shipment = res.json()
        return redirect(f"/payment/{shipment['id']}")
    return render_template("book.html")

@app.route("/payment/<tracking_id>", methods=["GET", "POST"])
def payment(tracking_id):
    if request.method == "POST":
        name = request.form["name"]
        amount = request.form["amount"]
        method = request.form["method"]

        # Call payments API
        requests.post(f"{PAYMENTS_API}/payments", json={
            "name": name,
            "amount": amount,
            "method": method,
            "tracking_id": tracking_id
        })

        return render_template("payment.html", paid=True, tracking_id=tracking_id)

    return render_template("payment.html", paid=False, tracking_id=tracking_id)

@app.route("/track", methods=["GET", "POST"])
def track():
    shipment = None
    if request.method == "POST":
        tracking_id = request.form["tracking_id"]
        res = requests.get(f"{SHIPMENTS_API}/shipments/{tracking_id}")
        if res.status_code == 200:
            shipment = res.json()
    return render_template("track.html", shipment=shipment)

@app.route("/status")
def status():
    res = requests.get(f"{SHIPMENTS_API}/shipments/XYZ")  # Example
    return render_template("status.html")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
