from flask import Flask
from api.api import risk_types_blueprint
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(risk_types_blueprint)
CORS(app, support_credentials=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
