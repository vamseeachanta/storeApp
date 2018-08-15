import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate
from security import identity

# Import Resources
from resources.user import UserRegister
from resources.item import Item
from resources.item import ItemList
from resources.store import Store
from resources.store import StoreList

#  __name__ gives each file a unique name
app = Flask(__name__)
# Make a URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
# Turn off default Flask tracking. SQLAlchmey has its own active tracking system
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'AceEngineer@2020'
api = Api(app)

# jwt creates a new end point "/auth"
jwt = JWT(app, authenticate, identity)

# http://127.0.0.1:5000/item/<string>:name
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(ItemList, '/items')

api.add_resource(UserRegister, '/register')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    # Specifies port to run the app
    app.run(port=5000)
