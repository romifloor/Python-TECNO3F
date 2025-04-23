"""Imprimir un mensaje de error si no se pasan suficientes argumentos"""

def procesar_argumentos(*args):
    try:
        if len(args) < 2:  # Ajusta el número mínimo de argumentos según tu necesidad
            raise ValueError("Error: Se requieren al menos 2 argumentos.")
        print(f"Argumentos recibidos: {args}")
    except ValueError as e:
        print(e)
    finally:
        print("Ejecución finalizada.")

while True:
    entrada = input("Introduce valores separados por espacios (o 'salir' para terminar): ")
    if entrada.lower() == "salir":
        break
    valores = entrada.split()
    procesar_argumentos(*valores)









  




