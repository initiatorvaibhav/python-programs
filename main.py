# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def fac(n):
    if n in [0, 1]:
        return 1
    else:
        return n * fac(n - 1)


print(fac(4))
