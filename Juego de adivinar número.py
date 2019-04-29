import random
magicalNumber = random.randint(0,100)
valorValido = False
c = 0

print (magicalNumber)
def verificarValor(num):
    if num > 100 or num < 0:
        print ("Error. Ingrese un valor entre 0 y 100")
        return False
    else:
        valorValido = True
        return valorValido


while c < 10:
    c = c + 1
    num = int(input("Ingrese un número: "))
    valorValido = verificarValor(num)
    if valorValido == True:
        if num <= (magicalNumber - 20) or num >= (magicalNumber + 20):
            print("Estás bastante lejos")
        elif num <= (magicalNumber - 10) or num >= (magicalNumber + 10):
            print("No estás muy lejos")
        elif num <= (magicalNumber - 1) or num >= (magicalNumber + 1):
            print("Estás muy cerca")
        elif num == magicalNumber:
            print("Correcto, ¡ganaste!")
            c = 15
    if c == 10:
        print("Perdiste, el número era: ", magicalNumber)
