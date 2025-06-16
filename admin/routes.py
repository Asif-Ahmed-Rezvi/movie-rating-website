# admin/routes.py

from flask import Blueprint, render_template, request, redirect, flash, session
from db_connection import get_db_connection

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# View admin panel with movie list
@admin_bp.route('/movies')
def admin_movies():
    if 'username' not in session:
        flash("You must be logged in to access admin panel.", "danger")
        return redirect('/login')

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM movies ORDER BY release_year DESC")
    movies = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('admin_movies.html', movies=movies)

# Add movie form + insert
@admin_bp.route('/movies/add', methods=['GET', 'POST'])
def add_movie():
    if 'username' not in session:
        flash("You must be logged in to add movies.", "danger")
        return redirect('/login')

    if request.method == 'POST':
        title = request.form['title']
        synopsis = request.form['synopsis']
        release_year = request.form['release_year']
        cast = request.form['cast']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO movies (title, synopsis, release_year, cast)
            VALUES (%s, %s, %s, %s)
        """, (title, synopsis, release_year, cast))
        conn.commit()
        cursor.close()
        conn.close()
        flash('Movie added successfully!', 'success')
        return redirect('/admin/movies')

    return render_template('add_movie.html')
