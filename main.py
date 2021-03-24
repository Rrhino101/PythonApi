from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

contact_put_args = reqparse.RequestParser()
contact_put_args.add_argument("name", type=str, help="The contact's NAME is required", required=True)
contact_put_args.add_argument("phone", type=str, help="The contact's NUMBER is required", required=True)
contact_put_args.add_argument("email", type=str, help="The contact's EMAIL is required", required=True)

## name, email, and phone number
contacts = {}

class PhoneBook(Resource):
    def get(self, contact_id):
        return contacts[contact_id]

    def put(self, contact_id):
        contact_already_exists(contact_id)
        args = contact_put_args.parse_args()
        contacts[contact_id] = args
        return contacts[contact_id], 201

    def delete(self, contact_id):
        contact_doesnt_exist(contact_id)
        del contacts[contact_id]
        return contact_id+' has been deleted', 201

    def update(self, contact_id):
        delete(self, contact_id)
        put(self, contact_id)
        return contact_id+' has been updated', 201

def contact_doesnt_exist(contact_id):
    if contact_id not in contacts:
        abort(404, message="Contact does not exist")

def contact_already_exists(contact_id):
    if contact_id in contacts:
        abort(409, message="Contact already exists")

api.add_resource(PhoneBook, "/phonebook/<int:contact_id>")

if __name__ =="__main__":
    app.run(debug=True)

