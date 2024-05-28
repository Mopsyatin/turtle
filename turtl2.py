import turtle as t
t.speed(10)
#t.hideturtle()
#============================================================================================================
dic = []

#============================================================================================================
def quadrat(color = 'black'):
    t.color = color
    t.pendown()
    t.dot(2)
    dic.append(t.position())
    t.penup()
#=============================================================================================================
def ifi():
    number = 0
    for l in dic:
        if str(l) == str(t.position()):
            number += 1
    t.forward(2)
    for l in dic:
        if str(l) == str(t.position()):
            number += 1
    t.backward(2)
    if number == 1:
        past = t.position()
        t.forward(1)
        t.right(90)
        t.forward(1)
        t.left(90)
        quadrat()
        t.goto(past)
#=============================================================================================================
t.penup()
t.goto(0,500)
quadrat()
t.goto(-50, 500)

for y in range(100):
    for g in range(101):
        ifi()
        t.forward(1)
    t.goto(-50, t.ycor() - 1)

    











#============================================================================================================




t.mainloop()