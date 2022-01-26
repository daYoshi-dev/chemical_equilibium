import matplotlib as mplt
from matplotlib import pyplot as plt
from matplotlib import gridspec
import numpy as np
import pandas as pd
import time


# GER:
"""
Dieses Programm stellt eine Gleichgewichtsreaktion graphisch dar.
Die Gleichgewichtskonstante Kc wird hierbei durch die Variable kc dargestellt.
Es reagiert immer 1% der Produkte.
Die Zeitspanne wird über maxTime bestimmt.
Edukt und Produktmengen über edukt und produkt.
Die verschiedenen Werte werden in den Arrays mit dem jeweiligen Anfangsbuchstaben abgelegt.
v steht für die Wartezeit nach jeder Durchführung.

Das Programm passt sich den gegebenen Werten entsprechend an.

Anmerkung:

Aufgrund der langen Kalkulationsdauer kann es sein, dass v = 0 eine angemessene Wartezeit ergibt.
"""

# VAR

edukt = 10000
produkt = 0
ealt = 0
zeit = 1
verhaeltnis = produkt/edukt
maxTime = 500
anteil = 0.1

eARR = [edukt]
pARR = [produkt]
zARR = [zeit]
vARR = [verhaeltnis]

v = 0.01
kc = 3.5

ungleichgewicht=True

# GER: Erstellen der Koord-Systeme
# ENG: Definition of coordinate systems
plt.ion()
fig = plt.figure()
gs = gridspec.GridSpec(2, 1, height_ratios=[2, 3])


# GER: Sys 1: Edukte & Produkte
# ENG: Sys 1: Educts & Products

ax0 = plt.subplot(gs[0], title='Edukte und Produkte', xlabel='Zeit', ylabel='Menge')
ax0.set_xscale('log')

ax0.grid()

# GER: Achsen
# ENG: Axis
ax0.set_xscale('log')
ax0.set_yscale('linear')

ax0.set_xlim([1, maxTime])
ax0.set_ylim([1, edukt+produkt])

# GER: Linien
# ENG: Graphs

eline, = ax0.plot(zeit, eARR, 'b', label='Edukte')
pline, = ax0.plot(zeit, pARR, 'r', label='Produkte')



# GER: Sys 2: Verhaeltnis und Kc
# ENG: Sys 2: Ratio and Kc

ax1 = plt.subplot(gs[1], sharex=ax0, title='Verhältnis und Kc', xlabel='Zeit', ylabel='Stoffverhältnis')
ax1.grid()


# GER: Achsen
# ENG: Axis

ax1.set_xscale('log')
ax1.set_yscale('linear')

ax1.set_xlim([1, maxTime])
ax1.set_ylim([0, kc+1])

# GER: Linen
# ENG: Graphs

kline = ax1.hlines(kc, 1, maxTime, 'black', label='kc')
vline, = ax1.plot(zeit, 'g', label='Edukt-Produkt-Verhältnis')

# GER: Legende
# ENG: Legend
ax0.legend(loc='center right')
ax1.legend(loc='lower right')

# GER/ENG: Padding
plt.tight_layout()

for zeit in range(1, maxTime):

    # GER: Neuberechnung der Werte
    # ENG: Calculating of next values
    ealt = edukt
    edukt = edukt - round(edukt / 1 * anteil) + round(produkt / kc * anteil)
    produkt = produkt - round(produkt / kc * anteil) + round(ealt / 1 * anteil)
    verhaeltnis = produkt/ edukt

    if ungleichgewicht and (kc < (verhaeltnis + 0.01)):
        plt.plot(zARR[-1]+1, kc, 'ro',label='Gleichgewichtspunkt')
        ax0.axvline(zARR[-1]+1, color='b', linestyle='dashed')
        ungleichgewicht=False

    # GER: Hinzufügen zu Wertemenge
    # ENG: Append to Arrays
    eARR.append(edukt)
    pARR.append(produkt)
    vARR.append(verhaeltnis)
    zARR.append(zARR[-1] + 1)

    # GER: Update der Graphen
    # ENG: Update of Graphs
    eline.set_xdata(zARR)
    eline.set_ydata(eARR)

    pline.set_xdata(zARR)
    pline.set_ydata(pARR)

    vline.set_xdata(zARR)
    vline.set_ydata(vARR)

    # GER: Neuzeichnen des Graphen + Warten
    # ENG: Redraw of Graph and wait
    fig.canvas.draw()
    time.sleep(v)

# GER: Offen halten des Fensters
# ENG: Keeping window open
plt.ioff()
plt.show()









