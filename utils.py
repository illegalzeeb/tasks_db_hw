import json
import sqlite3

import sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from mtd import db, User, Order, Offer
from sqlalchemy import exc

"""
Тут лежат функцмм
"""


def add_user(user_data_queue: dict):
    """
    Добавление пользователя в базу данных
    """
    current_user = User(**user_data_queue)
    db.session.add(current_user)
    try:
        db.session.commit()
    except exc.IntegrityError:
        print(f"INFO: Field with this id is already exists")


def add_order(order_data_queue: dict):
    """
    Добавление заказа в базу данных
    """
    current_order = Order(**order_data_queue)
    db.session.add(current_order)
    try:
        db.session.commit()
    except exc.IntegrityError:
        print(f"INFO: Field with this id is already exists")


def add_offer(offer_data_queue: dict):
    """
    Добавление предложения в базу данных
    """
    current_offer = Offer(**offer_data_queue)
    db.session.add(current_offer)
    try:
        db.session.commit()
    except exc.IntegrityError:
        print(f"INFO: Field with this id is already exists")


def get_users_all() -> list[dict]:
    """
    Возвращает всех пользователей для роута /users
    """
    users_data = []
    for user in User.query.all():
        users_data.append(user.return_data())
    return users_data


def get_user_by_id(user_id: int) -> dict:
    """
    Возвращает пользователя для роута /users/user_id
    """
    users_data_queue = get_users_all()
    for user in users_data_queue:
        if user.get('id') == user_id:
            return User.query.get(user_id)
    return "User does not exists"


def get_orders_all() -> list[dict]:
    """
    Возвращает все заказы для роута /orders
    """
    orders_data = []
    for order in Order.query.all():
        orders_data.append(order.return_data())
    return orders_data


def get_order_by_id(order_id: int) -> dict:
    """
    Возвращает заказ для роута /orders/order_id
    """
    orders_data_queue = get_orders_all()
    for order in orders_data_queue:
        if order.get('id') == order_id:
            return Order.query.get(order_id)
    return "Order does not exists"


def get_offers_all() -> list[dict]:
    """
    Возвращает все предложения для роута /offers
    """
    offers_data = []
    for offer in Offer.query.all():
        offers_data.append(offer.return_data())
    return offers_data


def get_offer_by_id(offer_id: int) -> dict:
    """
    Возвращает предложение для роута /offers/offer_id
    """
    offers_data_queue = get_offers_all()
    for offer in offers_data_queue:
        if offer.get('id') == offer_id:
            return Offer.query.get(offer_id)
    return "Offer does not exists"


def delete_user(user_id: int):
    """
    Удаляет пользователя по id
    """
    user = get_user_by_id(user_id)
    db.session.delete(user)
    db.session.commit()


def update_user(user_data_queue: dict, user_id: int)
    """
    Обновляет данные пользователя
    """
    user = get_user_by_id(user_id)
    user.id = user_data_queue["id"]
    user.first_name = user_data_queue["first_name"]
    user.last_name = user_data_queue["last_name"]
    user.age = user_data_queue["age"]
    user.email = user_data_queue["email"]
    user.role = user_data_queue["role"]
    user.phone = user_data_queue["phone"]
    db.session.commit()


def delete_order(order_id: int):
    """
    Удаляет заказ по id
    """
    order = get_order_by_id(order_id)
    db.session.delete(order)
    db.session.commit()



def update_order(order_data_queue: dict, order_id: int)
    """
    Обновляет данные по заказу
    """
    order = get_order_by_id(order_id)
    order.id = order_data_queue["id"]
    order.name = order_data_queue["name"]
    order.description = order_data_queue["description"]
    order.start_date = order_data_queue["start_date"]
    order.end_date = order_data_queue["end_date"]
    order.address = order_data_queue["address"]
    order.price = order_data_queue["price"]
    order.customer_id = order_data_queue["customer_id"]
    order.executor_id = order_data_queue["executor_id"]
    db.session.commit()


def delete_offer(offer_id: int):
    """
    Удаляет предложение по id
    """
    offer = get_offer_by_id(offer_id)
    db.session.delete(offer)
    db.session.commit()


def update_offer(offer_data_queue: dict, offer_id: int)
    """
    Обновляет предложение
    """
    offer = get_offer_by_id(offer_id)
    offer.id = offer_data_queue["id"]
    offer.order_id = offer_data_queue["order_id"]
    offer.executor_id = offer_data_queue["executor_id"]
    db.session.commit()