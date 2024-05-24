import random

print("WELCOME TO NEW HANGER GAME")
words = ["computers", "televisions", "laptops"]
sec_word = random.choice(words)
print("YOU ARE TO GUESS THE RIGHT ")
print("NOTE THAT YOU HAVE ONLY 5 GUESSES............HAHAHAHAHAHAHAHAH")

display_words =[]
for letter in sec_word:
    display_words += "_"
print(display_words)

num = 0
game_over = False

while not game_over:
    guess =input("Guess the letter ").lower()
    for position in range(len(sec_word)):
        letter = sec_word[position]
        if letter == guess:
            display_words[position] = letter
    if guess not in sec_word:
        num += 1
        guesses_left = 5 -num
        print(f"You have {guesses_left} guess keft")
        if num >= 5:
            print("YOU LOOSE........HAHAHAHAH TRY AGAIN NEXT TIME")
            game_over = True
    print(display_words)

    if "_" not in display_words:
        print("YOU WIN!!!!!")
        game_over = True