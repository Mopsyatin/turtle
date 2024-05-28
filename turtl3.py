import turtle as t
t.speed(10)
t.shape('turtle')
#t.hideturtle()
#============================================================================================================
dic = []

#============================================================================================================
def quadrat(color = 'black'):
    t.color = color
    t.pendown()
    t.stamp()
    dic.append(t.position())
    t.penup()
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
t.goto(-500, 500)

for y in range(100):
    for x in range(101):
        ifi()
        t.forward(10)
    t.goto(-500, t.ycor() - 10)

    











#============================================================================================================




t.mainloop()