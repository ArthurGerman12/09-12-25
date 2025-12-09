📘 Flask Multi-Module CRUD API + HTML Frontend
This project is a simple, modular Flask application featuring:
Three API modules (Blueprints)
/news — CRUD for news articles
/sports — CRUD for sports matches
/economy — CRUD for market/economy items
SQLite database (data.db) with automatic table creation and seed data
Static HTML frontend using Axios to interact with each API
index.html
news.html
sports.html
economy.html
This project is designed for learning, demos, and lightweight API-based applications.
📁 Project Structure
project/
│
├── app.py
├── database.py
├── data.db                (auto-created)
│
├── blueprints/
│   ├── news.py
│   ├── sports.py
│   └── economy.py
│
├── index.html
├── news.html
├── sports.html
└── economy.html
🚀 Features
✔ REST API (Flask)
Each module has full CRUD:
Route	Method	Description
/news	GET	Get all news
/news/<id>	GET	Get single news
/news	POST	Create news
/news/<id>	PUT	Update news
/news/<id>	DELETE	Delete news
(Sports and Economy follow the exact same structure.)
✔ SQLite Database With Seeding
data.db is automatically created on first run.
init_db() creates:
news table (with 3 initial articles)
sports table (with 3 matches)
economy table (with 3 market entries)
✔ HTML Frontend (Axios Powered)
Each HTML page includes:
Header navigation
Form to create a new item
Display of all items
Delete buttons
Auto-refresh after updates
🛠 Installation & Setup
1. Clone the project
git clone <your-repo-url>
cd <project-folder>
2. Create a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
3. Install dependencies
pip install flask
4. Run the server
python app.py
5. Open the frontend
Just open these files directly in the browser:
index.html
news.html
sports.html
economy.html
Or serve them from a simple HTTP server:
python -m http.server
🔥 API Endpoints Overview
News Module
GET    /news
GET    /news/<id>
POST   /news
PUT    /news/<id>
DELETE /news/<id>
Sports Module
GET    /sports
GET    /sports/<id>
POST   /sports
PUT    /sports/<id>
DELETE /sports/<id>
Economy Module
GET    /economy
GET    /economy/<id>
POST   /economy
PUT    /economy/<id>
DELETE /economy/<id>
🧪 Sample Seed Data
News
Breaking News: Python Takes Over
Flask 3.0 Released
Tech Market Surges
Sports
Lakers vs Bulls — 102-97
Arsenal vs Chelsea — 2-1
Patriots vs Dolphins — 24-20
Economy
NASDAQ — Green
DOW JONES — Red
S&P 500 — Neutral
🧩 How It Works
When app.py starts → init_db() runs
If any table is empty → the app inserts seed records
Blueprints handle routing logic
HTML files communicate using Axios to the Flask API
📌 Technologies Used
Python 3
Flask
SQLite3
Axios (frontend fetcher)
HTML/CSS
💡 Future Improvements (Ideas)
Add Bootstrap or Tailwind for prettier UI
Add edit/update UI on HTML pages
Add login/authentication
Convert frontend into a React or Vue app
Add Docker support
📄 License
MIT License — feel free to use, modify, and share.
