import time
known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

def main():
    n = 100
    start_time = time.time()
    t = fibonacci(n)
    elapsed_time = time.time() - start_time
    print(elapsed_time, ' seconds')
if __name__ == '__main__':
    main()
