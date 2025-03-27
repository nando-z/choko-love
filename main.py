import turtle
import math

# Function to draw the heart shape
def draw_heart():
    turtle.speed(0)
    turtle.color("red")
    turtle.begin_fill()
    for t in range(360):
        angle = math.radians(t)
        x = 16 * math.sin(angle)**3
        y = 13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)
        turtle.goto(x * 20, y * 20)  # Scale the heart
    turtle.end_fill()

# Function to write text inside the heart
def write_text():
    turtle.penup()
    turtle.goto(0, -50)
    turtle.color("white")
    turtle.write("JTM CHOKO", align="center", font=("Arial", 24, "bold"))
    turtle.hideturtle()

# Main function to set up the Turtle screen
def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("black")
    screen.title("Heart Shape with Turtle")
    turtle.penup()
    turtle.goto(0, 0)
    draw_heart()
    write_text()
    screen.mainloop()

if __name__ == "__main__":
    main()
