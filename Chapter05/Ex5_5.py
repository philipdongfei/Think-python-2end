import turtle

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

def main():
    length = int(input('Enter the length: '))
    n = int(input('Enter the n: '))
    bob = turtle.Turtle()
    draw(bob, length, n)
    turtle.mainloop()

if __name__ == '__main__':
    main()


