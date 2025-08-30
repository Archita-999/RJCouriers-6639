# RJCouriers-6639
# RJ Courier Services (Based on Monolithic architechture and Microservices architechture.)

# Monolithic Architechture 
RJ Courier is a monolithic web application designed to handle courier bookings, payments, tracking, and shipment management. 
It uses HTML, Bootstrap for frontend styling, and Flask with Jinja templating for backend logic.

1. Features

- Book Courier – Fill in sender, receiver, weight, and address
- Payment Gateway – Choose payment method and confirm booking
- Track Shipment – Enter tracking ID to view shipment status
- View All Shipments – Admin-style table of all bookings

2. Technologies Used

Service Area        Techniques / Tools Used         

 UI Design           HTML, Bootstrap 5               
 Templating          Jinja2 (Flask)                  
 Backend Logic       Python, Flask                   
 Architecture        Monolithic                      
 Data Handling       Python dictionaries (for demo)  

3. How to Run:
 i. Open your browser and go to
     http://localhost:5000

                                      
# Microservices Architechture
RJ Courier Microservices is a courier management system built using the microservices architecture. 
It is divided into separate services for users, shipments, payments, and the frontend interface. 
Each service runs independently and communicates through REST APIs.

Features Users Service – Stores and retrieves sender and receiver details 
Shipments Service – Creates bookings, generates tracking IDs, updates shipment status 
Payments Service – Records payments for bookings and marks them as paid 
Frontend Service – Provides the user interface for booking, payment, tracking, and viewing shipments

Technologies Used: 
UI Design – HTML, Bootstrap 5 (or React) 
Templating – Jinja2 (Flask) Backend Logic – Python,
Microservices Data Handling – Python dictionaries (demo storage)

How to Run:
i. Open four terminals 
ii. Run each service:  
python users-service/main.py  
python shipments-service/main.py  
python payments-service/main.py  
python frontend-service/main.py 
iii. Open your browser and go to 
http://localhost:5000

                                                                   
