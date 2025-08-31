# RJCouriers-6639
# RJ Courier Services

Microservices Architechture
RJ Courier Microservices is a courier management system built using the microservices architecture. 
It is divided into separate services for users, shipments, payments, and the frontend interface. 
Each service runs independently and communicates through REST APIs.

Features Users Service – Stores and retrieves sender and receiver details 
Shipments Service – Creates bookings, generates tracking IDs, updates shipment status 
Payments Service – Records payments for bookings and marks them as paid Frontend Service – Provides the user interface for booking, payment, tracking, and viewing shipments

Technologies Used: UI Design – HTML, Bootstrap 5 (or React) Templating – Jinja2 (Flask) Backend Logic – Python, Microservices Data Handling – Python dictionaries (demo storage)

How to Run: 
i. Open four terminals 
ii. Run each service:   
   python users-service/main.py   
   python shipments-service/main.py   
   python payments-service/main.py   
   python frontend-service/main.py 

iii. Open your browser and go to http://localhost:5000

