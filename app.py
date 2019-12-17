from flask import Flask
from flask_restplus import Api, Resource, fields
from datetime import datetime


app = Flask(__name__)
api = Api(app, version='1.0', title='OrderAPI', description='My Simple Order API')

ns = api.namespace('ordersApi', description='Orders operations')

order = api.model('Orders', {
    'id': fields.Integer(readOnly=True, description='The order id'),
    'name': fields.String(required=True, description='The name of the person who placed the order'),
    'amount': fields.String(required=True, description='The cost of the order'),
    'server': fields.String(required=True, description='The person who delivered the order'),
    'date': fields.String(required=True, description='The Data when the order was placed')
})


# def get_timestamp():
#     return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class OrderDAO(object):
    def __init__(self):
        self.orders = []
        self.counter = 0

    def get(self):
        return self.orders

    def get(self, order_id):
        for order in self.orders:
            if order['id'] == order_id:
                return order
        api.abort(404, "Order with Id {} doesn't exist".format(order_id))

    def create(self, data):
        order= data
        order['name'] = data['name']
        order['amount'] = data['amount']
        order['server'] = data['server']
        # # TODO: Need to require a specific date format and prettify as needed.
        order['date'] = data['date']
        order['id'] = self.counter = self.counter + 1

        self.orders.append(order)
        return order

    def update(self, order_id, name, amount, server, date):
        order = self.get(order_id)
        if name != order['name']:
            order['name'] = name
        if amount != order['amount']:
            order['amount'] = amount
        if server != order['server']:
            order['server'] = server
        if date is not None & date != order['date']:
            order['date'] = date
        return order

    def delete(self, order_id):
        order = self.get(order_id)
        self.orders.remove(order)


DAO = OrderDAO()
DAO.create({'name': 'Bob', 'amount': '25.75', 'server': 'Leslie', 'date': 'today'})
DAO.create({'name': 'Bob', 'amount': '25.75', 'server': 'Leslie', 'date': 'today'})
# DAO.create('Linda', '105.00', 'Leslie')
# DAO.create('Timothy', '10.50', 'Barb')


@ns.route('/')
@ns.doc('Order Details')
class Order(Resource):
    """Shows a list of all the Orders and lets you add a new one"""

    @ns.doc('Order List')
    @ns.marshal_list_with(order)
    def get(self):
        """list of all orders"""
        return DAO.orders

    @ns.doc('create_order')
    @ns.expect(order)
    @ns.marshal_with(order, code=201)
    def post(self):
        """Create new order"""
        return DAO.create(ns.payload), 201


# @app.route('/')
# def hello_world():
#     return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
