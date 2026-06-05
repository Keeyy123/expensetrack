from db import get_connection

def add_category(name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO categories (name) VALUES (%s)", (name,))
    conn.commit()
    cur.close()
    conn.close()

def get_categories():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM categories ORDER BY name")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def add_expense(description, amount, category_id, date=None):
    conn = get_connection()
    cur = conn.cursor()
    if date:
        cur.execute(
            "INSERT INTO expenses (description, amount, category_id, date) VALUES (%s, %s, %s, %s)",
            (description, amount, category_id, date)
        )
    else:
        cur.execute(
            "INSERT INTO expenses (description, amount, category_id) VALUES (%s, %s, %s)",
            (description, amount, category_id)
        )
    conn.commit()
    cur.close()
    conn.close()

def get_expenses():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT expenses.id, expenses.description, expenses.amount,
               categories.name, expenses.date
        FROM expenses
        LEFT JOIN categories ON expenses.category_id = categories.id
        ORDER BY expenses.date DESC
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def get_totals_by_category():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT categories.name, SUM(expenses.amount)
        FROM expenses
        LEFT JOIN categories ON expenses.category_id = categories.id
        GROUP BY categories.name
        ORDER BY SUM(expenses.amount) DESC
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def delete_expense(expense_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM expenses WHERE id=%s", (expense_id,))
    conn.commit()
    cur.close()
    conn.close()
