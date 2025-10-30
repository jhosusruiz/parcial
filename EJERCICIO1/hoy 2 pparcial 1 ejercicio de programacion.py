# 1 ejercicio codigo para invertir un array a string

print("=== invierte tu array ===\n")

# pedirte cuentos elementos tendra el array
cantidad = int(input("¿cuantos elementos quieres que sean? "))

# crea tu lista vacia para que guarde tus elementos
array_principal = []

# pedir tus elementos de uno en uno
print("escribe tus elementos:")
for i in range(cantidad):
    elemento = input(f"Elemento {i+1}: ")
    array_principal.append(elemento)

# codigo para invertir el array
def invertir(lista):
    array_invertido = []
    # checkeo de lista desde el principio hasta el final
    for i in range(len(lista) - 1, -1, -1):
        array_invertido.append(lista[i])
    return array_invertido

# invertidor de array
array_invertido = invertir(array_principal)

# mostrador de resultados
print("\nArray original:", array_principal)
print("Array invertido:", array_invertido)

# inpedir que se cierre la pestaña
input("\nPresiona ENTER para salir...")