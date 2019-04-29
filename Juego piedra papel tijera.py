import random

#piedra = 1
#papel = 2
#tijera = 3

CPUroundsWin = 0
PersonRoundsWin = 0

def logicaPartida(CPUselection,PersonSelection):
    if CPUselection == PersonSelection:
        return 0
    elif CPUselection == 1 and PersonSelection == 2:
        return 1
    elif CPUselection == 1 and PersonSelection == 3:
        return 2
    elif CPUselection == 2 and PersonSelection == 1:
        return 2
    elif CPUselection == 2 and PersonSelection == 3:
        return 1
        PersonRoundsWin = PersonRoundsWin + 1
    elif CPUselection == 3 and PersonSelection == 1:
        return 1
    elif CPUselection == 3 and PersonSelection == 2:
        return 2

print("¡Bienvenido!")
print("Para jugar elija una de las 3 opciones:")


while CPUroundsWin < 3 and PersonRoundsWin < 3:
    CPUselection = random.randint(1,3)
    print("1. Piedra\n"
          "2. Papel\n"
          "3. Tijera")
    PersonSelection = int(input("Ingrese la opción deseada: "))
    var = logicaPartida(CPUselection,PersonSelection)
    if var == 0:
        print("Empate")
    elif var == 1:
        print("Usted gana la ronda")
        PersonRoundsWin = PersonRoundsWin + 1
    else:
        print("La computadora gana la ronda")
        CPUroundsWin = CPUroundsWin + 1

print("¡Fin de la partida!")
if CPUroundsWin > PersonRoundsWin:
    print("La computadora gana la partida")
else:
    print("Usted gana la partida")

print("Resultado final:")
print("Usted: ", PersonRoundsWin)
print("La computadora: ", CPUroundsWin)