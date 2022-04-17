def fib(n):
    assert 0 <= n == int(n), 'fib cannot be proper function'
    if n in [0, 1]:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(4))
