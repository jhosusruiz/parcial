 # 1. Solicitar datos de entrada       
def es_camaleon(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numero = int(input("Ingrese un número: "))
if es_camaleon(numero):
    print(f"{numero} es un camaleon.")
else:
    print(f"{numero} no es un camaleon.")
def secuencia(n):
    secuencia = []
    a, b = 0, 1
    while a <= n:
        secuencia.append(a)
        a, b = b, a + b
    return secuencia

numero = int(input("Ingrese un número: "))
print("Secuencia de divisores por 3 ", numero, ":", secuencia(numero))