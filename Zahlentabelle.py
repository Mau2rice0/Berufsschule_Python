# Aufgabenstellung:
# Schreiben sie eine Funktion, die eine Tabelle ausgibt.
# Die Zeilen und Spalten sind die Höhe und Breite eines Rechteckes. Die Felder Tabelle sind die Flächen des jew. Rechteckes.
# Als Parameter erhält die Funktion zwei Zahlen, die die Maximale Höhe und Breite der Tabelle angibt.
# Hinweis: Sie können "\t" (Tabulator) zur Formatierung nutzen.  

def tabelle(hoehe, breite):   # Erstellen der Funktion Tabelle, diese bekommt werte wie die Höhe und die Breite mitgegeben.
    for h in range(1, hoehe + 1): #for schleife auf den Zähler Höhe 
        for b in range(1, breite + 1): #for schleifer auf den Zähler Breite
            flaeche = h * b # Berechnung der Fläche
            print(f"{flaeche}\t", end="") # Ausgeben der Werte
        print() # Ausgeben von Daten



h = int(input("Höhe: ")) # Einlesen Der Höhe 
b = int(input("Breite: ")) #Einlesen der Breite
tabelle(h, b) #Aufrufen der Funktion 
