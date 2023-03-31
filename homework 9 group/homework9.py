import turtle

# Створення вікна для малювання
wn = turtle.Screen()

# Створення об'єкту черепашки
t = turtle.Turtle()

# Малювання трикутника
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)

# Зупинка вікна
wn.mainloop()