from app import create_app
from app.models import db

app = create_app('DevelopmentConfig')


if __name__ == "__main__":
    # Create the tables before starting the development server.
    with app.app_context():
        db.create_all()
        
    app.run()
