import turtle
import math

# terpy = turtle.Turtle()
hypotenuse = 50 * math.sqrt(2)

def process(terpy: turtle.Turtle, input: int=0, place: int = 1):
    print(input, place)
    if input:
        return legend[input](terpy, place)

def go_home(terpy: turtle.Turtle, place: int=1):
    terpy.penup()
    terpy.home()
    terpy.pendown()

    if place in (1, 10):
        south(terpy)
    else:
        north(terpy)
    terpy.home()

def south(terpy: turtle.Turtle):
    terpy.right(90)
    terpy.forward(100)

def north(terpy: turtle.Turtle):
    terpy.left(90)
    terpy.forward(100)

def one(terpy: turtle.Turtle, place: int=1):
    if place in (100, 1000):
        south(terpy)
    else:
        north(terpy)
    if place in (10, 100):
        terpy.left(90)
    else:
        terpy.right(90)
    terpy.forward(50)
    go_home(terpy, place)

def two(terpy: turtle.Turtle, place: int=1):
    if place in (100, 1000):
        south(terpy)
    else:
        north(terpy)
    terpy.backward(50)
    if place in (10, 100):
        terpy.left(90)
    else:
        terpy.right(90)
    terpy.forward(50)
    go_home(terpy, place)

def three(terpy: turtle.Turtle, place: int=1):
    if place in (100, 1000):
        south(terpy)
    else:
        north(terpy)
    if place in (10, 100):
        terpy.left(135)
    else:
        terpy.right(135)
    terpy.forward(hypotenuse)
    go_home(terpy, place)

def four(terpy: turtle.Turtle, place: int=1):
    if place in (100,1000):
        south(terpy)
    else:
        north(terpy)
    terpy.backward(50)
    if place in (10, 100):
        terpy.left(45)
    else:
        terpy.right(45)
    terpy.forward(hypotenuse)
    go_home(terpy, place)

def five(terpy: turtle.Turtle, place: int=1):
    if place in (100, 1000):
        south(terpy)
    else:
        north(terpy)
    if place in (10, 100):
        terpy.left(90)
    else:
        terpy.right(90)
    terpy.forward(50)
    if place in (10, 100):
        terpy.left(135)
    else:
        terpy.right(135)
    terpy.forward(hypotenuse)
    go_home(terpy, place)

def six(terpy: turtle.Turtle, place: int=1):
    if place in (100, 1000):
        south(terpy)
    else:
        north(terpy)
    if place in (10, 100):
        terpy.left(90)
    else:
        terpy.right(90)
    terpy.penup()
    terpy.forward(50)
    terpy.pendown()
    if place in (10, 100):
        terpy.left(90)
    else:
        terpy.right(90)
    terpy.forward(50)
    go_home(terpy, place)

def seven(terpy: turtle.Turtle, place: int=1):
    if place in (100, 1000):
        south(terpy)
    else:
        north(terpy)
    if place in (10, 100):
        terpy.left(90)
    else:
        terpy.right(90)
    terpy.forward(50)
    if place in (10, 100):
        terpy.left(90)
    else:
        terpy.right(90)
    terpy.forward(50)
    go_home(terpy, place)

def eight(terpy: turtle.Turtle, place: int=1):
    if place in (100, 1000):
        south(terpy)
    else:
        north(terpy)
    terpy.backward(50)
    if place in (10, 100):
        terpy.left(90)
    else:
        terpy.right(90)
    terpy.forward(50)
    if place in (10, 100):
        terpy.right(90)
    else:
        terpy.left(90)
    terpy.forward(50)
    go_home(terpy, place)

def nine(terpy: turtle.Turtle, place: int=1):
    if place in (100, 1000):
        south(terpy)
    else:
        north(terpy)
    if place in (10, 100):
        terpy.left(90)
    else:
        terpy.right(90)
    terpy.forward(50)
    if place in (10, 100):
        terpy.left(90)
    else:
        terpy.right(90)
    terpy.forward(50)
    if place in (10, 100):
        terpy.left(90)
    else:
        terpy.right(90)
    terpy.forward(50)
    go_home(terpy, place)


legend = {
    1: one,
    2: two,
    3: three,
    4: four,
    5: five,
    6: six,
    7: seven,
    8: eight,
    9: nine,
}

def main():
    finished = False
    terpy = turtle.Turtle()
    # terpy.hideturtle()
    while not finished:
        print("Enter number: ")
        num = input()
        terpy.clear()
        num_places = []

        if num:
            while len(num) and not len(num) > 4:
                num_places.append(int(num[-1]))
                num = num[:-1]
            print(num_places)

            # process(input1)()
            # terpy.home()
            place = 1
            while num_places:
                process(terpy=terpy,input=num_places.pop(0), place=place)
                place = place * 10

        else:
            finished = True
    print("done")
    turtle.done()


if __name__ == "__main__":
    main()