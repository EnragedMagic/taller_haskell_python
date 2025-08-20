# problem5.py
IMPUESTOS = 53206000  

def debe_pagar_impuestos(edad: int, ingresos: float) -> bool:
    """
    Determina si un usuario debe pagar impuestos.
    """
    if edad < 0 or edad > 120:
        raise ValueError("Edad es valiida.")
    if ingresos < 0:
        raise ValueError("Ingresos no pueden ser negativos.")
    return edad >= 18 and ingresos >= IMPUESTOS


if __name__ == "__main__":
    try:
        edad = int(input("Ingrese su edad: "))
        ingresos = float(input("Ingrese el total acumulado de consignaciones anuales: "))

        if debe_pagar_impuestos(edad, ingresos):
            print("Debe pagar impuestos.")
        else:
            print("No debe pagar impuestos.")
    except ValueError as e:
        print("Error:", e)

