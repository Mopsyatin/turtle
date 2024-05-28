import turtle as t
import random as r
t.speed('fatsest')
#=========================================================================================
start_size = 100
def generate(number = 0):
    if number < 3:
        number = r.randint(3,10)
    print(number)
    for i in range(number):
        t.forward(start_size)
        t.right((180*(number - 2))/number)
#=========================================================================================
generate()
t.mainloop()