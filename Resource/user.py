from flask_restful import Resource, reqparse
from Model.user_model import UserModel

class Register(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='This can\'t be left blank')
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='This can\'t be left blank')

    def post(self):

        data = self.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return 'Username {} already exists'.format(data['username'])

        user = UserModel(data['username'], data['password'])
        user.save_to_db()
        return 'DONE'
