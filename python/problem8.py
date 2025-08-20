# problem8.py
def precio_boleto(edad: int) -> int:
    """
    Devuelve el precio del boleto según la edad.
    Categorías:
    - 0 a 3 años    -> 0
    - 4 a 12 años   -> 15000
    - 13 a 17 años  -> 20000
    - 18 a 64 años  -> 30000
    - 65+ años      -> 15000
    """
    if edad < 0 or edad > 120:
        raise ValueError("Edad no valida.")
    if edad <= 3:
        return 0
    elif edad <= 12:
        return 15000
    elif edad <= 17:
        return 20000
    elif edad <= 64:
        return 30000
    else:  # 65 en adelante
        return 15000


if __name__ == "__main__":
    try:
        edad = int(input("Ingrese la edad del cliente: "))
        precio = precio_boleto(edad)
        print(f"El precio de la entrada es: ${precio:,} COP")
    except ValueError as e:
        print("Error:", e)

