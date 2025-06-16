# main.py

from flask import Flask, render_template, session
from auth.routes import auth_bp, bcrypt
from movies.routes import movies_bp
from admin.routes import admin_bp  # ✅ NEW: Admin blueprint import

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with something strong in real projects

# Register all route blueprints
app.register_blueprint(auth_bp)      # Handles /login, /register, /logout
app.register_blueprint(movies_bp)    # Handles /movies
app.register_blueprint(admin_bp)     # ✅ NEW: Handles /admin/movies

# Initialize bcrypt for password hashing
bcrypt.init_app(app)

# Home route
@app.route('/')
def home():
    return render_template("home.html")

# Start the Flask server
if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')
