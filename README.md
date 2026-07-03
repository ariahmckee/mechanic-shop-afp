# Mechanic Shop API

Flask REST API for a mechanic shop service system. The app uses the application factory pattern, SQLAlchemy models, Marshmallow schemas, and separate blueprints for customers, mechanics, and service tickets (tickets).

## Features

- Customer, mechanic, and ticket CRUD routes
- Mechanic assignment and removal for tickets through the `ticket_mechanic` junction table
- Ticket responses with assigned `mechanic_ids`

## Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Marshmallow
- Marshmallow-SQLAlchemy
- MySQL Connector/Python
- MySQL

## Project Structure

```text
app/
  blueprints/
    customers/
    mechanics/
    tickets/
  __init__.py
  extensions.py
  models.py
app.py
config.py
requirements.txt
```

## Setup

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create the MySQL database:

```sql
CREATE DATABASE mechanic_db;
```

Update the database URI in `config.py` to agree with your local MySQL password, host, and database.

Run the app:

```bash
python app.py
```

The API runs at:

```text
http://127.0.0.1:5000
```

## Routes

### Customers

| Method | Endpoint | Description |
| --- | --- | --- |
| POST | `/customers/` | Create a customer |
| GET | `/customers/` | Get all customers |
| GET | `/customers/<customer_id>` | Get one customer |
| PUT | `/customers/<customer_id>` | Update a customer |
| DELETE | `/customers/<customer_id>` | Delete a customer |

Example customer payload:

```json
{
  "name": "Ada Lovelace",
  "email": "ada@example.com",
  "phone": 1112223333
}
```

### Mechanics

| Method | Endpoint | Description |
| --- | --- | --- |
| POST | `/mechanics/` | Create a mechanic |
| GET | `/mechanics/` | Get all mechanics |
| GET | `/mechanics/<mechanic_id>` | Get one mechanic |
| PUT | `/mechanics/<mechanic_id>` | Update a mechanic |
| DELETE | `/mechanics/<mechanic_id>` | Delete a mechanic |

Example mechanic payload:

```json
{
  "name": "Gino Jet",
  "email": "gjet@example.com",
  "phone": 2223334444,
  "salary": 90000
}
```

### Tickets

| Method | Endpoint | Description |
| --- | --- | --- |
| POST | `/tickets/` | Create a ticket |
| GET | `/tickets/` | Get all tickets |
| GET | `/tickets/<ticket_id>` | Get one ticket |
| PUT | `/tickets/<ticket_id>` | Update a ticket |
| DELETE | `/tickets/<ticket_id>` | Delete a ticket |
| PUT | `/tickets/<ticket_id>/assign-mechanic/<mechanic_id>` | Assign a mechanic to a ticket |
| PUT | `/tickets/<ticket_id>/remove-mechanic/<mechanic_id>` | Remove a mechanic from a ticket |

Example ticket payload:

```json
{
  "vin": "ABCDEFGHIJKL1234567890",
  "ticket_date": "1900-10-10",
  "ticket_desc": "Added NOS to the chair recline motor",
  "customer_id": 1
}
```

Example ticket response:

```json
{
  "id": 1,
  "vin": "ABCDEFGHIJKL1234567890",
  "ticket_date": "1900-10-10",
  "ticket_desc": "Added NOS to the chair recline motor",
  "customer_id": 1,
  "mechanic_ids": [1]
}
```

The assign and remove mechanic routes do not require a request body.

## Postman

Each route can be tested in Postman using the provided Postman collection file.

## Notes

- `customer_id` is required when creating or updating a ticket.
- Mechanic email and phone values must be unique.
- Customer email and phone values must be unique.
- `mechanic_ids` is returned in ticket responses and is managed through the assign/remove mechanic routes.
