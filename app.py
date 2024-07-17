# app.py
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Connect to SQLite database
def init_db():
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS feedback
                      (id INTEGER PRIMARY KEY, name TEXT, email TEXT, feedback TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_feedback():
    name = request.form['name']
    email = request.form['email']
    feedback = request.form['feedback']

    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO feedback (name, email, feedback) VALUES (?, ?, ?)', (name, email, feedback))
    conn.commit()
    conn.close()

    return 'Thank you for your feedback!'

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
