import turtle as t
t.speed('fastest')
#t.hideturtle()
#============================================================================================================
dic = []
distance = -40
howm = 3
#============================================================================================================
def quadrat(color = 'black'):
    dic.append(t.position())
    t.fillcolor(color)
    t.begin_fill()
    t.pendown()
    for i in range(4):
        t.forward(10)
        t.right(90)
    t.end_fill()
    t.penup()
    t.forward(10)
#=============================================================================================================
def ifi():
    number = 0
    for l in dic:
        if str(l) == str(t.position()):
            number += 1
    t.forward(20)
    for l in dic:
        if str(l) == str(t.position()):
            number += 1
    t.backward(20)
    if number == 1:
        past = t.position()
        t.forward(10)
        t.right(90)
        t.forward(10)
        t.left(90)
        quadrat()
        t.goto(past)
#=============================================================================================================
t.penup()
t.goto(0,500)
quadrat()
t.goto(-20, 500)

while True:
    for x in range(howm):
        ifi()
        t.forward(10)
    t.goto(distance, t.ycor() - 10)
    howm += 3
    distance -= 10

    











#============================================================================================================




t.mainloop()