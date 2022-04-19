def power(n, j):
    assert 0 <= n == int(n), 'error here'
    if j == 1:
        return n
    else:
        return n * power(n, j - 1)


print(power(4, 3))
