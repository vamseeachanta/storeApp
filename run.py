from app import app
from db import db

db.init_app(app)

# Utilize Flask to create libraries. Runs before it commits the first request.
@app.before_first_request
def create_tables():
    db.create_all()