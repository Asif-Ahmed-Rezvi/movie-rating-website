# movies/routes.py

from flask import Blueprint, render_template
from db_connection import get_db_connection

# Create blueprint for movie routes
movies_bp = Blueprint('movies', __name__)

# Route: /movies — list all movies
@movies_bp.route('/movies')
def list_movies():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM movies ORDER BY release_year DESC")
    movies = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('movies.html', movies=movies)
