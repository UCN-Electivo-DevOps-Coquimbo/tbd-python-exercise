# Verificar si es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # Solo hasta raíz cuadrada de n
        if n % i == 0:
            return False
    return True

def execute():
    num = int(input("Introduce un número: "))
    resultado = es_primo(num)
    if resultado:
        print(f"{num} es un número primo.")
    else:
        print(f"{num} no es un número primo.")

