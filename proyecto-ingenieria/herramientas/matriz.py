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


if __name__ == '__main__':
    # Prueba unitaria básica
    matriz = crear_matriz_identidad(3)

    for fila in matriz:
        print(fila)