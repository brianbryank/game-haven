from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///gamehave.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR']= True

CORS(app)

migrate = Migrate(app, db)
api = Api(app)

db.init_app(app)

api = Api(app)



if __name__ == "__main__":
 app.run(port=5555, debug=True)


