"""
Übung 8: Fehlersuche - Bibliothek

🔍 AUFGABE:
In der Klasse 'Buch' sind 5 FEHLER versteckt!
Finde und behebe alle Fehler.

💡 TIPPS:
- Achte auf den Konstruktor (__init__)
- Achte auf self bei Attributen
- Achte auf Einrückungen
- Achte auf Parameter

🎯 FEHLER-CHECKLISTE (zum Abhaken):
[ ] Fehler 1: _______________
[ ] Fehler 2: _______________
[ ] Fehler 3: _______________
[ ] Fehler 4: _______________
[ ] Fehler 5: _______________

Wenn alle Fehler behoben sind, erscheint am Ende:
✅ SUPER! Alle 5 Fehler wurden behoben!
"""


class Buch:
    # FEHLER 1: Wie heißt der Konstruktor richtig?
    def _init_(self, titel, autor, seiten):
        # FEHLER 2: Wie speichert man ein Attribut richtig?
        titel = titel
        self.autor = autor
        self.seiten = seiten
        self.gelesen = False

    # FEHLER 3: Was fehlt in den Klammern?
    def lesen():
        self.gelesen = True
        print(f"📖 Du liest '{self.titel}' von {self.autor}")

    def info_anzeigen(self):
        status = "✅ Gelesen" if self.gelesen else "📕 Noch nicht gelesen"
        # FEHLER 4: Achte auf die Einrückung!
    print(f"📚 {self.titel} - {self.autor} ({self.seiten} Seiten)")
        print(f"   Status: {status}")

    # FEHLER 5: Was fehlt bei der Methodendefinition?
    def seiten_uebrig(self, aktuelle_seite)
        return self.seiten - aktuelle_seite


# ═══════════════════════════════════════════════════════════════
# 🧪 TESTCODE - Nicht verändern! Zeigt ob alles funktioniert.
# ═══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    fehler_gefunden = 0
    
    print("🔍 Teste die Buch-Klasse...\n")
    
    try:
        # Test 1: Objekt erstellen
        buch = Buch("Harry Potter", "J.K. Rowling", 300)
        print("✅ Test 1: Buch-Objekt erstellt")
        fehler_gefunden += 1
    except Exception as e:
        print(f"❌ Test 1 fehlgeschlagen: {e}")
    
    try:
        # Test 2: Titel prüfen
        assert buch.titel == "Harry Potter"
        print("✅ Test 2: Titel korrekt gespeichert")
        fehler_gefunden += 1
    except Exception as e:
        print(f"❌ Test 2 fehlgeschlagen: Titel nicht als self.titel gespeichert")
    
    try:
        # Test 3: lesen() aufrufen
        buch.lesen()
        print("✅ Test 3: lesen() funktioniert")
        fehler_gefunden += 1
    except Exception as e:
        print(f"❌ Test 3 fehlgeschlagen: {e}")
    
    try:
        # Test 4: info_anzeigen() aufrufen
        buch.info_anzeigen()
        print("✅ Test 4: info_anzeigen() funktioniert")
        fehler_gefunden += 1
    except Exception as e:
        print(f"❌ Test 4 fehlgeschlagen: {e}")
    
    try:
        # Test 5: seiten_uebrig() aufrufen
        uebrig = buch.seiten_uebrig(50)
        assert uebrig == 250
        print("✅ Test 5: seiten_uebrig() funktioniert")
        fehler_gefunden += 1
    except Exception as e:
        print(f"❌ Test 5 fehlgeschlagen: {e}")
    
    print("\n" + "═" * 50)
    if fehler_gefunden == 5:
        print("🎉 SUPER! Alle 5 Fehler wurden behoben! 🎉")
    else:
        print(f"📊 Fortschritt: {fehler_gefunden}/5 Fehler behoben")
        print("💪 Weiter suchen!")
