"""
Memory, puzzle game of number pairs.

Ejercicios:
1. Contar y desplegar el numero de taps
2. Detectar cuando todos los cuadros se han destapado
3. Central el dígito en el cuadro
4. Como un condimento de innovación al juego, Podrías utilizar algo diferente 
a los dígitos para resolver el juego y que al usuario le ayude a tener mejor memoria ?
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
#################################################################
#Se añaden nuevas variables que nos ayudarán con los ciclos o condicionales
cuenta=0
parejas=0
largo='nada'
indice=0
abecedario='A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AA','AB','AC','AD','AE','AF'
##################################################################


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


###############################################################################
#Se modificó la funciónn "tap" ya que esta es la que monitorea los clicks dados, y las parejas encontradas

def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']
    global cuenta
    global parejas
    cuenta=cuenta+1
    print(f'Número de Taps: {cuenta}')

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        
        
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        parejas+=1
        if (parejas==32):
            print("Has ganado, todas las parejas han sido encontradas")
###########################################################################################################


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
