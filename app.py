from flask import Flask, jsonify, send_from_directory
import requests
import os
from datetime import datetime, timedelta, timezone
import pytz 

app = Flask(__name__)

# Route für die HTML-Seite (Startseite)
@app.route('/')
def home():
    # Wenn die HTML-Datei im Verzeichnis 'static' liegt
    return send_from_directory(os.getcwd(), 'site.html')

# Route für die Uhrzeit
@app.route('/api/zeit')
def get_time():
    # Festlegen der Zeitzone auf Mitteleuropäische Zeit (MEZ/MESZ)
    timezone = pytz.timezone('Europe/Berlin')
    current_time = datetime.now(timezone).strftime('%H:%M')
    return jsonify({"time": current_time})

# Route für die Abfahrtsdaten
@app.route('/api/abfahrten')
def abfahrten():
    # Abruf der Abfahrtsdaten von Wieckestraße
    wieckestraße_url = "http://widgets.vvo-online.de/abfahrtsmonitor/Abfahrten.do?hst=wiekestra%C3%9Fe&vz=0&ort=Dresden&lim=20"
    wieckestraße_response = requests.get(wieckestraße_url)
    wieckestraße_data = wieckestraße_response.json()

    # Abruf der Abfahrtsdaten vom Wasaplatz
    wasaPlatz_url = "http://widgets.vvo-online.de/abfahrtsmonitor/Abfahrten.do?hst=wasaplatz&vz=0&ort=Dresden&lim=50"
    wasaPlatz_response = requests.get(wasaPlatz_url)
    wasaPlatz_data = wasaPlatz_response.json()

    # Daten als JSON an das Frontend zurückgeben
    return jsonify({
        "wieckestraße": wieckestraße_data,
        "wasaPlatz": wasaPlatz_data
    })

if __name__ == "__main__":
    app.run(debug=True)