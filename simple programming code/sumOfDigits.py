def sumOfDigits(n):
    assert 0 <= n == int(n), 'error of negative number here'
    if n == 0:
        return 0
    else:
        return int(n % 10) + sumOfDigits(n // 10)


print(sumOfDigits(122))
