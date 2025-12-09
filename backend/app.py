from flask import Flask
from database import init_db
from blueprints.news import news_bp
from blueprints.sports import sports_bp
from blueprints.economy import economy_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Initialize SQLite DB
init_db()

# Register blueprints
app.register_blueprint(news_bp)
app.register_blueprint(sports_bp)
app.register_blueprint(economy_bp)

@app.get("/")
def home():
    return {
        "message": "API is running!",
        "routes": ["/news", "/sports", "/economy"]
    }

if __name__ == "__main__":
    app.run(debug=True)
