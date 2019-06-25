import os
from flask import Flask
from flask_restful import Api
from Resource.item import Item, Items
from Resource.user import Register
from Resource.store import Store
from flask_jwt import JWT
from sercurity import identity, authenticate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
app.secret_key = 'he'


jwt = JWT(app, authenticate, identity)
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Register, '/register')
api.add_resource(Items, '/items')
api.add_resource(Store, '/store/<string:name>')

if __name__ == '__main__':
    from createDB import db
    db.init_app(app)
    app.run(port=5000)
