def sumOfDigits(n):
    if n == 0:
        return 0
    else:
        return int(n % 10) + sumOfDigits(n / 10)


print(sumOfDigits(501))
