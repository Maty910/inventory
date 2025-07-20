def pedir_texto_no_vacio(mensaje: str) -> str:
    """Solicita un texto no vacío."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("El texto no puede estar vacío.")


def pedir_entero(mensaje: str, minimo: int = None) -> int:
    """Solicita un número entero, con opción de mínimo."""
    while True:
        entrada = input(mensaje)
        try:
            numero = int(entrada)
            if minimo is not None and numero < minimo:
                print(f"Debe ser mayor o igual a {minimo}")
                continue
            return numero
        except ValueError:
            print("Debe ingresar un número entero válido.")


def pedir_opcion(mensaje: str, opciones_validas: list[str]) -> str:
    """Solicita una opción dentro de una lista de valores válidos."""
    opciones_formateadas = ", ".join(opciones_validas)
    while True:
        entrada = input(f"{mensaje} ({opciones_formateadas}): ").strip().lower()
        if entrada in opciones_validas:
            return entrada
        print(f"Opción inválida. Debe ser una de: {opciones_formateadas}")

def pedir_nombre_unico(prompt, productos):
    while True:
        nombre = input(prompt).strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
        elif any(p.lower() == nombre.lower() for p in productos):  # <-- acá, p es string
            print("Ese nombre ya está en uso. Ingresá uno distinto.")
        else:
            return nombre

def pedir_numero_positivo(mensaje: str) -> int:
    """Solicita un número entero mayor o igual a cero."""
    return pedir_entero(mensaje, minimo=0)