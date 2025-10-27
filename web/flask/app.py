from flask import Flask, render_template, request, redirect, url_for, flash
from supabase import create_client, Client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'your-secret-key-change-this')

# Initialize Supabase client
SUPABASE_URL = os.getenv('NEXT_PUBLIC_SUPABASE_URL')
SUPABASE_KEY = os.getenv('NEXT_PUBLIC_SUPABASE_ANON_KEY')

if not SUPABASE_URL or not SUPABASE_KEY:
    print("Warning: Supabase credentials not found. Please set SUPABASE_URL and SUPABASE_KEY in .env file")
    supabase: Client = None
else:
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def home():
    """Home page route"""
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Registration page route"""
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        
        try:
            if supabase is None:
                flash('Database connection not configured. Please check your Supabase credentials.', 'error')
                return render_template('register.html')
            
            # Insert user data into Supabase
            # Note: This inserts into a 'users' table. Adjust table name as needed.
            data = {
                'name': name,
                'email': email,
            }
            
            response = supabase.table('user').insert(data).execute()
            
            flash('Registration successful! Welcome aboard.', 'success')
            return redirect(url_for('home'))
            
        except Exception as e:
            flash(f'Registration failed: {str(e)}', 'error')
            return render_template('register.html')
    
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

