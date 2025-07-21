def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
def numero_natural(n2):
    if n2 == 1:
        return 1
    else:
        return n2 + numero_natural(n2-1)
def fibonacci(n3):
    if n3 == 0:
        return 0
    else:
        return n3 + fibonacci(n3-1)


opcion = 0
while opcion != 7:
    print("=== Menu Matematico ===")
    print("1 - Factorial")
    print("2 - Suma de numeros naturales")
    print("3 - Fibonacci")
    print("4 - buscar cantidad de letras en una palabra")
    print("5 - cadena de texto")
    print("6 - potencia de un numero")
    print("7 - salir")
    opcion = int(input("Seleccione una opcion: "))
    if opcion == 1:
        print("=== Factorial ===")
        n = int(input("Ingresa un numero: "))
        print(factorial(n))
    if opcion == 2:
        print("=== Suma de numeros naturales ===")
        n2 = int(input("Ingresa un numero: "))
        print(numero_natural(n2))
    if opcion == 3:
        print("=== Fibonacci ===")
        n3 = int(input("Ingresa un numero: "))
        print(fibonacci(n3))
