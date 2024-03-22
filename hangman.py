import random

word_list=["apple","beautiful","potato"]
lives=6
chosen_word=random.choice(word_list)

print(chosen_word)

display=[]

for i in range(len(chosen_word)):
    display += '_'

print(display)

game_over=False

while not game_over:

    guessed_letter=input("guess a letter: ").lower()

    for positon in range(len(chosen_word)):

        letter = chosen_word[positon]

        if letter==guessed_letter:
            display[positon]= guessed_letter

    print(display)

    if guessed_letter not in chosen_word:
        lives -=1
        if lives == 0:
            game_over = True
            print("You loose!!")

    if '_' not in display:
        game_over=True
        print("You win!!")