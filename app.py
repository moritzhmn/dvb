from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Route für die Abfahrtsdaten
@app.route('/api/abfahrten')
def abfahrten():
    # Abruf der Abfahrtsdaten von Wieckestraße
    wieckestraße_url = "http://widgets.vvo-online.de/abfahrtsmonitor/Abfahrten.do?hst=wiekestra%C3%9Fe&vz=0&ort=Dresden&lim=12"
    wieckestraße_response = requests.get(wieckestraße_url)
    wieckestraße_data = wieckestraße_response.json()

    # Abruf der Abfahrtsdaten vom Wasaplatz
    wasaPlatz_url = "http://widgets.vvo-online.de/abfahrtsmonitor/Abfahrten.do?hst=wasaplatz&vz=0&ort=Dresden&lim=30"
    wasaPlatz_response = requests.get(wasaPlatz_url)
    wasaPlatz_data = wasaPlatz_response.json()

    # Daten als JSON an das Frontend zurückgeben
    return jsonify({
        "wieckestraße": wieckestraße_data,
        "wasaPlatz": wasaPlatz_data
    })

if __name__ == "__main__":
    app.run(debug=True)