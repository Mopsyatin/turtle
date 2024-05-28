#potoki
import turtle
import threading
#=========================================================================================
turtles = []
tr_angle = [90]
tr_pos = []
tr_pos2 = []
tr_pos3 = [(100,0)]
tr_x = [100]
#=========================================================================================
t = turtle.Turtle()
t.speed('fastest')
turtles.append(t)
#=========================================================================================
def quadrat(wid, tr_id):
    for i in range(4):
        turtles[tr_id].forward(wid)
        turtles[tr_id].right(90)
        if i == 1:
            if len(tr_pos) >= tr_id + 1:
                tr_pos[tr_id] = turtles[tr_id].position()
            else:
                tr_pos.append(turtles[tr_id].position())
    turtles[tr_id].forward(wid)

def create(tr_id):
    quadrat(tr_x[tr_id], tr_id)
    turtles[tr_id].right(60)
    tr_angle.append(turtles[tr_id].heading() + 90)
    tr_pos3.append(turtles[tr_id].position())
    turtles[tr_id].forward(tr_x[tr_id] * 0.86)
    tr_x.append(tr_x[tr_id] * 0.86)
    if len(tr_pos2) >= tr_id + 1:
        tr_pos2[tr_id] = turtles[tr_id].position()
    else:
        tr_pos2.append(turtles[tr_id].position())
    tr_x[tr_id] = turtles[tr_id].distance(tr_pos[tr_id]) 
    turtles[tr_id].goto(tr_pos[tr_id])
    turtles[tr_id].goto(tr_pos2[tr_id])
  
    

def create_turtle(x, id):
    t = turtle.Turtle()
    t.shapesize(0.2,0.2,0.3)
    t.shape('turtle')
    t.speed('fastest')
    t.up()
    t.goto(tr_pos3[id])
    t.down()
    t.setheading(tr_angle[id])
    tr_x.append(x)
    turtles.append(t)
    

#=========================================================================================
turtles[0].up()
turtles[0].goto(tr_pos3[0])
turtles[0].down()
turtles[0].setheading(tr_angle[0])
#=========================================================================================
for i in range(8):
    for i in range(len(turtles)):
        create(i)
        create_turtle(tr_x[i + 1], i + 1)
        create(i + 1)
        






    
    





#=========================================================================================
turtle.mainloop()