import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

t.pensize(3)
t.pencolor("purple")
t.shape("turtle")

for x in range(4):
    t.right(90)
    t.forward(100)

for x in range(3):
    t.left(120)
    t.forward(100)

win.mainloop()
