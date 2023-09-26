def factorial(n: int) -> int:
    """
    :param n:int
    :return int
    """
    f = 1

    for i in range(n):
        f*= (i+1)
    return f

for i in range(35):
    print(factorial(i))  




