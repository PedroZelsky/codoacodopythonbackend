from flask import jsonify, request
from app.models import User
from email_validator import validate_email

def index():
    response = {'message':'Hola comisión 24163 - [Imagine una bella página de inicio aquí 😂]'}
    return jsonify(response)

def get_users():
    users = User.get_all()
    return jsonify([user.serialize() for user in users])

def get_user(email):
    user = User.get_user(email)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(user.serialize())

def register():
    data = request.json

    # VALIDACIONES
    print("Validating request:")

    if validate_email(data['email']):
        print("Valid email address")
    else:
        return jsonify({'message':'Invalid email address'}), 500

    # agregar mas validaciones

    new_user = User(data['nombre'],data['apellido'],data['email'],data['password'])
    new_user.register()
    response = {'message':'Usuario creada con exito'}
    return jsonify(response) , 201


def delete_user(email):
    user = User.get_user(email)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    user.unregister()
    return jsonify({'message': 'User deleted successfully'})
