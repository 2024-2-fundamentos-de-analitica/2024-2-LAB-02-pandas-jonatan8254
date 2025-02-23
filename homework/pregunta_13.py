"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
    import pandas as pd
    # Cargar los datos de tbl0.tsv y tbl2.tsv
    df0 = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    df2 = pd.read_csv("files/input/tbl2.tsv", sep="\t")
    # Realizar el merge usando c0 como clave
    df_merge = pd.merge(df0, df2, on="c0")
    # Agrupar por c1 y sumar los valores de c5b
    resultado = df_merge.groupby("c1")["c5b"].sum()
    return resultado

if __name__ == "__main__":
    print(pregunta_13())
