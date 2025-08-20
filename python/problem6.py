# problem6.py
def determinar_grupo(nombre: str, genero: str) -> str:
    """
    Determina el grupo del estudiante segun su nombre y genero.
  
    """
    """
    Mujeres: Grupo A si el nombre empieza con letra 'M' o anteriores.
    Hombres: Grupo A si el nombre empieza con letra 'N' o posteriores.
    El resto para el Grupo B.
    """
    if not nombre or not genero:
        return "Error: datos invalidos."

    inicial = nombre.strip()[0].upper()
    genero = genero.strip().upper()

    if genero == "F" and inicial < "M":
        return "Grupo A"
    elif genero == "M" and inicial >= "N":
        return "Grupo A"
    else:
        return "Grupo B"


if __name__ == "__main__":
    nombre = input("Ingrese su nombre: ")
    genero = input("Ingrese el genero que sale en su cedula (M o F): ")

    print("Usted esta en el grupo:", determinar_grupo(nombre, genero))

