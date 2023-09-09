# random choose game

import random
import hangman_words

chosen_word= random.choice(hangman_words.word_list)



dispaly=[]

word_lenght=len(chosen_word)

for _ in range(word_lenght):
    dispaly += "_"
print(dispaly)  

end_of_game=False
lives=6

from hangman_art import logo,stages
print(logo)



while not end_of_game:

    guess= input("guess a letter").lower()


    if guess in dispaly:
        print(f"you have already guessed {guess} letter")

    for position in range(word_lenght):
        letter=chosen_word[position]
        if letter==guess:
            dispaly[position]=letter


    if guess not in chosen_word:

        print(f"you guesses {guess}, that not in the word.you losse a life")
        lives -=1
        if lives==0:
            end_of_game=True
            print("you loose")        
    
         

    print(dispaly)  

    if "_" not in dispaly:
        end_of_game=True
        print("you win.")


    print(stages[lives]) 


