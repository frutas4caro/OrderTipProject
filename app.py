from flask import Flask
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='OrderAPI', description='My Simple Order API')

ns = api.namespace('ordersApi', description='Orders operations')

order = api.model('Order', {
    'id': fields.Integer(readOnly=True, description='The order id'),
    'name': fields.String(required=True, description='The name of the person who placed the order'),
    'amount': fields.String(required=True, description='The cost of the order'),
    'tip': fields.String(required=False, description='Tip paid by those placing the order'),
    'server': fields.String(reequired=True, description='The person who delivered the order'),
    'tipStatus': fields.String(required=False,
                               description='The status of the tip, NOT_RECEIVED, RECEIVED, PAID_TO_SERVER')
})


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
