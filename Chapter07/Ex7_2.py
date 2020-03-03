import math

def eval_loop():
    while True:
        line = input('> ')
        if line == 'done':
            break
        print(eval(line))
    print('Done!')

def main():
    eval_loop()

if __name__ == '__main__':
    main()
