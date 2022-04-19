def hcf(a, b):
    assert b == int(b) and a == int(a), 'error here'
    if b == 0:
        return a
    else:
        return hcf(b, a % b)


print(hcf(44, 18))
