# from flask import Flask,render_template
# from flask_sqlalchemy import SQLAlchemy
# from pymongo import MongoClient
# from datetime import datetime


# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mongodb://localhost:27017'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(200), unique=True, nullable=False)
#     email = db.Column(db.String(500), unique=True, nullable=False)
#     fname = db.Column(db.String(500), nullable=False)
#     lname = db.Column(db.String(500), nullable=False)
#     password = db.Column(db.String(500), nullable=False)

#     def __repr__(self) -> str:
#         return '<User %r>' % self.username

# @app.route("/main")
# def main():
#     return render_template("main.html")

# @app.route("/index")
# def index():
#     return render_template("index.html")


# @app.route("/register")
# def register():
#     return render_template("register.html")

# @app.route("/login")
# def login():
#     return render_template("login.html")

# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()
#         user = User(username='Sanket Katkade',email='sanketkatkade782@gmail.com',fname='Sanket',lname='Katakde',password='1234')
#         db.session.add(user)
#         print("Session added")
#         db.session.commit()
#         print("Session Commited")
#         data = User.query.all()
#     app.run(debug=True)


# from flask import Flask, render_template, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mongodb://localhost:27017'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(200), unique=True, nullable=False)
#     email = db.Column(db.String(500), unique=True, nullable=False)
#     fname = db.Column(db.String(500), nullable=False)
#     lname = db.Column(db.String(500), nullable=False)
#     password = db.Column(db.String(500), nullable=False)

#     def __repr__(self) -> str:
#         return '<User %r>' % self.username

# # Create a route to add a user to the database
# @app.route("/add_user", methods=['GET', 'POST'])
# def add_user():
#     if request.method == 'POST':
#         username = request.form['username']
#         email = request.form['email']
#         fname = request.form['fname']
#         lname = request.form['lname']
#         password = request.form['password']
#         user = User(username=username, email=email, fname=fname, lname=lname, password=password)
#         db.session.add(user)
#         db.session.commit()
#         return redirect(url_for('index'))
#     return render_template("add_user.html")

# @app.route("/main")
# def main():
#     return render_template("main.html")

# @app.route("/index")
# def index():
#     # Fetch and display all users from the database
#     users = User.query.all()
#     return render_template("index.html", users=users)

# @app.route("/register")
# def register():
#     return render_template("register.html")

# @app.route("/login")
# def login():
#     return render_template("login.html")

# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)






# from flask import Flask, render_template
# from pymongo import MongoClient

# app = Flask(__name__)

# # Connect to MongoDB
# client = MongoClient('mongodb://localhost:27017')
# db = client['mydb']  # Replace 'your_database_name' with your database name

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(200), unique=True, nullable=False)
#     email = db.Column(db.String(500), unique=True, nullable=False)
#     fname = db.Column(db.String(500), nullable=False)
#     lname = db.Column(db.String(500), nullable=False)
#     password = db.Column(db.String(500), nullable=False)

#     def __repr__(self) -> str:
#         return '<User %r>' % self.username

# @app.route("/main")
# def main():
#     return render_template("main.html")

# @app.route("/index")
# def index():
#     return render_template("index.html")

# @app.route("/register")
# def register():
#     return render_template("register.html")

# @app.route("/login")
# def login():
#     return render_template("login.html")

# if __name__ == "__main__":
#     app.run(debug=True)





from flask import Flask, render_template, request,flash,redirect
from pymongo import MongoClient
from flask_login import LoginManager
login_manager = init_app(app)

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
app.config['SECRET_KEY'] = 'thisissecret'
db = client['mydb']  # Replace 'your_database_name' with your database name

# Define a MongoDB collection (not a SQLAlchemy model)
users_collection = db['User']  # Corrected collection name

@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        username = request.form.get('uname')
        fname = request.form.get('fname')
        lname = request.form.get('lname')

        registration_data = {
            "email": email,
            "password": password,
            "username": username,
            "first_name": fname,
            "last_name": lname
        }

        # Insert the registration data into the MongoDB collection
        inserted_id = users_collection.insert_one(registration_data).inserted_id  # Use the correct collection name

        if(inserted_id):
            flash('user has been register successfully','success')
            return redirect ('/login')
        return "User registration failed"



    return render_template("register.html")


@login_manager_user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route("/login",methods =['GET','POST'])
def login():
        username = request.form.get('username')
        password = request.form.get('password')
        return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
