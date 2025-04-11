def factorialCalculate(number: int):
    factorial= 1
    for i in range(number):
        factorial = (i+1) * factorial
    return factorial

def printResult(number: int, result: int):
    print("The factorial of ", number, " is ", result)
    

def execute():
    number= int(input("Enter a number: "))
    result= factorialCalculate(number)
    printResult(number,result)



