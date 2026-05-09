# Ejercicio 6 - Estadísticas de notas por estudiante


def grades_stats(filename):
    """
    Lee un archivo donde cada línea tiene el formato:

        estudiante:nota1,nota2,nota3,...

    y retorna un diccionario donde la clave es el nombre del estudiante y
    el valor es una TUPLA (promedio, maximo, minimo) con los tres valores
    como float.

    Reglas:
    - El promedio se calcula con todas las notas de la línea.
    - Las líneas vacías se ignoran.
    - Se garantiza que todas las notas son números válidos.
    - Si el archivo no existe, propagar FileNotFoundError.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        dict[str, tuple[float, float, float]] - estadísticas por estudiante.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene: "Ana:8,9,7\nBeto:5,5,10\nCami:10\n"
        grades_stats("notas.txt") -> {
            "Ana": (8.0, 9.0, 7.0),
            "Beto": (6.666666666666667, 10.0, 5.0),
            "Cami": (10.0, 10.0, 10.0),
        }
    """
    with open(filename, 'r') as file:
        result = {} # asigno el diccionario
        for line in file:
            if line != "" and line != '\n': # chequeo que la linea no este vacia
                where = line.find(':') # busco donde esta el :
                grades = line[where+1:] # las notas estan despues del :
                keys = line[:where] # las keyts estan antes del :
                grades = grades[:-1].split(',') # hago que me separe las notas menos el \n del final
                grades_converted = [] # nueva lista
                for grade in grades:
                    grade = float(grade) # convierto cada nota a float 
                    grades_converted.append(grade) # la meto en la lista vacia
                avg = (sum(grades_converted) / len(grades_converted)) # hago las cuentas
                max_note = (max(grades_converted))
                min_note = (min(grades_converted))
                result[keys] = (avg, max_note, min_note) # lo meto en el diccionario
                # vuelve arriba con la segunda linea y asi
        return result
    
