from sqlalchemy import select
from flask import jsonify, request
from marshmallow import ValidationError
from app.models import Customer, Ticket, db
from .schemas import ticket_schema, tickets_schema
from . import tickets_bp

# CREATE NEW SERVICE TICKET
@tickets_bp.route("/", methods=['POST'])
def create_ticket():
    try:
        # ticket_schema.load(request.json) handles deserialization and validation of incoming data.
        ticket_data = ticket_schema.load(request.json)
    # If validation fails, a ValidationError is raised and handled with a 400 response.
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    customer = db.session.get(Customer, ticket_data['customer_id'])
    if not customer:
        return jsonify({"error": "Customer not found."}), 404
    
    new_ticket = Ticket(**ticket_data)
    db.session.add(new_ticket)
    db.session.commit()
    return ticket_schema.jsonify(new_ticket), 201

# GET ALL TICKETS
@tickets_bp.route("/", methods=['GET'])
def get_tickets():
    query = select(Ticket)
    tickets = db.session.execute(query).scalars().all()
    
    return tickets_schema.jsonify(tickets)

# GET SPECIFIC TICKET
@tickets_bp.route("/<int:ticket_id>", methods=['GET'])
def get_ticket(ticket_id):
    ticket = db.session.get(Ticket, ticket_id)
    
    if ticket:
        return ticket_schema.jsonify(ticket), 200
    return jsonify({"error": "Ticket not found."}), 404

# UPDATE SPECIFIC TICKET
@tickets_bp.route("/<int:ticket_id>", methods=['PUT'])
def update_ticket(ticket_id):
    ticket = db.session.get(Ticket, ticket_id)
    
    if not ticket:
        return jsonify({"error": "Ticket not found."}), 404
    
    try:
        ticket_data = ticket_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    customer = db.session.get(Customer, ticket_data['customer_id'])
    if not customer:
        return jsonify({"error": "Customer not found."}), 404
    
    for key, value in ticket_data.items():
        setattr(ticket, key, value)
        
    db.session.commit()
    return ticket_schema.jsonify(ticket), 200

# DELETE SPECIFIC TICKET <---assignment is saying you don't need to delete a service ticket, becuase "why would you want to, you always want to retain service tickets, but you could've created a wrong one that needs to be deleted (I can see many reasons to need to delete a ticket, so leaving this in here)"
@tickets_bp.route("/<int:ticket_id>", methods=['DELETE'])
def delete_ticket(ticket_id):
    ticket = db.session.get(Ticket, ticket_id)
    
    if not ticket:
        return jsonify({"error": "Ticket not found."}), 404
    
    db.session.delete(ticket)
    db.session.commit()
    return jsonify({"message": f'Ticket id: {ticket_id}, successfully deleted.'}), 200
