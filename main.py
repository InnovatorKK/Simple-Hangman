import sys
import random

def game(word_2_guess: str, limit: int, word: str):
    if word_2_guess == word:
        sys.exit(f"YOU WIN\nword: {word}, tries left: {limit+1}")
        
    if limit >= 0:
        guess = str(input("guess a letter: "))
        #FIX ME
        try:
            exception = "1" + guess
        except:
            print("Error type a letter from a to z")
            game(word_2_guess, limit, word)
        #FIX ME
        if len(guess) != 1:
            if word_2_guess == guess:
                sys.exit(f"YOU WIN\nword: {word_2_guess}, trials: {limit}")
            else:
                print("Wrong word try again")        
                limit += 1
                print("\n")
                print(word, limit)
                print("\n")
                game(word_2_guess, limit, word)   
        else:
            if guess in word_2_guess:
                index = []
                counter = 0
                for i in word_2_guess:
                    if i == guess:
                        index.append(counter)
                    counter += 1
                for i in index:
                    temp = list(word)
                    temp[i] = guess
                    word = "".join(temp)
                
            else:
                print(f"No {guess} in this word")
        limit += 1
        print("\n")
        print(word, limit)
        print("\n")
        game(word_2_guess, limit, word)
    else:
        print(f"game over.\ncurrent word: {word}")
        print(f"answer: {word_2_guess}")


with open("words.txt", "r") as f:
    words = f.readlines()

word_data = words[random.randint(0, len(words))]
word_data = word_data.replace("\n", "")
word = "_" * len(word_data)
print("word loading...\nloaded\n word to guess: " + word + "\n")
game(word_data, 0, word)
