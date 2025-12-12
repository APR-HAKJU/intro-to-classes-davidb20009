"""
Übung 9: Fehlersuche - Fahrzeug (Einfach)

🔍 AUFGABE:
In der Klasse 'Auto' sind 5 FEHLER versteckt!
Finde und behebe alle Fehler.

💡 TIPPS:
- Achte auf Attributnamen (self.X)
- Achte auf Methodenaufrufe
- Achte auf return-Statements
- Achte auf Vergleichsoperatoren

🎯 FEHLER-CHECKLISTE (zum Abhaken):
[ ] Fehler 1: _______________
[ ] Fehler 2: _______________
[ ] Fehler 3: _______________
[ ] Fehler 4: _______________
[ ] Fehler 5: _______________

Wenn alle Fehler behoben sind, erscheint am Ende:
✅ SUPER! Alle 5 Fehler wurden behoben!
"""


class Auto:
    def __init__(self, marke, modell, tank_kapazitaet):
        self.marke = marke
        self.modell = modell
        self.tank_kapazitaet = tank_kapazitaet
        # FEHLER 1: Wie greift man auf das eigene Attribut zu?
        tankstand = 0
        self.gefahrene_km = 0

    def tanken(self, liter):
        # FEHLER 2: Wie greift man auf tank_kapazitaet zu?
        if self.tankstand + liter > tank_kapazitaet:
            self.tankstand = self.tank_kapazitaet
            print(f"⛽ Tank ist voll! ({self.tank_kapazitaet}L)")
        else:
            self.tankstand += liter
            print(f"⛽ {liter}L getankt. Tankstand: {self.tankstand}L")

    def fahren(self, km):
        verbrauch = km * 0.08  # 8L pro 100km
        # FEHLER 3: Vergleichsoperator falsch! (größer oder gleich?)
        if self.tankstand < verbrauch:
            self.tankstand -= verbrauch
            self.gefahrene_km += km
            print(f"🚗 {km}km gefahren. Tankstand: {self.tankstand:.1f}L")
        else:
            print("❌ Nicht genug Benzin im Tank!")

    def get_info(self):
        # FEHLER 4: Was muss diese Methode zurückgeben?
        info = f"🚙 {self.marke} {self.modell} - {self.gefahrene_km}km gefahren"

    def tank_prozent(self):
        # FEHLER 5: Wie ruft man eine eigene Methode auf?
        prozent = (self.tankstand / tank_kapazitaet) * 100
        return round(prozent, 1)


# ═══════════════════════════════════════════════════════════════
# 🧪 TESTCODE - Nicht verändern! Zeigt ob alles funktioniert.
# ═══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    fehler_gefunden = 0
    
    print("🔍 Teste die Auto-Klasse...\n")
    
    try:
        # Test 1: Objekt erstellen und tankstand prüfen
        auto = Auto("BMW", "M3", 50)
        assert auto.tankstand == 0
        print("✅ Test 1: Auto-Objekt erstellt, tankstand = 0")
        fehler_gefunden += 1
    except Exception as e:
        print(f"❌ Test 1 fehlgeschlagen: tankstand nicht als self.tankstand")
    
    try:
        # Test 2: tanken() aufrufen
        auto.tanken(30)
        assert auto.tankstand == 30
        print("✅ Test 2: tanken() funktioniert")
        fehler_gefunden += 1
    except Exception as e:
        print(f"❌ Test 2 fehlgeschlagen: {e}")
    
    try:
        # Test 3: fahren() aufrufen
        auto.fahren(100)
        assert auto.gefahrene_km == 100
        assert auto.tankstand == 22.0
        print("✅ Test 3: fahren() funktioniert")
        fehler_gefunden += 1
    except Exception as e:
        print(f"❌ Test 3 fehlgeschlagen: Vergleichsoperator prüfen (>= statt <)")
    
    try:
        # Test 4: get_info() aufrufen
        info = auto.get_info()
        assert info is not None
        assert "BMW" in info
        print(f"✅ Test 4: get_info() gibt zurück: {info}")
        fehler_gefunden += 1
    except Exception as e:
        print(f"❌ Test 4 fehlgeschlagen: get_info() muss etwas zurückgeben (return)")
    
    try:
        # Test 5: tank_prozent() aufrufen
        prozent = auto.tank_prozent()
        assert prozent == 44.0
        print(f"✅ Test 5: tank_prozent() = {prozent}%")
        fehler_gefunden += 1
    except Exception as e:
        print(f"❌ Test 5 fehlgeschlagen: self.tank_kapazitaet verwenden!")
    
    print("\n" + "═" * 50)
    if fehler_gefunden == 5:
        print("🎉 SUPER! Alle 5 Fehler wurden behoben! 🎉")
    else:
        print(f"📊 Fortschritt: {fehler_gefunden}/5 Fehler behoben")
        print("💪 Weiter suchen!")
