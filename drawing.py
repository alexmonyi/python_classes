import turtle

def draw_square(turtle_instance, side_length):
    for _ in range(4):
        turtle_instance.forward(side_length)
        turtle_instance.right(90)

def main():
    turtle.speed(1)
    turtle.shape("turtle")
    
    print("Welcome to the Simple Drawing Game!")
    print("You can draw a square by clicking on the turtle window.")
    
    turtle.onscreenclick(lambda x, y: draw_square(turtle.Turtle(), 50), 1)
    
    turtle.done()

if __name__ == "__main__":
    main()
