from flask import Flask, render_template, request, redirect, url_for, jsonify
from db import setup_database
from models import (
    add_category, get_categories,
    add_expense, get_expenses,
    get_totals_by_category, delete_expense
)

app = Flask(__name__)

@app.route('/')
def index():
    expenses = get_expenses()
    categories = get_categories()
    totals = get_totals_by_category()
    return render_template('index.html',
        expenses=expenses,
        categories=categories,
        totals=totals
    )

@app.route('/add-expense', methods=['POST'])
def add_expense_route():
    description = request.form.get('description')
    amount      = request.form.get('amount')
    category_id = request.form.get('category_id')
    date        = request.form.get('date')
    add_expense(description, amount, category_id, date)
    return redirect(url_for('index'))

@app.route('/add-category', methods=['POST'])
def add_category_route():
    name = request.form.get('name')
    add_category(name)
    return redirect(url_for('index'))

@app.route('/delete-expense/<int:expense_id>', methods=['POST'])
def delete_expense_route(expense_id):
    delete_expense(expense_id)
    return redirect(url_for('index'))

@app.route('/api/totals')
def api_totals():
    totals = get_totals_by_category()
    return jsonify([{'category': row[0], 'total': float(row[1])} for row in totals])

if __name__ == '__main__':
    setup_database()
    app.run(debug=True)
