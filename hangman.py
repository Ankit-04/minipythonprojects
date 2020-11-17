import random

word_list = ["python", "javascript", "typescript", "rubyonrails", "react", "angular"]
letters_guessed = []
word = random.choice(word_list)
lives = 6
underscores = []
playing = True

for x in range(len(word)):
    underscores.append("-")
        
while playing == True:
    print("".join(underscores))
    print("lives:",lives)  
    letter_guessed = str(input("Guess a letter: "))
    if letter_guessed in letters_guessed:
        print("letter already guessed")
    elif letter_guessed in word:
       for x in range(len(word)):
           if letter_guessed == word[x]:
               underscores[x] = letter_guessed
    else:
        letters_guessed.append(letter_guessed)
        lives -= 1
    
    if "-" not in underscores:
        print("you win")
        playing = False
    elif lives == 0:
        print("you lose")  
        playing = False 




