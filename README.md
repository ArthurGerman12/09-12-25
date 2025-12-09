# Flask Multi-Module CRUD API with SQLite and HTML Frontend

This project is a simple Flask application that provides CRUD APIs for three modules:

- News
- Sports
- Economy

It also includes a basic HTML frontend (using Axios) for interacting with each module.  
A SQLite database (`data.db`) is automatically created and seeded on first run.

------------------------------------------------------------

## Project Structure

project/
│
├── app.py
├── database.py
├── data.db                 (auto-created)
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

------------------------------------------------------------

## Features

1. REST API with full CRUD functionality for:
   - /news
   - /sports
   - /economy

2. SQLite database with automatic initialization.

3. Seed data inserted only if tables are empty:
   - 3 news articles
   - 3 sports matches
   - 3 economy market entries

4. HTML frontend using Axios for:
   - Displaying items
   - Creating new items
   - Deleting items

------------------------------------------------------------

## Installation

1. Clone the repository:

   git clone <your-repo-url>
   cd <project-folder>

2. Create a virtual environment (optional but recommended):

   python3 -m venv venv
   source venv/bin/activate     (macOS / Linux)
   venv\Scripts\activate        (Windows)

3. Install dependencies:

   pip install flask

4. Run the application:

   python app.py

5. Open the frontend pages directly in a browser:

   index.html
   news.html
   sports.html
   economy.html

------------------------------------------------------------

## API Endpoints

### News
GET    /news  
GET    /news/<id>  
POST   /news  
PUT    /news/<id>  
DELETE /news/<id>  

### Sports
GET    /sports  
GET    /sports/<id>  
POST   /sports  
PUT    /sports/<id>  
DELETE /sports/<id>  

### Economy
GET    /economy  
GET    /economy/<id>  
POST   /economy  
PUT    /economy/<id>  
DELETE /economy/<id>  

------------------------------------------------------------

## Seed Data (Inserted Automatically)

### News
- "Breaking News: Python Takes Over"
- "Flask 3.0 Released"
- "Tech Market Surges"

### Sports
- "Lakers vs Bulls" (102-97)
- "Arsenal vs Chelsea" (2-1)
- "Patriots vs Dolphins" (24-20)

### Economy
- NASDAQ (Green)
- DOW JONES (Red)
- S&P 500 (Neutral)

------------------------------------------------------------

## Requirements

- Python 3.x
- Flask
- SQLite (built-in)

------------------------------------------------------------

## Notes

- The database file is created automatically on first run.
- Seed data is only inserted if the corresponding table is empty.
- HTML files use Axios for communicating with the Flask backend.

------------------------------------------------------------

## License

MIT License
