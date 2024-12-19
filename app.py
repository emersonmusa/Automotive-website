from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Fake user data for demonstration purposes (replace with a database in a real app)
users = {"admin": {"password": "password123"}}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Basic registration logic (in a real app, you would save this to a database)
        if username in users:
            flash("Username already exists", "danger")
        else:
            users[username] = {"password": password}
            flash("Registration successful! Please login.", "success")
            return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username in users and users[username]['password'] == password:
        session['username'] = username
        return redirect(url_for('dashboard'))
    else:
        flash("Invalid username or password.", "danger")
        return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
