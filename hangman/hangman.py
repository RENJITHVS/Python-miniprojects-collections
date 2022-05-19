import random
import string
from words import words


def get_valid_words(words):
    word = random.choice(words)
    #eliminate words with spaces and "-"
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_words(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    
    while len(word_letters)> 0 and lives > 0:

        print("you have used these letters: ", " ".join(used_letters))

        word_list =[ letter if letter in used_letters else '-' for letter in word]
        print("current Words: ", " ".join(word_list))

        user_input= input("Guess the letters \t").upper()
        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                lives-=1
                print("letter not in words")

        elif user_input in used_letters:
            print("You have already used this character , Please try again")

        else:
            print("invalid character")

    if lives == 0:
        print(f"you died, our word is {word}")
    else:
        print(f"Hurray!!, you guessed the {word} correctly")




if __name__ == "__main__":
    hangman()