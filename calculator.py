def calculator():
    while True:
        # Options
        print(
            "Enter 1 to ADD Two Numbers:\n"\
            "Enter 2 to SUBTRACT Two Numbers:\n"\
            "Enter 3 to MULTIPLY Two Numbers:\n"\
            "Enter 4 to DIVIDE Two Numbers:\n"\
            "Enter q or Q to Exit")
        
        # Operation to be performed
        operation = input("Choose an operation: ")
        
        # Exit Condition for Calculator
        if operation == 'q' or operation == 'Q':
            print("Exiting the calculator. Goodbye!")
            break
        
        # Validate the input for operation
        if operation not in ['1', '2', '3', '4']:
            print("Enter a Valid Option!!!\n")
            continue
        
        # Take the numbers as input
        try:
            num_1 = float(input("Enter the First Number: "))
            num_2 = float(input("Enter the Second Number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.\n")
            continue
        
        print()
        
        # Perform the selected operation
        operation = int(operation)
        
        if operation == 1:
            result = num_1 + num_2
            print(f"{num_1} + {num_2} = {result}\n")
            
        elif operation == 2:
            result = num_1 - num_2
            print(f"{num_1} - {num_2} = {result}\n")
            
        elif operation == 3:
            result = num_1 * num_2
            print(f"{num_1} * {num_2} = {result}\n")
            
        elif operation == 4:
            # Division by Zero Error
            if num_2 == 0:
                print("ERROR: DIVISION BY ZERO!!!\n")
                continue
            result = num_1 / num_2
            print(f"{num_1} / {num_2} = {result}\n")
            
if __name__ == "__main__":
    calculator()
