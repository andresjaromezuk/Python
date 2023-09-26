def sum_eo(n,t):
    """Esto es un docstring"""
    suma = 0
    try:
        if t == 'e':
            for i in range(n):
                if (i % 2) == 0:
                    suma += i
            return suma
        elif t == 'o':
            for i in range(n):
                if (i % 2) != 0:
                    suma += i
            return suma
        else:
            raise ValueError("Este valor no corresponde")
    except ValueError:
        print("Ingresá otro valor")

def fibonacci(n):
    n /2 