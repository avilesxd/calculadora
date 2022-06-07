import time


def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def tabla_multiplicacion():
    num1 = int(input("Ingrese la tabla que desee saber: "))
    print("\n")
    for i in range(1, 13):
        print(f"{num1} x {i} = {num1 * i}")
    print("\n")


def division(num1, num2):
    return num1 / num2


def potenciatotal():
    base = int(input("Ingrese el numero base: "))
    print("\n")
    for i in range(1, 13):
        print(f"{base} ^ {i} = {base ** i}")


def raiz(num1):
    return num1 ** (1 / 2)


def menu():
    print("""
¿Qué operación desea realizar?

1. Suma
2. Resta
3. Multiplicación
4. División
5. Potencia
6. Raíz
7. Salir
    """)


def main():
    while True:
        menu()
        opcion = int(input("Elige una opción: "))

        while opcion < 1 or opcion > 7:
            print("Opción inválida")
            opcion = int(input("Elige una opción: "))

        if opcion == 1:
            num1 = float(input("Escribe el primer número: "))
            num2 = float(input("Escribe el segundo número: "))
            print(f"La suma de {num1} y {num2} es {suma(num1, num2)}")

        elif opcion == 2:
            num1 = float(input("Escribe el primer número: "))
            num2 = float(input("Escribe el segundo número: "))
            print(f"La resta de {num1} y {num2} es {resta(num1, num2)}")

        elif opcion == 3:
            tabla_multiplicacion()

        elif opcion == 4:
            num1 = float(input("Escribe el dividendo: "))
            num2 = float(input("Escribe el divisor: "))
            while num2 == 0:
                num2 = float(input("""No se puede dividir entre 0
Escribe otro número: """))
            print(f"La división de {num1} y {num2} es {division(num1, num2)}")

        elif opcion == 5:
            potenciatotal()

        elif opcion == 6:
            num1 = float(input("Escribe el número: "))
            print(f"La raíz de {num1} es {raiz(num1)}")

        elif opcion == 7:
            print("Saliendo...")
            time.sleep(2)
            print("Hasta pronto!")
            time.sleep(1)
            break


main()
