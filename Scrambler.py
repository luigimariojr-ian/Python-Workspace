import random
score = 0
rounds = 1
numofhints = 0
file = open("Words.txt", "r")
allwords = file.read()
words = allwords.split(",")
for i in range(0, 5):
    word = random.choice(words)
    word = word.strip()
    wordlist = list(word)
    random.shuffle(wordlist)
    shuffeledword = "".join(wordlist)
    print("It is Round " + str(rounds))
    print("Can you un-scramble this word? " + shuffeledword)

    hint = input("Do you need a hint? (y/n) ")
    if hint == "y":
        print("The second letter is = " + word[1] + ". And you know the first letter.")
        numofhints = numofhints + 1

    guess = input("What do you think the word is? ")
    if guess == word:
        print("Correct!")
        score = score + 1
    else:
        print("Incorrect :(")
        print("The correct word was: " + word)
    
    rounds = rounds + 1
    print("\n")

print("Your score is: " + str(score) + "/5")
print("The amount of hints you used is: " + str(numofhints) + "/5")