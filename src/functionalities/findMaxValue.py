
def printResult(maxValue : int):
    print(f"the max value is: {maxValue}")



def verifyInput(text : str):
    listText = text.split()
    
    for word in listText:
        try:
            float(word)
        except Exception:
            return False
    return True



def _processInput(text : str):
    listText = text.split()

    list = []
    for numberText in listText:
        list.append(float(numberText))
    return list



def execute():

    userInput = input("write numbers separated by space: ")

    if not(verifyInput(userInput)):
        print("error, only numbers in the input")
        return


    list = _processInput(userInput)
    printResult(max(list))
