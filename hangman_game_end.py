import random
i = 0
end = False
word_list = ["ardvark", "baboon", "Camel"]
chosen_word = random.choice(word_list)
display = list()
letters_guessed = []
lives = 6
for letter in chosen_word:
    display.append("_")

while end == False:
    if display != list(chosen_word):
        guess = input("Please guess a letter:\t").lower()
        letters_guessed.append(guess)
        minus_life = True
        for letter in chosen_word:
            if letter == guess:
                display[i] = guess
                minus_life = False
            i += 1
        i = 0
        if minus_life:
            lives -= 1
            minus_life = False
        print(display)
        print(f"Letters guessed: \n{letters_guessed}")
        #print(chosen_word)
        print(f"lives: {lives}")
    else:
        print("you win!")
        end = True

    if lives <= 0:
        print("you lose.")
        end = True