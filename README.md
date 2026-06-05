# ExpenseTrack

A full stack expense tracking web application built with Python, Flask, PostgreSQL, and AWS RDS. Features a live dashboard with Chart.js visualizations.

## Project Structure

expensetrack/
├── app.py          → Flask routes and application entry point
├── models.py       → database functions and SQL queries
├── db.py           → connection and configuration
├── templates/
│   └── index.html  → Jinja2 HTML template with Chart.js
├── static/
│   └── style.css   → dashboard styling
└── .env            → environment variables (not committed)

## Features

- Add and delete expenses with description, amount, category, and date
- Organize expenses into categories
- Live bar chart showing spending totals per category
- Full expenses table with JOIN query across two tables
- REST API endpoint serving JSON data to Chart.js
- Connected to AWS RDS PostgreSQL in the cloud

## Tech Stack

- Python 3
- Flask
- PostgreSQL
- AWS RDS
- psycopg2
- python-dotenv
- Chart.js
- HTML/CSS
- JavaScript (Fetch API)

## Setup

pip install flask psycopg2-binary python-dotenv

## Environment Variables

Create a .env file with the following:

PG_HOST=your-rds-endpoint.rds.amazonaws.com
PG_PORT=5433
PG_NAME=postgres
PG_USER=your-username
PG_PASSWORD=your-password

## Usage

python3 app.py

Then open your browser to http://127.0.0.1:5000

## What I Learned

- Building a full stack web application with Flask
- Creating REST API endpoints that return JSON data
- Connecting a JavaScript frontend to a Python backend via Fetch API
- Rendering dynamic HTML with Jinja2 templating
- Visualizing database data with Chart.js
- Designing relational schemas with foreign keys and JOIN queries
- Connecting to AWS RDS PostgreSQL from a Flask backend
- Separating concerns across database, business logic, and routing layers

## Project Journey

SQLite → PostgreSQL → AWS RDS → Flask Backend → HTML/CSS Frontend → Chart.js Dashboard

## Next Steps

- Deploy to AWS EC2 so it's accessible from anywhere
- Add user authentication with Flask-Login
- Add date range filtering for expenses
- Implement SSH tunneling for secure database access

