# -*- coding: utf-8 -*-
"""Skript um ein Histogramm interaktiv zu füllen"""

import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from pylab import *
# Speicher für Einträge vorbereiten
values = []
# Bin-Grenzen erzeugen: [0.5,1.5,...,9.5,10.5]
edges   = mlab.frange(0.5,10,1)
# Grafik-Fenster vorbereiten
fig = plt.figure()
plt.show(block=False)

# Histogramm füllen
while True:
    # nächsten Eintrag einlesen
    try:
        new = float(input("neu : "))
    except ValueError:
        break
    # Kontrolle auf Programm-Ende
    if new <= 0:
        break
    # Histogramm erstellen, alte Einträge blau, neuster Eintrag rot
    plt.hist([values, [new]], bins=edges, histtype='barstacked', rwidth=1, color=['b','r'])
    # neuen Eintrag zu Speicher hinzufügen
    values.append(new)
    # Grafik aktualisieren
    fig.canvas.draw()
savefig("histo.png")
