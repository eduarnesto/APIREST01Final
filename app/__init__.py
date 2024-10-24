from flask import Flask
from flask_jwt_extended import JWTManager

from app.autores.routes import autoresBP
from app.libro.routes import librosBP

import string
import secrets

from app.users.routes import usersBP

alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(8))

app = Flask(__name__)

app.register_blueprint(autoresBP, url_prefix='/autores')
app.register_blueprint(librosBP, url_prefix='/libros')
app.register_blueprint(usersBP, url_prefix='/users')

app.config['SECRET_KEY'] = password

jwt = JWTManager(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)