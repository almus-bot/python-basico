def resumen(productos):
    promedio =  sum(productos.values()) / len(productos)
    maximo = max(productos.values())
    return promedio, maximo     # devuelve dos valores en forma de tupla