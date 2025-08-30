from flask import Flask, render_template, request, redirect, session
import random, string

app = Flask(__name__)
app.secret_key = "rjcouriersecret"

# In-memory DB simulation
shipments = {}

# Home page
@app.route("/")
def home():
    return render_template("home.html")

# Track shipment
@app.route("/track", methods=["GET", "POST"])
def track():
    shipment = None
    if request.method == "POST":
        tracking_id = request.form["tracking_id"]
        shipment = shipments.get(tracking_id)
    return render_template("track.html", shipment=shipment)

# Book courier
@app.route("/book", methods=["GET", "POST"])
def book():
    if request.method == "POST":
        sender = request.form["sender"]
        receiver = request.form["receiver"]
        weight = request.form["weight"]
        address = request.form["address"]

        session["booking"] = {
            "sender": sender,
            "receiver": receiver,
            "weight": weight,
            "address": address
        }

        return redirect("/payment")

    return render_template("book.html")

# Payment
@app.route("/payment", methods=["GET", "POST"])
def payment():
    booking = session.get("booking")
    paid = False
    tracking_id = None

    if request.method == "POST":
        name = request.form["name"]
        amount = request.form["amount"]
        method = request.form["method"]
        paid = True

        # Generate Tracking ID
        tracking_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

        # Save shipment in memory
        shipments[tracking_id] = {
            "id": tracking_id,
            "sender": booking["sender"],
            "receiver": booking["receiver"],
            "weight": booking["weight"],
            "address": booking["address"],
            "payment": method,
            "status": "Created",
            "history": ["Created"]
        }

        # Clear booking session
        session.pop("booking", None)

    return render_template("payment.html", booking=booking, paid=paid, tracking_id=tracking_id)

# Status page
@app.route("/status")
def status():
    return render_template("status.html", shipments=shipments)

if __name__ == "__main__":
    app.run(debug=True)
