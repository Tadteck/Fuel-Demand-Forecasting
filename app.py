from flask import Flask
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS  # Import CORS

# Import Blueprints
from routes.auth_routes import auth_bp
from routes.predict_routes import predict_bp
from routes.admin_routes import admin_bp
from routes.data_routes import data_bp

app = Flask(__name__)
app.config.from_object('config.Config')

jwt = JWTManager(app)

# Initialize Flask-Limiter
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# Enable CORS for Vite frontend
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:5173"],  # Vite default port
        "methods": ["GET", "POST", "PUT", "DELETE"],
        "allow_headers": ["Authorization", "Content-Type"]
    }
})

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(predict_bp, url_prefix='/api')
app.register_blueprint(admin_bp, url_prefix='/api/admin')
app.register_blueprint(data_bp)

if __name__ == '__main__':
    app.run(debug=True)