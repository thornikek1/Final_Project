import random

def choose_word():
    word_list = ["apple", "banana", "orange", "strawberry", "grape", "pineapple"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 8

    print("Welcome to Hangman!")
    print("The word contains", len(word), "letters.")
    print(display_word(word, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
        else:
            print("Incorrect!")
            attempts -= 1
            print("Attempts left:", attempts)

        displayed = display_word(word, guessed_letters)
        print(displayed)

        if "_" not in displayed:
            print("Congratulations! You guessed the word:", word)
            break

    if "_" in displayed:
        print("Sorry, you ran out of attempts. The word was:", word)

if __name__ == "__main__":
    hangman()
