def sort (List):
    return sorted(List)


def printResult(sortedList: list):
    print("Numbers sorted: ")
    print(sortedList)
    print()

def execute():
    
    userNumbres = input("Insert number separated by ',': ")
    numberList =[int(num.strip()) for num in userNumbres.split(",")]

    sortedList = sort(numberList)

    printResult(sortedList)