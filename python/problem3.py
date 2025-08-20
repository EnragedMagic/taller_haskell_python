# problem3.py
def dividir(a: float, b: float):
    """
    Realiza la división a / b.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: dividiste por cero"


if __name__ == "__main__":
    try:
        a = float(input("Numerador: "))
        b = float(input("Denominador: "))
        resultado = dividir(a, b)
        print("Resultado:", resultado)
    except ValueError:
        print("Error ingrese numeros validos.")
