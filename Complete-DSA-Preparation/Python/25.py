def handheld_calculator():
    result = 0
    operator = None
    
    while True:
        try:
            user_input = input("Enter a number, operator (+,-,*,/), 'C' to clear, or 'Q' to quit: ")
            
            if user_input == 'C':
                result = 0
                operator = None
                print("Cleared.")
            elif user_input == 'Q':
                print(f"Final result: {result}")
                break
            elif user_input in '+-*/':
                operator = user_input
            else:
                number = float(user_input)
                if operator:
                    if operator == '+':
                        result += number
                    elif operator == '-':
                        result -= number
                    elif operator == '*':
                        result *= number
                    elif operator == '/':
                        result /= number
                else:
                    result = number
                print(f"Current result: {result}")
        except ValueError:
            print("Invalid input. Please enter a number or a valid operator.")

if __name__ == "__main__":
    handheld_calculator()
