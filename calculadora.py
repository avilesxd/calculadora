def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplicacion(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


def potencia(num1, num2):
    return num1 ** num2


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
            num1 = float(input("Escribe el primer número: "))
            num2 = float(input("Escribe el segundo número: "))
            print(f"La multiplicación de {num1} y {num2} es {multiplicacion(num1, num2)}")

        elif opcion == 4:
            num1 = float(input("Escribe el dividendo: "))
            num2 = float(input("Escribe el divisor: "))
            while num2 == 0:
                num2 = float(input("""No se puede dividir entre 0
Escribe otro número: """))   
            print(f"La división de {num1} y {num2} es {division(num1, num2)}")

        elif opcion == 5:
            num1 = float(input("Escribe el número base: "))
            num2 = float(input("Escribe el exponente: "))
            print(f"La potencia de {num1} y {num2} es {multiplicacion(num1, num2)}")

        elif opcion == 6:
            num1 = float(input("Escribe el número: "))
            print(f"La raíz de {num1} es {raiz(num1)}")

        elif opcion == 7:
            print("Adiós, hasta pronto")
            break

main()