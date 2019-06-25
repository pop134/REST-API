from flask_restful import Resource, reqparse
from Model.store_model import StoreModel


class Store(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help='This can\'t be left blank')

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return 'Cant find store: {}'.format(name)

    def post(self, name):
        if StoreModel.find_by_name(name):
            return 'Store: {} already exists'.format(name)

        data = self.parser.parse_args()
        store = StoreModel(data['name'])
        store.save_to_db()
        return 'Created store: {}'.format(name)

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            StoreModel.delete_from_db(store)
            return 'Removed store: {}'.format(name)
        return 'Cant find store: {}'.format(name)