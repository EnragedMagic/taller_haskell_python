# problem2.py
def coincide_password(guardada: str, entrada: str) -> bool:
    """
    Compara dos contraseñas.
    
    """
    if not entrada:  # si esta vacia
        return 
    return guardada.lower() == entrada.lower()


if __name__ == "__main__":
    PASSWORD = "Magic2005$"  # contraseña almacenada
    
    entrada = input("Escribe la contraseña: ").strip()
    
    if coincide_password(PASSWORD, entrada):
        print("Contraseña correcta ")
    else:
        print("Contraseña incorrecta ")

