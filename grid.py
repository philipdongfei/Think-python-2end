import do_four as m

def beam():
    s = '+ ' + '- '*4
    s *= 2
    s += '+'
    return s
def posts():
    s = '|'+' '*9
    s *= 2
    s += '|'
    return s
def thirdline():
    print(beam())
    #print(('+ '+'- '*4)*2+'+')
def fourline():
    m.do_four(print, posts())
    #m.do_four(print, ('|'+' '*9)*2+'|')
def print_grid():
    thirdline()
    fourline()
    thirdline()
    fourline()
    thirdline()
def main():
    print_grid()

if __name__ == '__main__':
    main()




