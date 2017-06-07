from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store
from resources.annonce import Annonce, AnnonceList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ecpyv5a79ekacjpe:bg2h7jguvyvoh87m@irkm0xtlo2pcmvvz.chr7pe7iynqr.eu-west-1.rds.amazonaws.com:3306/xxdzsrzpx3uk4b9f'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Annonce, '/annonce/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(AnnonceList, '/annonces')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
