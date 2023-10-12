try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    total = float(input("Enter total: "))
    
    percentage = str(value/total * 100)
    
    print("That is " + percentage + "%.")
except ValueError:
    print("You need to enter a number. Run the program again.")
