import json

import sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import exc

# from views import main_blueprint

"""
Тут лежат модели и единожды генерируется база данных из Json-файлов
"""

app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dtb.db"
#app.config['DEBUG'] = True
# app.register_blueprint(main_blueprint)
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    role = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def return_data(self):
        """
        Возвращает данные пользователя в виде словаря
        """

        return {"id": self.id,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age,
                "email": self.email,
                "role": self.role,
                "phone": self.phone}


class Order(db.Model):
    __tablename__ = "Order"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    start_date = db.Column(db.Integer)
    end_date = db.Column(db.Integer)
    address = db.Column(db.String(100))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey("User.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("User.id"))


    def return_data(self):
        """
        Возвращает данные заказа в виде словаря
        """

        return {"id": self.id,
                "name": self.name,
                "description": self.description,
                "start_date": self.start_date,
                "end_date": self.end_date,
                "address": self.address,
                "price": self.price,
                "customer_id": self.customer_id,
                "executor_id": self.executor_id}


class Offer(db.Model):
    __tablename__ = "Offer"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("Order.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("User.id"))


    def return_data(self):
        """
        Возвращает данные предложения в виде словаря
        """

        return {"id": self.id,
                "order_id": self.order_id,
                "executor_id": self.executor_id}

db.create_all()
"""
Заполнение таблиц данными из json файлов
"""
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
