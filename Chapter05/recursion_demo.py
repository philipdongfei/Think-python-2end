def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

def dothing():
    print('func')
def do_n(func, n):
    if n <= 0:
        return
    func(n)
    do_n(func, n-1)
'''
countdown(3)
print('')
print_n('print n...', 4)
print('')
'''
#func = countdown(4)
do_n(countdown, 3)

