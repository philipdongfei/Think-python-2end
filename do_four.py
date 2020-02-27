def print_spam(s):
    print(s)

def do_twice(fun, s):
    fun(s)
    fun(s)

def do_four(fun, s):
    do_twice(fun, s)
    do_twice(fun, s)

'''

do_twice(print, 'spam')
print('')
do_four(print, 'spam')

'''
