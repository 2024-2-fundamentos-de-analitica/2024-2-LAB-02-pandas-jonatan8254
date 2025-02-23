"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_05():
    """
    Calcule el valor máximo de `c2` por cada letra en la columna `c1` del
    archivo `tbl0.tsv`.

    Rta/
    c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: c2, dtype: int64
    """
    # Cargar el archivo tbl0.tsv ubicado en files/input/
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    
    # Agrupar los datos por la columna 'c1' y obtener el máximo valor de 'c2'
    maximos = df.groupby('c1')['c2'].max()
    
    return maximos

# Ejemplo de uso:
if __name__ == "__main__":
    print(pregunta_05())