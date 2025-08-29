from flask import Flask
from flask_cors import CORS
from controllers.bfhl_controller import bfhl_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(bfhl_bp, url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True)
