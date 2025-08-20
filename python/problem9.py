# problem9.py
BASE = ["mozzarella", "tomate"]
ING_VEGET = ["Maiz tierno", "Platano maduro caramelizado", "Aguacate en laminas", "Queso costeno rallado"]
ING_NO_VEGET = ["Chorizo santarrosano", "Chicharron crocante", "Carne desmechada", "Pollo apanado con hogao"]

def descripcion_pizza(es_vegetariana: bool, opcion: int) -> str:
    """
    Devuelve la descripcion final de la pizza segun el tipo y el ingrediente elegido.
    """
    menu = ING_VEGET if es_vegetariana else ING_NO_VEGET
    if opcion < 1 or opcion > len(menu):
        return "Error: opcion de ingrediente invalida."
    
    extra = menu[opcion - 1]
    tipo = "vegetariana" if es_vegetariana else "no vegetariana"
    ingredientes = BASE + [extra]
    return f"Pizza {tipo} con " + ", ".join(ingredientes)


if __name__ == "__main__":
    try:
        respuesta = input("Desea una pizza vegetariana? (s/n): ").strip().lower()
        
        if respuesta not in ("s", "n"):
            print("Error: respuesta invalida, use 's' o 'n'.")
        else:
            es_vegetariana = respuesta == "s"
            menu = ING_VEGET if es_vegetariana else ING_NO_VEGET
            
            print("Elige un ingrediente adicional:")
            for i, ing in enumerate(menu, start=1):
                print(f"{i}. {ing}")
            
            opcion = int(input("Numero de ingrediente: "))
            print(descripcion_pizza(es_vegetariana, opcion))
    except ValueError:
        print("Error: debes ingresar un numero valido para el ingrediente.")
