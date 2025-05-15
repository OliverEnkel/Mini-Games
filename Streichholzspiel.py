print("Streichholzwegnehmspiel")
print("=======================")
print("Das Spiel ist auf zwei Spieler ausgelegt und funktioniert so:")
print("Hier liegen 21 Streichhölzer.")
print("Jeder von euch nimmt nun abwechselnd 1, 2 oder 3 Hölzer")
print("von dem Stapel. Wer den letzten Stab bekommt hat verloren.")

spieler1name = input("Wie heißt du, Spieler 1? ")
spieler2name = input("Wie heißt du, Spieler 2? ")

names = [spieler1name, spieler2name]
for name in names:
    print("Okay, " + name)

print("Das Spiel beginnt nun.")

ergebnis = 21  # Anzahl der Streichhölzer zu Beginn
aktueller_spieler = 0  # 0 für Spieler 1, 1 für Spieler 2
spieler_namen = [spieler1name, spieler2name]

while ergebnis > 0:
    print(f"\nEs sind noch {ergebnis} Streichhölzer übrig.")
    print(f"{spieler_namen[aktueller_spieler]}, du bist dran.")

    gueltige_eingabe = False
    while not gueltige_eingabe:
        try:
            wegnahme = int(input(f"Wie viele Streichhölzer nimmst du weg (1-3)? "))
            if 1 <= wegnahme <= 3 and wegnahme <= ergebnis:
                gueltige_eingabe = True
            else:
                print("Bitte nimm 1, 2 oder 3 Streichhölzer (nicht mehr als übrig sind).")
        except ValueError:
            print("Bitte gib eine Zahl ein.")

    ergebnis -= wegnahme

    if ergebnis == 0:
        print(f"\n{spieler_namen[aktueller_spieler]} hat verloren!")
        print(f"Herzlichen Glückwunsch, {spieler_namen[1 - aktueller_spieler]}!")
        print("Du hast gewonnen. ---> SPIELENDE")
    else:
        # Spieler wechseln (0 wird zu 1, 1 wird zu 0)
        aktueller_spieler = 1 - aktueller_spieler