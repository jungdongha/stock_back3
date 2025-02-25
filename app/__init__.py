from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": ["http://localhost:3000"]}})

    from app.routes import main
    app.register_blueprint(main, url_prefix='/api')

    return app
