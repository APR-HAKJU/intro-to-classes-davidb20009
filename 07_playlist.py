"""
Übung 5: Playlist - Klassen in Klassen verwenden

Aufgabe:
Erstelle eine Klasse `Playlist` mit:
- Konstruktor mit Parameter: name (String, z.B. "Meine Lieblingslieder")
- Attribut: songs (Liste von Song-Objekten, startet leer)
- Methode song_hinzufuegen(song) mit Parameter:
  - Fügt einen Song zur Playlist hinzu
  - Gibt aus "➕ '{song.titel}' zur Playlist hinzugefügt"
- Methode song_entfernen(titel) mit Parameter:
  - Entfernt einen Song mit dem gegebenen Titel aus der Playlist
  - Gibt aus "➖ '{titel}' aus Playlist entfernt" (wenn gefunden)
  - Gibt aus "❌ Song '{titel}' nicht gefunden" (wenn nicht gefunden)
- Methode zeige_playlist() ohne Parameter:
  - Zeigt den Playlist-Namen und alle Songs mit ihren Infos
- Methode alle_abspielen() ohne Parameter:
  - Spielt alle Songs in der Playlist nacheinander ab

💡 Tipps:
- Importiere die Song-Klasse aus 05_song.py
- Eine Klasse kann Objekte von anderen Klassen als Attribute haben!
- Verwende eine for-Schleife um durch alle Songs zu iterieren
- Um einen Song zu entfernen: self.songs.remove(song)

Beispiel Ergebnis:
➕ 'Summer Vibes' zur Playlist hinzugefügt
➕ 'Neon Lights' zur Playlist hinzugefügt
➕ 'Ocean Wave' zur Playlist hinzugefügt

📋 Playlist: Meine Lieblingslieder
   Anzahl Songs: 3
   ---
   🎵 Song: Summer Vibes
      Interpreten: DJ Max, Sarah Sound
   🎵 Song: Neon Lights
      Interpreten: Electric Beats
   🎵 Song: Ocean Wave
      Interpreten: Chill Master, Wave Rider

➖ 'Neon Lights' aus Playlist entfernt

📋 Playlist: Meine Lieblingslieder
   Anzahl Songs: 2
   ---
   🎵 Song: Summer Vibes
      Interpreten: DJ Max, Sarah Sound
   🎵 Song: Ocean Wave
      Interpreten: Chill Master, Wave Rider

🎧 Playlist abspielen:
▶️ Song 'Summer Vibes' wird gespielt...
▶️ Song 'Ocean Wave' wird gespielt...
"""

# TODO: Importiere die Klasse Song aus 05_song
# from 05_song import Song


# TODO: Erstelle hier die Klasse Playlist


# TODO: Erstelle mehrere Song-Objekte mit Titeln und Interpreten deiner Wahl


# TODO: Erstelle eine Playlist mit einem Namen deiner Wahl


# TODO: Füge die Songs zur Playlist hinzu
# print()


# TODO: Zeige die Playlist
# print()


# TODO: Entferne einen Song aus der Playlist
# print()


# TODO: Zeige die Playlist erneut
# print()


# TODO: Spiele alle Songs ab
