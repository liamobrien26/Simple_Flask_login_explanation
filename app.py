# Import necessary modules
from flask import Flask, redirect, url_for, render_template, request 
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user 

"""
----- Imported Modules and Functions Explanation -----

-Flask: It's a Python library that helps us create web applications. It provides tools and features to make building web apps easier.

-redirect: This function is used to send users to a different page or URL. For example, after submitting a form, we can use redirect to take the user to a thank you page.

-url_for: This function helps us generate URLs for different parts of our application. 
  Instead of hardcoding URLs in our templates or code, we use url_for to dynamically generate them. It's like having a dynamic address book for our web pages.

-render_template: This function allows us to create HTML pages with dynamic content. We can combine HTML with Python code using templates. 
  For example, we can pass data from our Python code to an HTML template to display information on a web page.

-request: This object contains information about the current request made by the client (usually a web browser). 
  It provides access to form data, request headers, cookies, and more. It's like a messenger that brings us all the details about what the user wants from our application.

-LoginManager: This is a Flask extension that helps manage user authentication. It provides functionality to handle user logins, logouts, and session management.

-UserMixin: It's a mixin class provided by Flask-Login that includes common user-related methods and properties. 
  It simplifies user management by providing default implementations for user-related functionality.

-login_user: This function is used to log in a user. It takes a user object and sets up the necessary session data to keep the user logged in across requests.

-login_required: This decorator is used to restrict access to certain views or routes to only logged-in users. 
  If a user tries to access a protected route without being logged in, they will be redirected to the login page.

-logout_user: This function is used to log out a user. It clears the session data related to the current user, effectively ending their session.

-current_user: This object represents the currently logged-in user. It allows us to access information about the logged-in user, such as their ID, username, or other user-specific data.
"""



#------- Instructions to Set Up and Run a Flask Application -------

# 1. Create a Virtual Environment: 'python3 -m venv myenv'
# 2. Activate the Virtual Environment: 'source myenv/bin/activate'
# 3. Install Flask: Once your virtual environment is activated, you can install Flask using pip, the Python package installer: 'pip install Flask'
# 4. Install Flask-Login: 'pip install Flask-Login'
# 5. Run the Flask Application: 'python app.py' on terminal 
# 6. Go on your browser and copy paste this link: http://127.0.0.1:5000/login




# Create a Flask application
app = Flask(__name__)  

# Set a secret key for the application to securely sign session cookies
app.secret_key = 'team_mind'  

# Define a class representing a user, inheriting basic functionality from Flask-Login
class User(UserMixin):  
    def __init__(self, id):  
        self.id = id  

# Define a static database with sample usernames and passwords
users = {'user1': {'password': 'password1'}, 'user2': {'password': 'password2'}}  

# Create a LoginManager instance to manage user login sessions
login_manager = LoginManager()  
login_manager.init_app(app)  

# Define a function to load a user by ID from the user database
@login_manager.user_loader  
def load_user(user_id):  
    return User(user_id)  



# Define a route for handling login requests
@app.route('/login', methods=['GET', 'POST'])  
def login():  
    # Check if the user submitted the login form
    if request.method == 'POST':  
        # Get the username and password from the mock database
        username = request.form['username']  
        password = request.form['password']  
        
        # Check if the entered username and password match any in the database
        if username in users and users[username]['password'] == password:  
            # Create a User object and log the user in
            user = User(username)  
            login_user(user)  
            # Redirect the user to their dashboard
            return redirect(url_for('dashboard'))  
        
        # Return an error message if the login attempt failed
        return 'Invalid username or password'  
    
    # Render the login page template
    return render_template('login.html')  



# Define a route for the dashboard page, accessible only to logged-in users
@app.route('/dashboard')  
@login_required  
def dashboard():  
    # Render the dashboard template, passing the current user's ID
    return render_template('dashboard.html', username=current_user.id) 



# Define a route for logging out
@app.route('/logout', methods=['POST'])  
@login_required  
def logout():  
    # Log the user out and redirect them to the login page
    logout_user()  
    return redirect(url_for('login'))  



# Run the Flask application in debug mode
if __name__ == '__main__':  
    app.run(debug=True)  
