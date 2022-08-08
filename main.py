from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from views import main_blueprint

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dtb.db"
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(main_blueprint)
db = SQLAlchemy(app)
db.init_app(app)

app.run()
