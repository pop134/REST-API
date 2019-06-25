from flask_restful import Resource, reqparse
from Model.item_model import ItemModel
from flask_jwt import jwt_required

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help='This can\'t be left blank')
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This can\'t be left blank')
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help='An item must have a store id')

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item
        return 'Cant find item: {}'.format(name)

    def post(self, name):
        if ItemModel.find_by_name(name):
            return 'Item: {} already exists'.format(name)

        data = self.parser.parse_args()
        item = ItemModel(name, data['price'], data['store_id'])
        item.save_to_db()
        return 'Inserted item {}'.format(name)

    def put(self, name):
        data = self.parser.parse_args()
        item = ItemModel(name, data['price'], data['store_id'])
        if ItemModel.find_by_name(name):
            item.save_to_db()
            return 'Updated item: {}'.format(name)
        else:
            item.save_to_db()
            return 'Inserted item {}'.format(name)

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            ItemModel.delete_from_db(item)
            return 'Deleted item: {}'.format(name)
        return 'Cant find item {}'.format(name)


class Items(Resource):

    def get(self):
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
