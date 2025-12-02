"""
Übung 3: Einkaufswagen

Aufgabe:
Erstelle zwei Klassen:
1. Artikel: Repräsentiert einen einzelnen Artikel mit Name und Preis
2. Einkaufswagen: Verwaltet eine Liste von Artikel-Objekten

Der Einkaufswagen soll:
- Artikel hinzufügen können
- Den Gesamtpreis berechnen
- Die Anzahl der Artikel zählen
- Den Inhalt anzeigen
"""

# TODO 1: Erstelle die Klasse Artikel mit passendem Konstruktor
class Artikel:
    """
    Ein einzelner Artikel im Einkaufswagen.
    
    Attribute:
    - name (str): Name des Artikels
    - preis (float): Preis des Artikels
    """
    # TODO 1.1: Schreibe den Konstruktor __init__
    # Parameter: self, name, preis
    # Speichere name und preis als Attribute
    pass
    
    # TODO 1.2: Schreibe die Methode zeige_info()
    # Gibt aus: "- {name}: {preis} EUR"
    pass


# TODO 2: Erstelle die Klasse Einkaufswagen
class Einkaufswagen:
    """
    Ein Einkaufswagen der Artikel-Objekte verwaltet.
    
    Attribute:
    - artikel (list): Liste von Artikel-Objekten
    """
    
    # TODO 2.1: Schreibe den Konstruktor __init__
    # Keine Parameter außer self
    # Initialisiere eine leere Liste self.artikel = []
    pass
    
    # TODO 2.2: Schreibe die Methode hinzufuegen(artikel)
    # Parameter: self, artikel (ein Artikel-Objekt)
    # Füge das Artikel-Objekt zur Liste hinzu
    # Gib aus: "✅ {artikel.name} hinzugefügt"
    pass
    
    # TODO 2.3: Schreibe die Methode gesamtpreis()
    # Keine Parameter außer self
    # Berechne die Summe aller Preise (artikel.preis)
    # Gib die Summe zurück (return)
    pass
    
    # TODO 2.4: Schreibe die Methode anzahl_artikel()
    # Keine Parameter außer self
    # Gib die Anzahl der Artikel zurück (len(self.artikel))
    pass
    
    # TODO 2.5: Schreibe die Methode zeige_inhalt()
    # Keine Parameter außer self
    # Gib aus: "Einkaufswagen ({anzahl} Artikel):"
    # Für jeden Artikel: Rufe artikel.zeige_info() auf
    # Gib aus: "Gesamtpreis: {gesamtpreis} EUR"
    pass


# TODO 3.1: Erstelle drei Artikel-Objekte
# artikel1 = Artikel("Brot", 2.99)
# artikel2 = Artikel("Milch", 1.49)
# artikel3 = Artikel("Käse", 4.50)
pass

# TODO 3.2: Erstelle einen Einkaufswagen
# wagen = Einkaufswagen()
pass

# TODO 3.3: Füge die drei Artikel zum Wagen hinzu
# wagen.hinzufuegen(artikel1)
# wagen.hinzufuegen(artikel2)
# wagen.hinzufuegen(artikel3)
pass

# TODO 3.4: Zeige den Inhalt des Wagens
# wagen.zeige_inhalt()
pass


"""
Erwartetes Ergebnis:
✅ Brot hinzugefügt
✅ Milch hinzugefügt
✅ Käse hinzugefügt

Einkaufswagen (3 Artikel):
- Brot: 2.99 EUR
- Milch: 1.49 EUR
- Käse: 4.50 EUR
Gesamtpreis: 8.98 EUR
"""
