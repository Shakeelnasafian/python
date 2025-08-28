import turtle

colors = ["red", "purple", "blue", "green", "orange", "yellow"]

t = turtle.Pen()          # or: t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)

for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x // 100 + 2)
    t.forward(x)
    t.left(59)            # 60 would be a perfect hexagon; 59 gives a spiral

turtle.done()
