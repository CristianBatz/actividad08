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
    try:
        opcion = int(input("Seleccione una opcion: "))
    except ValueError:
        print("Opcion no valida")
        continue

    if opcion == 1:
        print("=== Factorial ===")
        try:
            n = int(input("Ingresa un numero: "))
            if n<0:
                print("Ha ingresado un numero negativo")
            else:
                print("Resultado:", factorial(n))
        except ValueError:
            print("Error: Debe ingresar un número entero.")

    elif opcion == 2:
        print("=== Suma de numeros naturales ===")
        try:
            n2 = int(input("Ingresa un numero: "))
            if n2 <= 0:
                print(" El número debe ser mayor que cero.")
            else:
                print("Resultado:", numero_natural(n2))
        except ValueError:
            print("Error: Ingrese un número válido.")

    elif opcion == 3:
        print("=== Fibonacci ===")
        try:
            n3 = int(input("Ingresa un numero: "))
            if n3 < 0:
                print("El número debe ser positivo.")
            else:
                print("Resultado:", fibonacci(n3))
        except ValueError:
            print("Error: Ingrese un número válido.")

    elif opcion == 4:
        print("=== buscar letras en una palabra ===")
        n4 = input("Ingresa una palabra: ")
        n5 = input("Ingresa una letra: ")
        if len(n5) != 1:
            print("Error: Debe ingresar solo una letra.")
        else:
            print("La letra aparece:", cantidad_letras(n4, n5), "veces")

    elif opcion == 5:
        print("=== Cadena de texto ===")
        texto = input("Ingrese un texto: ")
        print(f"Texto invertido: {invertir_texto(texto)}")

    elif opcion == 6:
        print("=== potencia de un numero ===")
        try:
            base = int(input("Ingresa un numero: "))
            exponente = int(input("Ingresa un numero: "))
            if exponente < 0:
                print("El exponente debe ser positivo.")
            else:
                print("Resultado:", potencia(base, exponente))
        except ValueError:
            print("Error: Ingrese solo números enteros.")

    elif opcion == 7:
        print("Saliendo")

    else:
        print("Opción no válida.")