import random
from words import list_of_words

def get_word():
    word = random.choice(list_of_words)
    return word.upper()

def play(word):
    word_tobe_completed = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Welcome to the Hangman Game!")
    print(display_hangman(tries))
    print(word_tobe_completed)
    print("\n\n")

    while not guessed and (tries > 0):
        guess = input("Please guess a letter or word : ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter " + guess)
            elif guess not in word:
                print(guess + " is not in the word!")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job! " + guess + " is in the word")
                guessed_letters.append(guess)
                word_as_list = list(word_tobe_completed)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_tobe_completed = "".join(word_as_list)    
                if "_" not in word_tobe_completed:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word " + guess)
            elif guess != word:
                print(guess + " is not the word!")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_tobe_completed = word
        else:
            print("Not a valid guess")
        
        print(display_hangman(tries))
        print(word_tobe_completed)
        print("\n\n")

    if guessed:
        print("Congrats, you guessed the word! You Win!")
    else:
        print("Oh no, you ran out of tries. The word was " + word)


def display_hangman(tries):
    stages = [  # final state: head, body, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, body, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, body, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, body, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and body
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Want to play again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()