import requests
import time
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# URL der API
url = "http://widgets.vvo-online.de/abfahrtsmonitor/Abfahrten.do?hst=wiekerstraße&vz=0&ort=Dresden&lim=10&timestamp=1487172338"

# Funktion, um die Daten abzufragen
def get_data():
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Angenommen, die API liefert JSON zurück
    else:
        print("Fehler beim Abrufen der Daten")
        return []

# Funktion, um die Abfahrtszeiten zu visualisieren
def plot_data(data):
    # Umwandeln der Daten in Abfahrtszeiten
    abfahrt_zeiten = []
    for item in data:
        if item[2] == "":
            abfahrt_zeiten.append("Jetzt")
        else:
            abfahrt_zeiten.append(f"{item[2]} Minuten")
    
    # Erstellen eines Diagramms
    plt.clf()  # Vorheriges Diagramm löschen
    plt.bar(range(len(abfahrt_zeiten)), np.ones(len(abfahrt_zeiten)))  # Balkendiagramm
    plt.xticks(range(len(abfahrt_zeiten)), abfahrt_zeiten, rotation=45, ha="right")
    plt.title("Abfahrtszeiten für die Haltestelle Wieckestraße")
    plt.ylabel("Züge")
    plt.tight_layout()  # Stellt sicher, dass alles im Diagramm Platz hat
    plt.draw()

# Echtzeit-Datenabfrage alle 30 Sekunden
def real_time_monitor():
    plt.ion()  # Interaktiven Modus aktivieren (Echtzeit-Update)
    while True:
        data = get_data()  # Daten abfragen
        if data:
            plot_data(data)  # Daten visualisieren
        time.sleep(30)  # 30 Sekunden warten

if __name__ == "__main__":
    real_time_monitor()