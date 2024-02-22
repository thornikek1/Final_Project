import random
import math

def calculate_max_attempts(lower_bound, upper_bound, difficulty):
  range_size = upper_bound - lower_bound + 1
  total_attempts = int(math.ceil(math.log2(range_size)))  # Calculate minimum attempts for any difficulty

  if difficulty == "easy":
    return total_attempts + 2
  elif difficulty == "medium":
    return total_attempts + 1
  elif difficulty == "hard":
    return total_attempts
  else:
    raise ValueError("Invalid difficulty level. Please choose 'easy', 'medium', or 'hard'.")

def main():
  # Get and validate user input for range
  while True:
    try:
      lower_bound = int(input("Enter the lower bound of the range (inclusive): "))
      upper_bound = int(input("Enter the upper bound of the range (inclusive): "))
      if lower_bound >= upper_bound:
        raise ValueError("Lower bound must be less than upper bound.")
      break
    except ValueError as e:
      print("Invalid input. Please enter valid integers.")

  # Validate difficulty
  valid_difficulties = ["easy", "medium", "hard"]
  while True:
    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
    if difficulty in valid_difficulties:
      break
    else:
      print("Invalid difficulty. Please choose from easy, medium, or hard.")

  # Calculate maximum attempts
  max_attempts = calculate_max_attempts(lower_bound, upper_bound, difficulty)  

  # Generate random number with inclusive bounds
  secret_number = random.randint(lower_bound, upper_bound)

  # Start the game
  print(f"\nYou have {max_attempts} attempts to guess a number between {lower_bound} (inclusive) and {upper_bound} (inclusive).")
  attempts = 0
  guessed = False

  while attempts < max_attempts and not guessed:
    while True:
      try:
        guess = int(input("Enter your guess: "))
        if guess < lower_bound or guess > upper_bound:
          raise ValueError("Guess must be within the range.")
        break
      except ValueError as e:
        print("Invalid input. Please enter a number within the range.")

    attempts += 1

    if guess == secret_number:
      guessed = True
      print(f"\nCongratulations! You guessed the number in {attempts} attempts.")
    elif guess < secret_number:
      print("Your guess is too low. Try again.")
    else:
      print("Your guess is too high. Try again.")

  if not guessed:
    print(f"\nSorry, you ran out of attempts. The secret number was {secret_number}.")

if __name__ == "__main__":
  main()
