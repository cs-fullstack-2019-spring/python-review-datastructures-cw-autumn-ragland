def main():
    prob1()
    # prob2()

# Create a function that has a loop that quits with q
# Allow the User to enter names until q is entered
# Add each name entered to a List
# When the User enters q print the list of names
# ADDITIONAL REQUIREMENTS:Your code should be able to process the quit command (q) the User enters regardless of case
def prob1():
    userInput = input("Enter a name!\n").lower()
    userList = []
    while userInput != "q":
        userList.append(userInput)
        userInput = input("Nice!\nEnter q to quit or keep entering names.\n").lower()
    print(userList)
# Prints a formatted list of names and ages.
# Prompt the User for which property they want to use to sort the list (e.g. AGE or NAME).
# Print the formatted list of names and ages sorted by the specified sort criteria.
# Continue prompting the User for the sort criteria and print a sorted list until the User enters q then exit.

# Your code should be able to process the sort criteria the User enters regardless of case
# Your code should be able to process the quit command (q) the User enters regardless of case
# If the User enters something other than q or a valid sort criteria (e.g. AGE or NAME)
# your code should display INVALID ENTRY. PLEASE TRY AGAIN and continue the process.
def prob2():
    dictionaryList = [
        {
            "name": "Kelvin",
            "age": 30
        },
        {
            "name": "Bob",
            "age": 50
        },
        {
            "name": "Alex",
            "age": 21
        }
    ]
    for values in dictionaryList:
        for name, age in values.items():
            print(f"{name}:{age}")


    userInput = ""
    while userInput != "q":
        userInput = input("Sort by age or name?: ").lower()

        if userInput != "q" and userInput != "age" and userInput != "name":
            print("INVALID")
            continue

        if userInput == "q":
            break

        def sortKey(eachElement):
            return eachElement[userInput]
        dictionaryList.sort(key=sortKey)

        for values in dictionaryList:
            for name, age in values.items():
                    print(f"{name}:{age}")









if __name__ == '__main__':
    main()