import os

def load_dictionary(file_path):
    dictionary = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            key, value = line.strip().split(',')
            dictionary[key.strip()] = value.strip()
    return dictionary

def save_dictionary(dictionary, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for key, value in dictionary.items():
            file.write(f"{key},{value}\n")

def create_dictionary_file(file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        pass

def translate_word(word, dictionary):
    return dictionary.get(word, "Translation not found")

def add_translation(word, translation, dictionary, file_path):
    dictionary[word] = translation
    save_dictionary(dictionary, file_path)
    print("Translation added successfully.")

def return_to_menu():
    while True:
        choice = input("Do you want to translate another word? (yes/no): ")
        if choice.lower() == 'yes':
            return True
        elif choice.lower() == 'no':
            print("Goodbye!")
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    file_path = "dictionary.txt"
    if not os.path.isfile(file_path):
        create_dictionary_file(file_path)

    dictionary = load_dictionary(file_path)

    print("Welcome to the Translator App!")
    print("Available language pairs:")
    print("1. English-Georgian")
    print("2. Georgian-English")
    print("3. Russian-Georgian")
    print("4. Georgian-Russian")

    while True:
        choice = input("Please choose a language pair (1/2/3/4): ")
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue
        else:
            break

    language_pairs = {
        '1': ('English', 'Georgian'),
        '2': ('Georgian', 'English'),
        '3': ('Russian', 'Georgian'),
        '4': ('Georgian', 'Russian')
    }

    from_lang, to_lang = language_pairs[choice]
    print(f"You chose {from_lang}-{to_lang} translation.")

    while True:
        word = input(f"Enter a word or phrase in {from_lang}: ")
        if word.lower() == 'exit':
            print("Goodbye!")
            break

        translation = translate_word(word, dictionary)
        if translation != "Translation not found":
            print(f"Translation: {translation}")
        else:
            while True:
                add_new = input("Translation not found. Do you want to add it to the dictionary? (yes/no): ")
                if add_new.lower() == 'yes':
                    new_translation = input(f"Enter the translation of '{word}' in {to_lang}: ")
                    add_translation(word, new_translation, dictionary, file_path)
                    if return_to_menu():
                        break
                    else:
                        return
                elif add_new.lower() == 'no':
                    if return_to_menu():
                        break
                    else:
                        return
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
                    continue

if __name__ == "__main__":
    main()
