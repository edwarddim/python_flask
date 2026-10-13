from flask import Flask, render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt


app = Flask(__name__)

bcrypt = Bcrypt(app)

app.secret_key = 'fb534bf97e53d2b93d1d894128cbd701d66cbde9d303ea550606719b2d763605'
