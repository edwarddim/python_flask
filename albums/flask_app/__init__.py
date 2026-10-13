from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)

app.secret_key = 'a6db85295f74be71f4a28eb2bec68e1ec7f0378e7eae1ab1efe74398c4e0beda'