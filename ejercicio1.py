def fizzbuzz(numero):
    """Recibe un número y devuelve el string correspondiente según las reglas de FizzBuzz."""
    if numero % 15 == 0:
        return "FizzBuzz"
    elif numero % 3 == 0:
        return "Fizz"
    elif numero % 5 == 0:
        return "Buzz"
    else:
        return str(numero)


if __name__ == "__main__":
    for i in range(1, 101):
        print(fizzbuzz(i))