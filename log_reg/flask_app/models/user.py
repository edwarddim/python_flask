from flask_app import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
DATABASE = 'login_reg'

class User:
    def __init__(self, data):
        self.id = data['id']
        # 
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        # 
        self.created_at = data['created_at']
        self.updated_at = data['updated-at']

    def __repr__(self):
        return f'<User: {self.username}>'

    @staticmethod
    def validate_register(form):
        is_valid = True
        if len(form['username']) < 3:
            flash('Username must be at least three characters.', 'username')
            is_valid = False
        if not EMAIL_REGEX.match(form['email']):
            flash('Please enter a valid email.', 'email')
            is_valid = False
        if len(form['password']) < 8:
            flash('Password must be at least eight characters.', 'password')
            is_valid = False
        else:
            if form['password'] != form['confirm_password']:
                flash('Passwords do not match.', 'confirm_password')
                is_valid = False
        return is_valid
    
    @classmethod
    def find_user_by_email(cls, data):
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) > 0:
            return User(results[0])
        return None


    @classmethod
    def find_by_id(cls, data):
        query = 'SELECT * FROM users WHERE id = %(id)s'
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results[0]
