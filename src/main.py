import turtle


def apply_rules(axiom, rules):
    """Applies the L-system rules to a string."""
    result = ""
    for char in axiom:

        result += rules.get(char, char)
    return result


def generate_lsystem(iterations, axiom, rules):
    """Generates the final L-system string after a number of iterations."""
    system_string = axiom
    for _ in range(iterations):
        system_string = apply_rules(system_string, rules)
    return system_string


def draw_lsystem(t, instructions, angle, distance):
    """Interprets the L-system string and draws it with the turtle."""
    stack = []
    for command in instructions:
        if command == "F" or command == "G":

            t.forward(distance)
        elif command == "+":

            t.right(angle)
        elif command == "-":

            t.left(angle)
        elif command == "[":

            position = t.position()
            heading = t.heading()
            stack.append((position, heading))
        elif command == "]":

            position, heading = stack.pop()
            t.penup()
            t.setposition(position)
            t.setheading(heading)
            t.pendown()


def main():

    ITERATIONS = 5
    AXIOM = "FF"
    RULES = {"F": "F[+F][-F][-F]F"}
    ANGLE = 55
    BRANCH_LENGTH = 10

    instructions = generate_lsystem(ITERATIONS, AXIOM, RULES)

    screen = turtle.Screen()
    screen.bgcolor("black")

    t = turtle.Turtle()
    t.speed(0)
    t.color("green")
    t.hideturtle()
    t.left(90)
    t.penup()

    t.setpos(0, -screen.window_height() / 2 + 50)
    t.pendown()

    draw_lsystem(t, instructions, ANGLE, BRANCH_LENGTH)

    print("Fractal tree drawing complete.")
    screen.exitonclick()


if __name__ == "__main__":
    main()
