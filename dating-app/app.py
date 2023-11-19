from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secret key

# User data (In a real application, this should be stored in a database)
users = [
    {"id": 1, "username": "Alice", "interests": ["Hiking", "Movies", "Travel"]},
    {"id": 2, "username": "Bob", "interests": ["Reading", "Sports", "Cooking"]},
    # Add more users as needed
]

@app.route('/')
def home():
    return render_template('home.html', users=users)

@app.route('/profile/<int:user_id>')
def profile(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return render_template('profile.html', user=user)
    else:
        flash('User not found', 'error')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
