import random
import hangmanStages
import randomWords
import warnings
warnings.filterwarnings('ignore')
words_list = randomWords.random_words
chosen_word = random.choice(words_list).lower()
print(chosen_word)
display = ['_' for _ in chosen_word]
lives = 6
game_over = False
while not game_over:
    guessed_letter = input('Guess a letter: ').lower()
    for idx, letter in enumerate(chosen_word):
        if letter == guessed_letter:
            display[idx] = letter
    print(display)
    print()
    if guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print('You lost!!')
    if '_' not in display:
        game_over = True
        print('You won!!')
    print(hangmanStages.stages[lives])


