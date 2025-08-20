# problem1.py
def verificar_edad(edad: int) -> str:
    """
    Verifica si la edad ingresada corresponde a un mayor o menor de edad.
    """
    if edad < 0 or edad > 120:
        return "Error: edad no valida"
    return "Mayor de edad" if edad >= 18 else "Menor de edad"

if __name__ == "__main__":
    try:
        edad = int(input("Ingresa tu edad: "))
        print(verificar_edad(edad))
    except ValueError:
        print("Error: debes ingresar un nmero entero.")

