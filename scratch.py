import turtle

sides = int(eval(input("введите количество сторон от 2 до 8: ")))
if  sides > 8 or sides < 2:
    print("Введите правильное число")
else:
    t = turtle.Pen()
    turtle.bgcolor('black')
    colors = ["red", "yellow" , "blue" , "orange" , "green" , "purple", "brown"]
    for x in range (360):
        t.pencolor(colors[x%sides])
        t.forward(x * 3/sides + x)
        t.left(360/sides + 1)
        t.width(x * sides/200)