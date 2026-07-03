from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import date
from typing import List

# Create a base class for our models
class Base(DeclarativeBase):
    pass

# Instantiate your SQLAlchemy database
db = SQLAlchemy(model_class = Base)


# # Clear the table for a fresh start
# with app.app_context():
#     db.clear_all()

class Customer(Base):
    __tablename__ = 'customers'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    email: Mapped[str] = mapped_column(db.String(360), nullable=False, unique=True)
    phone: Mapped[int] = mapped_column(nullable=False, unique=True)
    
    
    tickets: Mapped[List['Ticket']] = db.relationship(back_populates='customer')

ticket_mechanic = db.Table(
    'ticket_mechanic',
    Base.metadata,
    db.Column('ticket_id', db.ForeignKey('tickets.id')),
    db.Column('mechanic_id', db.ForeignKey('mechanics.id'))
)

class Ticket(Base):
    __tablename__ = 'tickets'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    vin: Mapped[str] = mapped_column(db.String(255),nullable=False)
    ticket_date: Mapped[date] = mapped_column(db.Date)
    ticket_desc: Mapped[str]= mapped_column(db.String(255),nullable=False)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey('customers.id'))
    
    customer: Mapped['Customer'] = db.relationship(back_populates='tickets')   # <---- I think this needs to be 'tickets' to match the relationship attribute in Customer class(?) (lesson had it as singular here)
    mechanics: Mapped[List['Mechanic']] = db.relationship(secondary=ticket_mechanic, back_populates='tickets')
    
class Mechanic(Base):
    __tablename__ = 'mechanics'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    email: Mapped[str] = mapped_column(db.String(360), nullable=False, unique=True)
    phone: Mapped[int] = mapped_column(nullable=False, unique=True)
    salary: Mapped[float]
    
    tickets: Mapped[List['Ticket']] = db.relationship(secondary=ticket_mechanic, back_populates='mechanics')