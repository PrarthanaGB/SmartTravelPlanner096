from flask import Flask, send_from_directory
from flask_cors import CORS
from config import Config
from database import init_database

frontend_dir = "../frontend"
app = Flask(__name__, static_folder=frontend_dir, static_url_path="/static")
app.secret_key = Config.SECRET_KEY
CORS(app)

# Initialize database
init_database()

# Import routes after setting up db
from routes.user_routes import user_bp
from routes.ai_routes import ai_bp

app.register_blueprint(user_bp)
app.register_blueprint(ai_bp)

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    app.run(debug=True)
