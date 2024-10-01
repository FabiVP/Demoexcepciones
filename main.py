while True:
    try:
        x = int(input("Ingrese un número natural: "))
        if x <= 0:
            raise ValueError("Debe ingresar un número mayor que 0.")

        # Calculando los divisores
        divisores = [i for i in range(1, x + 1) if x % i == 0]

        # Salir del ciclo si la entrada es válida
        break

    except ValueError as ve:
        print(f"Error: {ve}. Por favor, intente nuevamente.")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
    finally:
        print("Validando ingreso...")

# Mostrando los divisores
try:
    print(f"Los divisores de {x} son: {divisores}")
except Exception as e:
    print(f"El programa no puede imprimir los divisores: {e}")

