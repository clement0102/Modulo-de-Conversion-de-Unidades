def crear_matriz_identidad(n: int) -> list[list[int]]:
    """
    Crea una matriz identidad de dimensión n x n.

    Args:
        n: Dimensión de la matriz.

    Returns:
        Una lista de listas que representa la matriz identidad.
    """
    return [
        [1 if i == j else 0 for j in range(n)]
        for i in range(n)
    ]

if __name__ == "__main__":

    try:
        # Prueba unitaria básica
        n = int(input("Ingrese la dimensión de la matriz: "))

        if n <= 0:
            raise ValueError("La dimensión debe ser un número entero positivo.")

        matriz = crear_matriz_identidad(n)

        print("\nMatriz identidad:")
        for fila in matriz:
            print(fila)

    except ValueError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

    finally:
        print("\nProceso de creación de la matriz finalizado.")