def get_float_input(prompt):
  """Gets a valid float input from the user."""
  while True:
    try:
      value = float(input(prompt))
      return value
    except ValueError:
      print("Invalid input. Please enter a number.")

def choose_operation():
  """Gets a valid operation character from the user."""
  valid_ops = "+-*/"
  while True:
    operation = input("Choose an operation (+, -, *, /): ")
    if operation in valid_ops:
      return operation
    else:
      print(f"Invalid operation! Please choose one of: {', '.join(valid_ops)}")

def perform_calculation(num1, operation, num2):
  """Performs the specified operation on two numbers, handling errors."""
  try:
    if operation == "+":
      return num1 + num2
    elif operation == "-":
      return num1 - num2
    elif operation == "*":
      return num1 * num2
    elif operation == "/":
      if num2 == 0:
        raise ZeroDivisionError
      else:
        return num1 / num2
    else:
      raise ValueError("Internal error: invalid operation")
  except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
  except ValueError as e:
    print(f"Invalid input: {e}")
    
def main():
  """Main function for the calculator application."""
  print("Welcome to the Simple Calculator!")

  while True:
    try:
      num1 = get_float_input("Enter the first number: ")
      operation = choose_operation()
      num2 = get_float_input("Enter the second number: ")

      result = perform_calculation(num1, operation, num2)
      print(f"{num1} {operation} {num2} = {result}")

      valid_choices = "y", "n"
      while True:
        choice = input("Perform another calculation? (y/n): ").lower()
        if choice in valid_choices:
          break
        else:
          print(f"Invalid choice. Please enter y or n.")

      if choice == "n":
        break

    except ValueError as e:
      print(f"Error: {e}")

if __name__ == "__main__":
  main()
