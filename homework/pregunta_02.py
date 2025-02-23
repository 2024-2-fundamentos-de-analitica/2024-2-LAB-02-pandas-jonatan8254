"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd

def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    # Cargar el archivo tbl0.tsv ubicado en files/input/
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    # Retornar la cantidad de columnas del DataFrame
    return df.shape[1]

# Ejemplo de uso:
if __name__ == "__main__":
    print(pregunta_02())  # Se espera que imprima 4
