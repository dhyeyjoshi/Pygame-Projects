import turtle
wn = turtle.Screen()
wn.bgcolor('black')
Albert = turtle.Turtle()
Albert.speed(10)
Albert.color('white')
def square(length,angle):
    for i in range(4):
        Albert.forward(length)
        Albert.right(angle)
while True:
    square(100,90)
    Albert.right(11)
