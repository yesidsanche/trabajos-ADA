import turtle

name = input("Ingrese el nombre del jugador: ")

print("Hola ", name)

ventana = turtle.Screen()
ventana.bgcolor("black")
ventana.title("juego")
ventana.setup(700, 700)


class Dibujar(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)


# class Jugador(turtle.Turtle):
#    def __init__(self):
#        turtle.Turtle.__init__(self)
#        self.shape("circle")
#        self.color("green")
#        self.penup()
#        self.speed(0)


class Jugador(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('turtle')
        self.color("green")
        self.penup()
        self.speed(0)

    def mover_arriba(self):
        self.sety(self.ycor() + 10)

    def mover_abajo(self):
        self.sety(self.ycor() - 10)

    def mover_izquierda(self):
        self.setx(self.xcor() - 10)

    def mover_derecha(self):
        self.setx(self.xcor() + 10)


niveles = turtle.Turtle()


niveles = []

nivel_1 = [
    "P  xxxxxxxxxxxxxxxxxx",
    "    x               x",
    "x x xxxxx xxxxxxxxx x",
    "x x           x x x x",
    "x xxxxx x xxx x x x x",
    "x   x x x x     x   x",
    "x x x xxxxxxx x xxxxx",
    "x x   x     x x   x x",
    "xxxxx xxxxx x x xxx x",
    "x x x x       x   x x",
    "x x x xxxxxxx xxxxx x",
    "x   x   x   x x x   x",
    "xxx x xxxxx x x xxx x",
    "x x   x       x     x",
    "x x x xxx x x xxx x x",
    "x   x x   x x     x x",
    "xxx xxxxxxx xxx xxx x",
    "x x x x x x   x x   x",
    "x x x x x x x x x x x",
    "xxxxxxxxxxxxxxxxxxx  "
]

niveles.append(nivel_1)


def iniciar_juego(nivel):
    for fila in range(len(nivel)):
        for columna in range(len(nivel[fila])):
            x = nivel[fila][columna]
            screen_x = -288+(columna*24)
            screen_y = 288-(fila*24)
            if x == "x":
                dibujar.goto(screen_x, screen_y)
                dibujar.stamp()
            if x == "P":
                jugador.goto(screen_x, screen_y)


# instancia de la clase
jugador = Jugador()
dibujar = Dibujar()
# muñeco = Muñeco()

turtle.listen()
turtle.onkey(jugador.mover_arriba, 'Up')
turtle.onkey(jugador.mover_abajo, 'Down')
turtle.onkey(jugador.mover_izquierda, 'Left')
turtle.onkey(jugador.mover_derecha, 'Right')

iniciar_juego(niveles[0])


# mantener el juego abierto

turtle.mainloop()
