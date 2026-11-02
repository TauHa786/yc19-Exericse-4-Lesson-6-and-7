import math_operations

def run_calculator():
    print("--- Simple Module-Based Calculator ---")
    print("Available choices: add, subtract, multiply, divide, quit")
    
    while True:
        choice = input("\nEnter operation choice: ").strip().lower()
        
        if choice == 'quit':
            print("Exiting calculator. Goodbye!")
            break
            
        if choice not in ['add', 'subtract', 'multiply', 'divide']:
            print("Invalid choice. Please choose a valid operation or 'quit'.")
            continue
            
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
            
        if choice == 'add':
            result = math_operations.add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
            
        elif choice == 'subtract':
            result = math_operations.subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
            
        elif choice == 'multiply':
            result = math_operations.multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
            
        elif choice == 'divide':
            result = math_operations.divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")

if __name__ == "__main__":
    run_calculator()

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
    
