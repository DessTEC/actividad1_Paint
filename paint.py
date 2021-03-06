"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.

"""

from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circleDraw(start, end): #Se cambia el nombre de la función
    "Draw circle from start to end."
    up()
    goto(start.x, start.y) #Se mueve el cursor al punto inicial
    down()
    begin_fill()

    circle(end.x - start.x) #Se usa la función de la librería turtle, pasando como radio la distancia entre el punto inicial y final en x

    end_fill()


def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y) #mover el cursor al punto inicial
    down()
    begin_fill()

    for count in range(4): #Se dibujan los 4 lados
        if count % 2 == 0: #Si el lado es par su longitud es la distancia entre el punto inicial y final de x y sino mide el doble
            forward(end.x - start.x)
        else:
            forward((end.x - start.x)*2)
        left(90)

    end_fill()

def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y) #Se mueve el cursor al punto inicial
    down()
    begin_fill()

    for count in range(3): #Se van a dibujar los tres lados
        forward(end.x - start.x) #Cada lado medirá lo mismo
        left(120) #Se gira 120 grados para que cada par de lados formen 60 grados

    end_fill()

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('magenta'), 'M') #Se define un nuevo color, de la libreria turtle y se le asigna una tecla
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
