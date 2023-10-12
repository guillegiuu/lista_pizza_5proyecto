"""
Proyecto 5: 

Trabajas en Len's Slice, una pizzería nueva en el barrio. Vas a utilizar tus conocimientos de listas de Python para organizar algunos de tus datos de ventas.

"""

#Len's Slice: 5 Proyecto

#Codigo Aqui:

#Step 1 Lista aderezos
aderezos = ["pepperoni", "piña", "queso", "salchicha", "aceitunas", "anchoas", "champiñones"]

#Step 2 Lista precios
precios = [2, 6, 1, 3, 2, 7, 2]

#Step 3 metodo .count()
num_dos_rebanadas_dolar = precios.count(2)
#print(num_dos_rebanadas_dolar)

#Step 4 funcion len()
num_pizzas = len(aderezos)
#print(num_pizzas)

#Step 5 concatenacion 
print("¡Vendemos " + str(num_pizzas) + " diferentes tipos de pizza!")

#Step 6 Lista Bidimensional
pizza_y_precios = [[2,"mozarella"],[6,"jamon y morrones"], [1,"fugazzeta"], [3,"roquefort"], [2,"margarita"], [7,"cuatro quesos"], [2,"capresse"]]

#print(pizza_y_precios)

#Funcion Sorted y metodo Slicing
#===============================

#Step 7 metodo sort o funcion sorted
pizza_y_precios.sort()
#print(pizza_y_precios) se ordena por el precio.

#Step 8 metodo slicing
pizza_barata = pizza_y_precios[0]
#print(pizza_barata)

#Step 9 metodo slicing
pizza_cara = pizza_y_precios[-1]
#print(pizza_cara)

#Step 10 metodo .pop()
pizza_y_precios.pop()
#print(pizza_y_precios) Borro el ultimo elemento


#Step 11 metodo .insert()
pizza_y_precios.insert(2, [2.5, "pizza comun"])
#print(pizza_y_precios)


#Step 12 metodo slicing cortar
tres_pizzas_baratas = pizza_y_precios[:3]

#Step 13 
print(tres_pizzas_baratas)

