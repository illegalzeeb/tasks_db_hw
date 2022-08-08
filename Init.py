import json

import sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import exc
from mtd import User, Order, Offer


app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dtb.db"
#app.config['DEBUG'] = True
# app.register_blueprint(main_blueprint)

"""
Заполнение таблиц данными из json файлов
"""

db = SQLAlchemy()

with open('users.json', 'r', encoding='utf8') as file:
#    print(file)
    users = json.load(file)
#    print(users)
    for user in users:
#        print(user)
        current_user = User(**user)
#        print(current_user)
        db.session.add(current_user)
    try:
        db.session.commit()
    except exc.IntegrityError:
        print(f"INFO: Table already initialized and filled")


with open('orders.json', 'r', encoding='utf8') as file:
    orders = json.load(file)
    for order in orders:
        current_order = Order(**order)
        db.session.add(current_order)
    try:
        db.session.commit()
    except exc.IntegrityError:
        print(f"INFO: Table already initialized and filled")


with open('offers.json', 'r', encoding='utf8') as file:
    offers = json.load(file)
    for offer in offers:
        current_offer = Offer(**offer)
        db.session.add(current_offer)
    try:
        db.session.commit()
    except exc.IntegrityError:
        print(f"INFO: Table already initialized and filled")



#app.run()