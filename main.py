import turtle
import math

# إعداد الشاشة
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("JTM CHOKO")

# إعداد القلم
pen = turtle.Turtle()
pen.color("red")
pen.hideturtle()
pen.speed(5)

# رسم القلب باستخدام معادلة رياضية
pen.up()
pen.goto(0, -200)
pen.down()
pen.begin_fill()

for t in range(0, 360, 1):
    x = 16 * (math.sin(math.radians(t))**3)
    y = 13 * math.cos(math.radians(t)) - 5 * math.cos(2 * math.radians(t)) - 2 * math.cos(3 * math.radians(t)) - math.cos(4 * math.radians(t))
    pen.goto(x * 10, y * 10 - 100)

pen.end_fill()

# كتابة النص "JTM CHOKO"
pen.up()
pen.goto(-70, 30)
pen.color("white")
pen.write("JTM CHOKO", font=("Arial", 24, "bold"))

# إغلاق الشاشة عند النقر
screen.exitonclick()
