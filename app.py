
from calculadora import (
    sumar, restar, multiplicar, dividir,
    potencia, raiz_cuadrada, porcentaje, modulo
)

historial = []

operaciones = {
    "1": ("Suma", sumar),
    "2": ("Resta", restar),
    "3": ("Multiplicacion", multiplicar),
    "4": ("Division", dividir),
    "5": ("Potencia", potencia),
    "6": ("Raiz cuadrada", raiz_cuadrada),
    "7": ("Porcentaje", porcentaje),
    "8": ("Modulo", modulo),
}


def mostrar_menu():
    print("\n===== CALCULADORA =====")
    for clave, (nombre, _) in operaciones.items():
        print(f"{clave}. {nombre}")
    print("9. Ver historial")
    print("0. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ")

        if opcion == "0":
            print("Hasta luego")
            break

        if opcion == "9":
            print("\n--- HISTORIAL ---")
            if not historial:
                print("No hay operaciones registradas")
            for registro in historial:
                print(registro)
            continue

        if opcion not in operaciones:
            print("Opcion no valida")
            continue

        nombre, funcion = operaciones[opcion]

        try:
            a = float(input("Primer numero: "))

            if opcion == "6":
                resultado = funcion(a)
                detalle = f"{nombre}({a}) = {resultado}"
            else:
                b = float(input("Segundo numero: "))
                resultado = funcion(a, b)
                detalle = (
                    f"{nombre}({a}, {b}) = {resultado}"
                )

            print(f"Resultado: {resultado}")
            historial.append(detalle)

        except ValueError as error:
            print(f"Error: {error}")
        except OverflowError:
            print("Error: resultado demasiado grande")


if __name__ == "__main__":
    main()
