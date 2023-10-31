from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Route to handle form submission
@app.route('/add_user', methods=['POST'])
def add_user():
    # Get data from the form submitted by the user
    username = request.form['username']
    email = request.form['email']

    # Establish a connection to the database
    conn = sqlite3.connect('db/database.db')

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Insert data into the users table
    cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", (username, email))

    # Commit the transaction
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Redirect the user to the user list page
    return redirect(url_for('user_list'))

# Route to display a form for user input
@app.route('/form')
def form():
    return render_template('form.html')

# Route to display a list of users
@app.route('/users')
def user_list():
    conn = sqlite3.connect('db/database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users;')
    users = cursor.fetchall()
    conn.close()
    return render_template('user.html', users=users)

# Route to display a success message
@app.route('/success')
def success():
    return "User successfully added to the database!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

