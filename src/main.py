from functionalities import *

# Execute a functionality. Return True if the user select option 0
def executeFunction (option):
	if option == 1:
		meanFromList.execute()
	elif option == 2:
		findMaxValue.execute()
	elif option == 3:
		getFactorial.execute()
	elif option == 4:
		circle_area.execute()
	elif option == 5:
		isCousing.execute()
	elif option == 6:
		isPalindrome.execute()
	elif option == 7:
		sortFunction.execute()
	elif option == 8:
		print("TO BE IMPLEMENTED...")
	elif option == 9:
		getTextWords.execute()
	elif option == 0:
		return True
	return False


# MAIN CODE
def main():
	while True:

		menu.printMenu()
		userInput = int(input("Select an Option: "))

		if not menu.isValidOption(userInput):
			print("Invalid Option. Try Again!")
		else:
			terminated = executeFunction(userInput)

			if terminated:
				break

	print("Application Ended!")

if __name__ == "__main__":
	main()
