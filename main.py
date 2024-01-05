"""
Joseph Mulaparthi
Plate Stacking Application
Created for Dev10
Due: 2024/01/05 @ 23:59
"""


#create empty list of plates
plates = []


#add plates function
def add_plate():
    #loop to get desired input
    #find out how many plates to add
    numberofPlates = ""
    while not numberofPlates == "0":
        #prompt for user input
        numberofPlates = input("Enter the number of plates you would like to add: ")
        #determine whether input is valid
        if numberofPlates.isdigit():
            numberofPlates = int(numberofPlates)
            break
        else:
            print("You have entered an invalid value. Please try again.")
    #get plate sizes
    for plate in range(numberofPlates):
        #display which plate user is on
        print(f"Plate {plate + 1} of {numberofPlates}")
        #loop to get desired input
        plateSize = ""
        while not plateSize == "0":
            plateSize = input("Enter a plate size: ")
            #determine whether input is valid
            if plateSize.isdigit():
                plateSize = int(plateSize)
                #determine whether list is empty
                if len(plates) == 0:
                    plates.insert(0, plateSize)
                    break
                else:
                    #determine biggest possible stackable plate
                    biggestPossiblePlate = plates[0]
                    if plateSize > biggestPossiblePlate:
                        print(f"You cannot stack a plate of size {plateSize} on top of a plate of size {biggestPossiblePlate}")
                    else:
                        plates.insert(0, plateSize)
                        break
            else:
                print("You have entered an invalid value. Please try again.")


#print plates function
def print_plates():
    #determine if there are any plates to print
    if len(plates) > 0:
        #convert plate size to hashes to look pretty
        for plate in plates:
            #set limit on size of plate thats converted to hashes
            if (plate >= 20):
                print(f"{plate:^20}")
            else:
                print(("#" * plate).center(20))
    else:
        print("There are no stacked plates.")


#remove plates function
def remove_plates():
    #determine if there any plates to remove
    if len(plates) == 0:
        print("There are no stacked plates to remove.")
    else:
        #determine how many plates to remove
        numberOfPlates = ""
        #loop to get desired input
        while not numberOfPlates == "0":
            numberOfPlates = input("Enter the number of plates you want to remove from the stack: ")
            #determine whether input is valid
            if numberOfPlates.isdigit():
                numberOfPlates = int(numberOfPlates)
                break
            else:
                print("You have entered an invalid value. Please try again.")
        #determine if there are enough plates to remove
        if numberOfPlates > len(plates):
            print(f"You cannot remove {numberOfPlates} plates from a stack of only {len(plates)}!")
        else:
            for plate in range(numberOfPlates):
                plates.pop(0)
            #display confirmation message
            if numberOfPlates == 0:
                print("No plates were removed.")
            else:
                print("The plates were successfully removed!")


#menu function
def create_menu():
    #loop to get desired input
    menuChoice = ""
    while not menuChoice == "0":
        #create menu
        print("=" * 20)
        print("""
Welcome to the plate stacking application!
0. [Exit]
1. Add a plate
2. Print plates
3. Remove plates
              """)
        #retreive user input
        menuChoice = input("Select [0-3]: ")
        #match user input and call function
        match (menuChoice):
            case "0":
                print("\nThanks for trying this out! Goodbye! :)")
                print("=" * 20)
            case "1":
                print("Add a plate")
                print("=" * 20)
                add_plate()
            case "2":
                print("Print plates")
                #display preliminary information about size of stack
                if len(plates) > 0:
                    print(f"There are {len(plates)} plates in the stack:")
                print("=" * 20)
                print_plates()
            case "3":
                print("Remove plates")
                print("=" * 20)
                remove_plates()
            case _:
                print("You entered an invalid input. Please try again.")


#call menu function
create_menu()


"""
For any questions, comments, concerns, or feedback, please contact
Joseph Mulaparthi at: 
mulaparthijoe@yahoo.com

Thank you!
"""
