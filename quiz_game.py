#Begrüst den spieler
print("Wilkommen zu meinem quiz")

#Fragt Nach deinem Namen und Begrüst dich dann mit deinem Namen
name = input("Was ist dein Name ")
print("Hallo " + name)

#Fragt ob der spieler spielen möchte wenn er etwas anderes schreibt wird das programm sofort gestopt
playing = input("Willst du spielen ")

if playing.lower() != "ja":
            quit()

#kurtz die regeln erklärt
print("Ok dann hier kurtz die regeln :)")

print("Du musst gleich 5 allgemeine Fragen beantworten")

print("Du musst die Fragen alle Richtig beantwirten sobalt eine frage Falsch ist Stop das Spiel")

#Noch eine Nachricht das das spiel jetzt Startet
print("So dann legen wir mal los")

#Erste Frage
answer1 = input("Was ist die Hauptstadt von Schottland? ")
if answer1.lower() == "edinburgh":
    print("Richtig")
else:
        print("Falsche Antwort")
        quit(print("Jetzt bist du Leider Raus"))

#Giebt eine nette nachricht nach der ersten Frage aus
if answer1.lower() == "edinburgh":
    print("Die erste Frage war schonmal gut")
    
#Zweite Frage
answer2 = input("Ist Donald Trump noch der President von den USA? ")
if answer2.lower() == "nein":
    print("Ja Richtig")
else:
        print("Nein das ist die Falsche Antwort")
        quit(print("Jetzt bist du Leider Raus"))

#Nachricht das jetzt eine ja nein frage kommt
print("Jetzt kommt eine ja nein Frage")

#Dritte Frage
answer3 = input("Ist rauchen Gesund? ")
if answer3.lower() == "nein":
    print("Ja Richtig")
else:
        print("Nein das ist die Falsche Antwort")
        quit(print("Jetzt bist du Leider Raus"))

#Vierte Frage
answer4 = input("Wie lautet die Hauptstadt von Frankreich? ")
if answer4.lower() == "paris":
    print("Ja Richtig")
else:
        print("Nein das ist die Falsche Antwort")
        quit(print("Jetzt bist du Leider Raus"))

#Fünfte Frage
answer5 = input("Welcher Agent steht im Zusammenhang mit der Lizenz zum Töten? ")
if answer5.lower() == "james bond":
    print("Ja Richtig")
else:
        print("Nein das ist die Falsche Antwort")
        quit(print("Jetzt bist du Leider Raus"))

#Das spiel ist zu Ende Nachrichten
print("Super " + name + " du hast es Geschafft")

#Github Link damit die user sich den code angucken können (wenn man das will)
print("Hier kannst den code von dem Kleinen quiz finden ihr könnt es gernen nach euren beliben anpassen :)")
print("quiz github Link wenn es einen giebt")
