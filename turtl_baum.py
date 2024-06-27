#potoki
import turtle
import threading
#=========================================================================================
h_m = 8
turtles = [{} for _ in range(2**h_m)] 
turtles[0] = {"angle": 90,"pos": "", "pos2": "","pos3": (100,0), "x": 100}

#=========================================================================================
t = turtle.Turtle()
t.speed("fastest")
turtles[0].update({"turtle": t})
#=========================================================================================
def quadrat(wid, tr_id):
    for i in range(4):
        turtles[tr_id]["turtle"].forward(wid)
        turtles[tr_id]["turtle"].right(90)
        if i == 1:
            turtles[tr_id].update({"pos": turtles[tr_id]["turtle"].position()}) 
    turtles[tr_id]["turtle"].forward(wid)

def create(tr_id, f):
    quadrat(turtles[tr_id]["x"], tr_id)
    turtles[tr_id]["turtle"].right(60)
    print(turtles)
    turtles[1 + f].update({"angle": turtles[tr_id]["turtle"].heading() + 90})
    print(turtles)
    turtles[1 + f].update({"pos3": turtles[tr_id]["turtle"].position()})
    print(turtles)
    turtles[tr_id]["turtle"].forward(turtles[tr_id]["x"] * 0.86)
    print(turtles)
    turtles[1 + f].update({"x": turtles[tr_id]["x"] * 0.86})
    print(turtles)
    turtles[tr_id].update({"pos2": turtles[tr_id]["turtle"].position()}) 
    print(turtles)
    turtles[tr_id].update({"x": turtles[tr_id]["turtle"].distance(turtles[tr_id]["pos"])})  
    print(turtles)
    turtles[tr_id]["turtle"].goto(turtles[tr_id]["pos"])
    print(turtles)
    turtles[tr_id]["turtle"].goto(turtles[tr_id]["pos2"])
    print(turtles)
  
    

def create_turtle(x, id):
    t = turtle.Turtle()
    t.shapesize(0.2,0.2,0.3)
    t.shape('turtle')
    t.speed("fastest")
    t.up()
    t.goto(turtles[id]["pos3"])
    t.down()
    t.setheading(turtles[id]["angle"])
    turtles[id].update({"x": x})
    turtles[id].update({"turtle": t})
    

#=========================================================================================
turtles[0]["turtle"].up()
turtles[0]["turtle"].goto(turtles[0]["pos3"])
turtles[0]["turtle"].down()
turtles[0]["turtle"].setheading(turtles[0]["angle"])
#=========================================================================================
print(turtles)
for i in range(h_m):   
    for y in range(2 ** i ):
        create(y, 2 ** i + y - 1 )
        print(turtles)
        create_turtle(turtles[2 ** i + y]["x"], 2 ** i + y )
        print (turtles)
        # create(y + 1, 2 ** i + y + 1)

    
        






    
    





#=========================================================================================
turtle.mainloop()

