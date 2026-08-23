import sys

from herramientas.matriz import crear_matriz_identidad


print("Rutas actuales de búsqueda de Python:")
for ruta in sys.path:
    print(ruta)


# Agregar manualmente una ruta absoluta personalizada
ruta_personalizada = r"C:\ruta\personalizada"
sys.path.append(ruta_personalizada)

print("\nRutas después de agregar la ruta personalizada:")
for ruta in sys.path:
    print(ruta)


# Utilizar la función importada
print("\nMatriz identidad de 3 x 3:")

matriz = crear_matriz_identidad(3)

for fila in matriz:
    print(fila)