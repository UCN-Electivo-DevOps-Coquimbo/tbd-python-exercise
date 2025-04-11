def _processList(userList: str):
    return userList.split(",")

def _frecuencyList(userList: list):
    numberList = []
    frequencyList = []
    for i in userList:
        if i not in numberList:
            numberList.append(i)
            frequencyList.append(1)
        else:
            index = numberList.index(i)
            frequencyList[index] += 1
    return numberList, frequencyList

def execute():
    userList = input("Ingrese lista y separe valores por una coma: ")

    processList = _processList(userList)

    numberList, frequencyList = _frecuencyList(processList)
    print("Lista de números: ", numberList)
    print("Lista de frecuencias: ", frequencyList)