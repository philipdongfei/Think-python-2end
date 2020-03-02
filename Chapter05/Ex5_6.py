import turtle

def koch(t, x):
    """
    Draws a koch curve with length x.
    """
    if x < 10:
        t.fd(x)
        return
    m = x / 3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)
def snowflake(t, x):
    """
    Draws a snowflake
    (a triangle with a koch curve for each side).
    """
    for i in range(3):
        koch(t, x)
        t.rt(120)

def main():
    bob = turtle.Turtle()

    bob.pu()
    bob.goto(-150, 90)
    bob.pd()
    snowflake(bob, 300)
    turtle.mainloop()
if __name__ == '__main__':
    main()

