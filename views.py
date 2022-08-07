import json

from utils import get_users_all, get_user_by_id, get_orders_all, get_order_by_id, get_offers_all, get_offer_by_id, \
    add_user, update_user, delete_user, add_order, update_order, delete_order, add_offer, update_offer, delete_offer
from flask import Blueprint, render_template, request, jsonify

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')



@main_blueprint.route("/users/", methods=['GET', 'POST'])
def users_page():
    if request.method == 'GET':
        return json.dumps(get_users_all())
    elif request.method == 'POST':
        add_user(request.json)


@main_blueprint.route("/users/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def user_by_id_page(user_id):
    if request.method == 'GET':
        return json.dumps(get_user_by_id(user_id))
    elif request.method == 'PUT':
        update_user(request.json, user_id)
        return "Пользователь обновлен"
    elif request.method == 'DELETE':
        delete_user(user_id)
        return "Пользователь удален"


@main_blueprint.route("/orders/", methods=['GET', 'POST'])
def orders_page():
    if request.method == 'GET':
        return json.dumps(get_orders_all())
    elif request.method == 'POST':
        add_order(request.json)


@main_blueprint.route("/orders/<int:order_id>", methods=['GET', 'PUT', 'DELETE'])
def order_by_id_page(order_id):
    if request.method == 'GET':
        return json.dumps(get_order_by_id(order_id))
    elif request.method == 'PUT':
        update_order(request.json, order_id)
        return "Заказ обновлен"
    elif request.method == 'DELETE':
        delete_order(order_id)
        return "Заказ удален"


@main_blueprint.route("/offers/", methods=['GET', 'POST'])
def offers_page():
    if request.method == 'GET':
        return json.dumps(get_offers_all())
    elif request.method == 'POST':
        add_offer(request.json)


@main_blueprint.route("/offers/<int:offer_id>", methods=['GET', 'PUT', 'DELETE'])
def offer_by_id_page(offer_id):
    if request.method == 'GET':
        return json.dumps(get_offer_by_id(offer_id))
    elif request.method == 'PUT':
        update_offer(request.json, offer_id)
        return "Предложение обновлено"
    elif request.method == 'DELETE':
        delete_offer(offer_id)
        return "Предложение удалено"