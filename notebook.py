#Klasse für Laptops mit den Eigenschaften:
#   -  RAM Größe
#   -  Marke
#   -  Modell
#   -  Bildschirmgröße

notebook_ram_1 = 16
notebook_ram_2 = 32

notebook_1_marke = "Apple"
notebook_2_marke = "Lenovo"

notebook_1_modell = "Macbook Air"
notebook_2_modell = "Thinkpad 14"

notebook_1_bildschirmgröße = 14.1
notebook_2_bildschirmgröße = 16

class Notebook: # class + Name - > legt neuen Bauplan an
    def __init__(self, ram, marke, modell, bildschirmgröße):
        self.ram = ram 
        self.marke = marke
        self.modell = modell
        self.bildschirmgröße = bildschirmgröße
        print(f"Neues Notebook mit Marke: " + marke + "wurde erstellt. ")

nb_1 = Notebook(16, "Apple", "Macbook Pro", 14,2)