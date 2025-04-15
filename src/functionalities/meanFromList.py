from statistics import mean

def execute():
    numLen = input("Ingrese tamaño de la lista: ")
    numLen = int(numLen)
    
    numeros = []
    
    while numLen > 0:
        new = input("Ingrese un numero: ")
        numeros.append(int(new))
        numLen -= 1
    
    promedio = mean(numeros)
    print("Promedio:", promedio)
