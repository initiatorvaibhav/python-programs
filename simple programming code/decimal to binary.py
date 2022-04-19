def dcm(n):
    assert n == int(n) and n >= 0, 'error here'
    if n == 0:
        return 0
    else:
        return (n % 2) + 10 * dcm(n//2)


print(dcm(7))
