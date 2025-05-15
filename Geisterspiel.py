# CoderDojo Linz - Geisterspiel
from random import randint

print('Geisterspiel')
print('============')

score = 0  # Punktestand initialisieren
du_bist_mutig = True

while du_bist_mutig:
    geistertuer = randint(1, 3)
    print('Vor dir sind drei Türen.')
    print('Hinter einer ist ein Geist.')
    print('Welche Tür öffnest du?')
    tuer = input('1, 2 oder 3? ')
    tuer_nummer = int(tuer)

    if tuer_nummer == geistertuer:
        print('Lauf schnell weg!')
        du_bist_mutig = False
    else:
        print('Kein Geist!')
        print('Du bis ein Zimmer weiter.')
        score = score + 1

print('Game over! Deine Punkte: ', score)