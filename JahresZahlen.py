# JahrensZahlen auflisten von einem Startpunkt bis zu einem Fest definierten Endpunkt
#Version 1.0
#Author Maurice Flöthmann

jahr = int(input("Jahr: ")) #Dort wird die Variable jahr eingelesen, diese Definiert den Startpunkt der aufzählung
Monat = 1 # Diese Variable gibt an in wie großen schritten die aufzälung aufzählen soll
ende = jahr+2 # Defieniert den Endpunkt der Aufzählung
for i in range(1,13): # Starte die Wieder Holung der Aufzählung für das erste Jahr
    print(f"{jahr}- {i} ") #Gibt den Jahreswert aus und rechnet diesen +1
    

for i in range(1,13): # Starte die Wieder Holung der Aufzählung für das zweite Jahr
    print(f"{jahr+1} - {i} ") #Gibt den Jahreswert aus und rechnet diesen +1
 

for i in range(1,13): # Starte die Wieder Holung der Aufzählung für das dritte Jahr
    print(f"{jahr+2} - {i} ") #Gibt den Jahreswert aus und rechnet diesen +1
