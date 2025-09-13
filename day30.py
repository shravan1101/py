# factorial(3) = 3*2*1

#  factorail(n) = n * factorial(n-1 )


def factorail(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorail(n - 1)


print(factorail(5))
