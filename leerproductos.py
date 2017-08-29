with open('compras.csv', 'r') as f:
	c = f.readlines()

# eliminando el caracter \n  (nueva línea o enter)
for i in range(len(c)):
	 c[i] = c[i].replace("\n","")

# separando nombres de precios (lista de listas)
prod = [p.split(",") for p in c]

# eliminando las listas sin contenido (vacías)
for i in range(len(prod)):
	if len(prod[i]) == 0: prod.pop(i)

# creando el diccionario
productos2 = {i[0]:float(i[1]) for i in prod}
