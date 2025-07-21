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
    elif n3 == 1:
        return 1
    else:
        return fibonacci(n3-1) + fibonacci(n3-2)

def cantidad_letras(n4, n5, i=0):
    if i >= len(n4):
        return 0
    elif n4[i] == n5:
        return 1 + cantidad_letras(n4, n5, i + 1)
    else:
        return cantidad_letras(n4, n5, i + 1)

def invertir_texto(texto, i=0):
    if i == len(texto):
        return ""
    else:
        return invertir_texto(texto, i + 1) + texto[i]
def potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente == 1:
        return base
    else:
        return base * potencia(base, exponente - 1)

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
    elif opcion == 2:
        print("=== Suma de numeros naturales ===")
        n2 = int(input("Ingresa un numero: "))
        print(numero_natural(n2))
    elif opcion == 3:
        print("=== Fibonacci ===")
        n3 = int(input("Ingresa un numero: "))
        print(fibonacci(n3))
    elif opcion == 4:
        print("=== buscar letras en una palabra ===")
        n4 = input("Ingresa una palabra: ")
        n5 = input("Ingresa una letra: ")
        print(cantidad_letras(n4, n5))
    elif opcion == 5:
        print("=== Cadena de texto ===")
        texto = input("Ingrese un texto: ")
        print(invertir_texto(texto))
    elif opcion == 6:
        print("=== potencia de un numero ===")
        base = int(input("Ingresa un numero: "))
        exponente = int(input("Ingresa un numero: "))
        print(potencia(base, exponente))
    if opcion == 7:
        print("=== Salir ===")
        print("Saliendo")