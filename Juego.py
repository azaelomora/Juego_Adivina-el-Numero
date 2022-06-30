from random import *

nombre = input('¿Cuál es tu nombre? ')
print(f"""Bueno {nombre}, he pensado un número entre el 1 y el 100 y como eres tan cool, sé que lo adivinarás de forma sencilla.

Solo tienes 8 oportunidades.

¡Qué comience el juego!""")

'''Número Random y cantidad de intentos'''
numer_random = randint(1,100)
intentos = 7

a = int(input('Ingresa un número: '))
while (a != numer_random) and (intentos != 0):
    if a < numer_random:
        print(f'''Respuesta incorrecta {nombre}.
        Elegiste un número menor al número secreto.\n''')
        intentos -=1
        a = int(input('Ingresa un número diferente: '))
    elif a > numer_random:
        print(f'''Respuesta incorrecta {nombre}.
        Elegiste un número mayor al número secreto.\n''')
        intentos -=1
        a = int(input('Ingresa un número diferente: '))
else:
    if a == numer_random:
        print(f'''Felicidades {nombre}, acertaste, ¡has ganado!
        Lo lograste en {intentos-8} intentos''')
    else:
        print(f'''¡Qué mala suerte :/! {nombre}, has gastado todos tus intentos.
        El número secreto era {numer_random}.
    ¡Has perdido :(!''')

