from flask import Flask
from app.views import *
from app.database import init_app
from flask_cors import CORS

#inicializacion de la apliacion con Flask
app = Flask(__name__)

init_app(app)
#permitir solicitudes desde cualquier origin
CORS(app)

#registrar una ruta asociada a una vista
app.route('/',methods=['GET'])(index)
app.route('/api/login/',methods=['POST'])(authenticate)
app.route('/api/register/',methods=['POST'])(register)
app.route('/api/validate/<email>', methods=['GET'])(get_user)
app.route('/api/unregister/<email>', methods=['DELETE'])(unregister)

if __name__ == '__main__':
    app.run(debug=True)