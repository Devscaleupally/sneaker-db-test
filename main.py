from flask import Flask
from web import routes as web_routes
from api import routes as api_routes

# Create the Flask app
app = Flask(__name__)

# Register the blueprints
app.register_blueprint(web_routes.web)
app.register_blueprint(api_routes.api)

if __name__ == '__main__':
    app.run()