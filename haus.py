# TODO: Aufgabe 1:
# Ändere den Code unten, so dass die Eigenschaften des Hauses als Attribute im Konstruktor definiert sind.
# Aktuell werden die Eigenschaften als separate Variablen definiert.
# Definiere einen Konstruktor (__init__), um die Attribute zu initialisieren.
class Haus:
    def __init__(self, quadratmeter, schlafzimmer, badezimmer):
        self.quadratmeter = quadratmeter
        self.schlafzimmer = schlafzimmer
        self.badezimmer = badezimmer
        print("Neues Haus wurde erstellt!")

haus1 = Haus(quadratmeter=120, schlafzimmer=3, badezimmer=2)

haus2 = Haus(quadratmeter=85, schlafzimmer=3, badezimmer=1)

print(f"Haus: {haus1.quadratmeter}m², {haus1.schlafzimmer} Schlafzimmer")
print(f"Haus: {haus2.quadratmeter}m², {haus2.schlafzimmer} Schlafzimmer")

haus3 =  Haus(quadratmeter=200, schlafzimmer=3, badezimmer=4)

print(f"Haus: {haus3.quadratmeter}m², {haus3.schlafzimmer} Schlafzimmer")


haus4 = Haus(quadratmeter=120, schlafzimmer=2, badezimmer= 3)
print(f"Haus hat {haus4.quadratmeter}m")
# TODO: Aufgabe 2: Erstelle drei weitere Objekte der Klasse Haus mit unterschiedlichen Eigenschaften.


# TODO: Aufgabe 3: Gib die Anzahl der Schlafzimmer und Badezimmer für jedes Haus aus.