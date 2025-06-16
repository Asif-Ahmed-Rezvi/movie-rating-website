from flask import Blueprint, render_template, request, redirect, flash
from flask_bcrypt import Bcrypt
from db_connection import get_db_connection

auth_bp = Blueprint('auth', __name__)
bcrypt = Bcrypt()

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                           (username, email, hashed_password))
            conn.commit()
            flash('Registration successful!', 'success')
            return redirect('/')
        except Exception as e:
            flash(f'Error: {e}', 'danger')
        finally:
            cursor.close()
            conn.close()

    return render_template('register.html')
from flask import session  # Make sure this is imported at the top

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user and bcrypt.check_password_hash(user['password'], password):
            session['user_id'] = user['user_id']
            session['username'] = user['username']
            flash('Login successful!', 'success')
            return redirect('/')
        else:
            flash('Invalid email or password.', 'danger')

    return render_template('login.html')
from flask import session, redirect, flash

@auth_bp.route('/logout')
def logout():
    session.clear()  # removes all session data
    flash('You have been logged out.', 'success')
    return redirect('/')
