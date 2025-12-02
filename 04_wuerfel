"""
Übung 4: Würfelspiel

Aufgabe:
Erstelle zwei Klassen:
1. Wuerfel: Simuliert einen Würfel mit verschiedenen Seitenzahlen
2. Spieler: Repräsentiert einen Spieler der würfeln und Punkte sammeln kann

Das Spiel soll:
- Würfel mit unterschiedlichen Seitenzahlen erstellen können (z.B. W6, W20)
- Spieler würfeln lassen und Punkte sammeln
- Die Gesamtpunktzahl anzeigen
- Einen Würfelwurf-Verlauf anzeigen

Wichtig: Verwende das 'random' Modul für die Zufallszahlen!
"""

# TODO 0: Importiere das random Modul
# import random


# TODO 1: Erstelle die Klasse Wuerfel
class Wuerfel:
    """
    Ein Würfel mit einer bestimmten Anzahl an Seiten.
    
    Attribute:
    - seiten (int): Anzahl der Seiten (z.B. 6 für einen normalen Würfel)
    - name (str): Name des Würfels (z.B. "W6", "W20")
    """
    
    # TODO 1.1: Schreibe den Konstruktor __init__
    # Parameter: self, seiten, name
    # Speichere seiten und name als Attribute
    pass
    
    # TODO 1.2: Schreibe die Methode werfen()
    # Keine Parameter außer self
    # Verwende random.randint(1, self.seiten) um eine Zufallszahl zu erzeugen
    # Gib die Zahl zurück (return)
    pass
    
    # TODO 1.3: Schreibe die Methode zeige_info()
    # Gibt aus: "{name} (1-{seiten})"
    pass


# TODO 2: Erstelle die Klasse Spieler
class Spieler:
    """
    Ein Spieler der würfeln und Punkte sammeln kann.
    
    Attribute:
    - name (str): Name des Spielers
    - punkte (int): Aktuelle Gesamtpunktzahl
    - wuerfe (list): Liste aller geworfenen Zahlen
    """
    
    # TODO 2.1: Schreibe den Konstruktor __init__
    # Parameter: self, name
    # Speichere name als Attribut
    # Initialisiere punkte mit 0
    # Initialisiere eine leere Liste wuerfe = []
    pass
    
    # TODO 2.2: Schreibe die Methode wuerfeln(wuerfel)
    # Parameter: self, wuerfel (ein Wuerfel-Objekt)
    # Rufe wuerfel.werfen() auf und speichere das Ergebnis
    # Füge das Ergebnis zur Liste wuerfe hinzu
    # Addiere das Ergebnis zu self.punkte
    # Gib aus: "🎲 {name} würfelt mit {wuerfel.name}: {ergebnis}"
    pass
    
    # TODO 2.3: Schreibe die Methode zeige_statistik()
    # Keine Parameter außer self
    # Gib aus: "\n📊 Statistik für {name}:"
    # Gib aus: "Anzahl Würfe: {anzahl}"
    # Gib aus: "Gesamtpunkte: {punkte}"
    # Gib aus: "Alle Würfe: {wuerfe}" (als komma-getrennte Liste)
    pass
    
    # TODO 2.4: Schreibe die Methode punkte_zuruecksetzen()
    # Keine Parameter außer self
    # Setze punkte auf 0
    # Leere die wuerfe Liste
    # Gib aus: "🔄 {name}: Punkte zurückgesetzt"
    pass


# TODO 3: Teste deine Klassen

# TODO 3.1: Erstelle zwei Würfel-Objekte
# w6 = Wuerfel(6, "W6")
# w20 = Wuerfel(20, "W20")
pass

# TODO 3.2: Zeige die Würfel-Infos
# w6.zeige_info()
# w20.zeige_info()
pass

# TODO 3.3: Erstelle einen Spieler
# spieler = Spieler("Anna")
pass

# TODO 3.4: Lass den Spieler 3x mit W6 würfeln
# spieler.wuerfeln(w6)
# spieler.wuerfeln(w6)
# spieler.wuerfeln(w6)
pass

# TODO 3.5: Lass den Spieler 2x mit W20 würfeln
# spieler.wuerfeln(w20)
# spieler.wuerfeln(w20)
pass

# TODO 3.6: Zeige die Statistik
# spieler.zeige_statistik()
pass


"""
Erwartetes Ergebnis (Zufallszahlen variieren):
W6 (1-6)
W20 (1-20)
🎲 Anna würfelt mit W6: 4
🎲 Anna würfelt mit W6: 2
🎲 Anna würfelt mit W6: 6
🎲 Anna würfelt mit W20: 15
🎲 Anna würfelt mit W20: 8

📊 Statistik für Anna:
Anzahl Würfe: 5
Gesamtpunkte: 35
Alle Würfe: [4, 2, 6, 15, 8]
"""
