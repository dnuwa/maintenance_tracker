from flask import Flask
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser

app = Flask(__name__)
api= Api(app, prefix="/api/v1")

app_users = [
    {"email":"daniel.nuwa@gmail.com", "password":"1234", "id": 1},{"email":"danielnuwa84@gmail.com", "password":"65426", "id": 2}
]

main_req = [ 
    {"item":"Motobike(Suzzuki)", "issue":"Wornout tires", "issue_details":"On a rainny day the bike slides all over the palce", "status":"", "id": 1}
]

#helper method to iterate through to access a request by id
def get_item_by_id(req_id):
    for req in main_req:
        if req.get("id") == int(req_id):
            return req

user_request_parser = RequestParser(bundle_errors=True)
user_request_parser.add_argument("email", type=str, required=True, help="Name has to be valid string")
user_request_parser.add_argument("password", required=True)
user_request_parser.add_argument("id", type=int, required=True, help="Please enter valid integer as ID")

mainreq_request_parser = RequestParser(bundle_errors=True)
mainreq_request_parser.add_argument("item", type=str, required=True, help="item has to be valid string")
mainreq_request_parser.add_argument("issue", type=str, required=True, help="issue has to be valid string")
mainreq_request_parser.add_argument("issue_details", type=str, required=True, help="details must be a valid string")
mainreq_request_parser.add_argument("status", required=True)
mainreq_request_parser.add_argument("id", type=int, required=True, help="Please enter valid integer as ID")

# #test class
# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}
#users class
class UserCollection(Resource):
    #method to get all users signed up
    def get(self):
        for one in app_users:
            return one

    #method to cater for user sign up
    def post(self):
        args = user_request_parser.parse_args()
        app_users.append(args)
        return {"msg": "User added", "user_data": args}

#requests class
class MaintenanceRequests(Resource):
    
    #method to create a request
    def post(self):
        arguments = mainreq_request_parser.parse_args()
        main_req.append(arguments)
        return {"msg": "Request added", "Request_data": arguments}
    #method to fetch all the requests
    def get(self):
        for one in main_req:
            return one

#class to make updates on the requests
class Maintenance(Resource):
    #method to make cahnges to a request accessed by its id
    def put(self, id):
        arguments = mainreq_request_parser.parse_args()
        req = get_item_by_id(id)
        if req:
            main_req.remove(req)
            main_req.append(arguments)

        return arguments        

    #accessing a particular request using its id
    def get(self, id):
        req = get_item_by_id(id)
        if not req:
            return {"error": "request not found"}
        return req

api.add_resource(HelloWorld, '/')
api.add_resource(UserCollection, '/users')

api.add_resource(MaintenanceRequests, '/user/request')
api.add_resource(Maintenance, '/user/request/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)