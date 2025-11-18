# Ohne Klassen - unübersichtlich
name1 = "Max"
alter1 = 25
name2 = "Anna"  
alter2 = 30

# Mit Klasse - strukturiert
class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    
    def vorstellen(self):
        return f"Hallo, ich bin {self.name} und {self.alter} Jahre alt"

# Objekte erstellen
person1 = Person("Max", 25)
person2 = Person("Anna", 30)
person3 = Person("Jonas", 15)
person4 = Person("Peter", 67)
print(person1.vorstellen())
print(person2.vorstellen())
print(person3.vorstellen())
print(person4.vorstellen())
