def fib(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, b + a
    print()
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
