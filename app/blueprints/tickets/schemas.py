from app.extensions import ma
from app.models import Ticket


class TicketSchema(ma.SQLAlchemyAutoSchema):
    mechanic_ids = ma.Method("get_mechanic_ids", dump_only=True)
    
    class Meta:
        model = Ticket
        include_fk = True
        
    def get_mechanic_ids(self, ticket):
        return [mechanic.id for mechanic in ticket.mechanics]
        
ticket_schema = TicketSchema()
tickets_schema = TicketSchema(many=True)
