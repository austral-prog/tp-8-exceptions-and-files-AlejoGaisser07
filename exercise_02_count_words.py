# Ejercicio 2 - Contar palabras en un archivo
import os

def count_words(filename):
    """
    Lee un archivo y retorna un diccionario palabra -> cantidad.

    Reglas:
    - Las palabras se separan por espacios en blanco (cualquier tipo:
      espacios, tabs, saltos de línea). El método .split() sin argumentos
      ya maneja eso.
    - El conteo es case-insensitive: "Hola" y "hola" cuentan como la
      misma palabra. En el diccionario final las claves están en
      minúsculas.
    - Si el archivo está vacío, retornar {}.
    - Si el archivo no existe, propagar FileNotFoundError.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        dict[str, int] - cada palabra (en minúscula) con su frecuencia.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene: "Hola mundo hola\nmundo python\n"
        count_words("texto.txt") -> {"hola": 2, "mundo": 2, "python": 1}
    """
    with open(filename, 'r') as arch:
        if not os.path.exists(filename):
            raise FileNotFoundError
        dictionary = {}
        for line in arch:
            line = line.lower().split()
            for words in line:
                if words in dictionary:
                    dictionary[words] += 1
                else:
                    dictionary[words] = 1
    return dictionary
