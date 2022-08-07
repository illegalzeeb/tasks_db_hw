import json
import sqlite3

import sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from mtd import db, User, Order, Offer

"""
Тут лежат функцмм
"""


def add_user(user_data_queue: dict):
    """
    Добавление пользователя в базу данных
    """
    #    with open('users.json', 'r', encoding='utf8') as file:
    for user in user_data_queue:
        current_user = User(**user)
        db.session.add(current_user)
    try:
        db.session.commit()
    except SQLAlchemy.exc.IntegrityError:
        print(f"INFO: Field with this id is already exists")


def add_order(order_data_queue: dict):
    """
    Добавление заказа в базу данных
    """
    for order in order_data_queue:
        current_order = Order(**order)
        db.session.add(current_order)
    try:
        db.session.commit()
    except SQLAlchemy.exc.IntegrityError:
        print(f"INFO: Field with this id is already exists")


def add_offer(offer_data_queue: dict):
    """
    Добавление предложения в базу данных
    """
    for offer in offer_data_queue:
        current_offer = Offer(**offer)
        db.session.add(current_offer)
    try:
        db.session.commit()
    except SQLAlchemy.exc.IntegrityError:
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
            return user
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
            return order
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
            return offer
    return "Offer does not exists"


def delete_user(user_id: int):
    """
    Удаляет пользователя по id
    """
    users_data_queue = get_users_all()
    for user in users_data_queue:
        if user.get('id') == user_id:
            db.session.delete(user)
            db.session.commit()


def update_user(user_data_queue: dict, user_id: int)
    """
    Удаляет пользователя по id, записывает на его место новую информацию
    """
    delete_user(user_id)
    add_user(user_data_queue)


def delete_order(order_id: int):
    """
    Удаляет заказ по id
    """
    orders_data_queue = get_orders_all()
    for order in orders_data_queue:
        if order.get('id') == order_id:
            db.session.delete(order)
            db.session.commit()


def update_order(order_data_queue: dict, order_id: int)
    """
    Удаляет заказ по id, записывает на его место новую информацию
    """
    delete_order(order_id)
    add_order(order_data_queue)


def delete_offer(offer_id: int):
    """
    Удаляет предложение по id
    """
    offers_data_queue = get_offers_all()
    for offer in offers_data_queue:
        if offer.get('id') == offer_id:
            db.session.delete(offer)
            db.session.commit()


def update_offer(offer_data_queue: dict, offer_id: int)
    """
    Удаляет предложение по id, записывает на его место новую информацию
    """
    delete_offer(offer_id)
    add_offer(offer_data_queue)