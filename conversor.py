# conversor.py

def celsius_a_fahrenheit(c):
    """Convierte grados Celsius a Fahrenheit."""
    return c * 1.8 + 32

def fahrenheit_a_celsius(f):
    """Convierte grados Fahrenheit a Celsius."""
    return (f - 32) / 1.8

def kilometros_a_millas(km):
    """Convierte kilómetros a millas."""
    return km * 0.621371
  
try:  
 # Menú interactivo de conversión
 print("Bienvenido al conversor de unidades.")
 print("Seleccione la conversión que desea realizar:")
 print("1. Celsius a Fahrenheit")
 print("2. Fahrenheit a Celsius")
 print("3. Kilómetros a Millas")

 opcion = input("Ingrese el número de la opción deseada (1-3): ")

 if opcion == "1":
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius}°C son {fahrenheit}°F.")
 elif opcion == "2":
    fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
    celsius = fahrenheit_a_celsius(fahrenheit)
    print(f"{fahrenheit}°F son {celsius}°C.")
 elif opcion == "3":
    kilometros = float(input("Ingrese la distancia en kilómetros: "))
    millas = kilometros_a_millas(kilometros)
    print(f"{kilometros} km son {millas} millas.")
 else:
    print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")
    
except ValueError:
    print("Ocurrió un error en la conversión. Por favor, verifica los valores ingresados.")
    
finally:
    print("Gracias por usar el conversor de unidades.")