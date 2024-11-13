from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='public')

# Route für die Startseite (HTML)
@app.route('/')
def home():
    return send_from_directory('public', 'site.html')
