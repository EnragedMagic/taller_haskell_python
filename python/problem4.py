# problem4.py
def par_o_impar(n: int) -> str:
    """
    Determina si un numero entero es par o impar.
    """
    return "Par" if n % 2 == 0 else "Impar"


if __name__ == "__main__":
    try:
        numero = int(input("Ingresa un numero entero: "))
        print(f"El numero {numero} es {par_o_impar(numero)}")
    except ValueError:
        print("Error: debes ingresar un numero entero valido.")
