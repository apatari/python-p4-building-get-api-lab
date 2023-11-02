#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from sqlalchemy import desc

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h2> Something </h2>'

    

@app.route('/bakeries')
def bakeries():
    bakeries = []
    for bakery in Bakery.query.all():
        bakeries.append(bakery.to_dict())
    body = bakeries

    return body

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakery = Bakery.query.filter_by(id=id).first().to_dict()
    return jsonify(bakery)

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    goods = []
    for good in BakedGood.query.order_by(desc('price')).all():
        goods.append(good.to_dict())
    return goods

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    return BakedGood.query.order_by(desc('price')).first().to_dict()

if __name__ == '__main__':
    app.run(port=5555, debug=True)
