

def fizz_buzz(n) -> str:
    """
    :param n: int
    :return str
    """
    if n % 3 == 0 and n % 5 != 0:
        return "fizz"
    elif n % 3 != 0 and n % 5 == 0:
        return "buzz"
    elif n % 3 == 0 and n % 5 == 0:
        return "fizz buzz"
    else:
        return str(n)

for n in range(100):
    print(fizz_buzz(n))