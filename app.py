from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='public')

# Route für die Startseite (HTML)
@app.route('/')
def home():
    return send_from_directory('public', 'site.html')

# Starten der Datenbank und des Servers
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)  # use_reloader=False, um Konflikte mit dem Scheduler zu vermeiden
