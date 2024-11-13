from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='public')

# Route für die Startseite (HTML)
@app.route('/')
def home():
    return send_from_directory('public', 'site.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))