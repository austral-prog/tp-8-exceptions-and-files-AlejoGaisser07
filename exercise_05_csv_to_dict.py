# Ejercicio 5 - CSV a lista de diccionarios

def csv_to_dict(filename):
    """
    Lee un archivo CSV con header "name,age,city" y retorna una lista de
    diccionarios, uno por fila.

    Reglas:
    - La primera línea es siempre el header.
    - Las claves del diccionario se toman del header.
    - El campo "age" se convierte a int. "name" y "city" quedan como str.
    - Se deben hacer strip a los valores para eliminar espacios sobrantes.
    - Si el archivo está vacío o solo tiene header, retornar [].
    - Si el archivo no existe, propagar FileNotFoundError.
    - No se permite usar el módulo csv.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        list[dict] - lista de diccionarios por fila del CSV.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene:
        # name,age,city
        # Alice,30,Buenos Aires
        # Bob,25,Rosario
        csv_to_dict("people.csv") -> [
            {"name": "Alice", "age": 30, "city": "Buenos Aires"},
            {"name": "Bob", "age": 25, "city": "Rosario"},
        ]
    """
    with open(filename, 'r') as file:
        answer = []
        counter = 0
        for line in file:
            line = line.strip()
            line = line.split('\n')
            for subline in line:
                subline = subline.split(',')
                if counter == 0:
                    key1 = subline[0]
                    key2 = subline[1]
                    key3 = subline[2]
                if counter != 0:
                    dicc = {key1: subline[0],
                            key2: int(subline[1]),
                            key3: subline[2]}
                    answer.append(dicc)
                counter += 1
        return answer
    
