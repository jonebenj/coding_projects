
import urllib.request, re, random

print(("-" * len("WELCOME TO HANGMAN, WHERE YOU TRY TO FIND OUT WHAT WORD I AM THINKING OF") + "\n\n"),\
          "WELCOME TO HANGMAN, WHERE YOU TRY TO FIND OUT WHAT WORD I AM THINKING OF\n\n", \
          "-" * len("WELCOME TO HANGMAN, WHERE YOU TRY TO FIND OUT WHAT WORD I AM THINKING OF"))
def hangman():
    #download the words from a url and find the list items
    web_page = urllib.request.urlopen("http://www.manythings.org/vocabulary/lists/a/words.php?f=compound_words")
    contents = web_page.read().decode(errors="replace")
    web_page.close()

    contents = contents.split("<ul>")[1]
    #print(contents)

    words = re.findall('(?<=<li>).+?(?=</li>)',contents,re.DOTALL)
    #print(words)
    word = random.choice(words)
    #print(word)

    #after choosing a random word, go through each letter in the word
    #, and append it to the list in the form of ("_", letter)
    char_list = []
    blanks_list = []
    for char in word:
        char_list.append(char)
        blanks_list.append(["_", char])

    #print(blanks_list)

    count = 0
    #print(len(char_list))
    print("Current word:")
    print("_ " * len(word))
    print("Current guesses: 0")
    print("Remaining guesses:", len(word) + 5)
    guess_list = []

    #Contiuously loop through, asking the user to enter in either
    # a letter or a word, displaying information each time
    while count <= len(char_list) + 4:
        remaining = []
        while True:
            guess = input("Please guess a letter or guess the word: ")
            if guess.lower() not in guess_list:
                break
            print("You have already used that letter!")
        guess_list.append(guess)
        alpha = "abcdefghijklmnopqrstuvwxyz"

        #generates list of letters not guessed yet
        for letter in alpha:
            if letter not in guess_list:
                remaining.append(letter)
        #print(guess)
        #print(word)

        #break clause if user enters correct word
        if guess == word:
            count += 1
            print("You win! It took you", count, "guesses.")
            break
        
        count += 1

        #loop through blank list and switch the position of the letter
        #and the "_" if the guessed letter is the same as the letter
        #in the list
        for i in range(len(blanks_list)):
            #print(blanks_list[i])
            if blanks_list[i][1] == guess:
                #print("true")
                blanks_list[i][0], blanks_list[i][1] = blanks_list[i][1], blanks_list[i][0]

        #If all the positions have been switched, all_together
        #stays as True. If at least one of the letters in blanks_list
        #is in the 1 position, though, all_together = False
        all_together = True
        print("Current word:")
        for i in range(len(blanks_list)):
            print(blanks_list[i][0], end = " ")
            
            if blanks_list[i][0] == "_":
                all_together = False
        print()
        print("Current guesses:", count)
        print("Remaining guesses:", (len(char_list) + 5) - count)
        print("Letters/words guessed:", ", ".join(guess_list))
        print("Letters you haven't used yet:", remaining)

        #winning condition
        if all_together == True:
            print("You win! It took you", count, "guesses.")
            break
        print()
        
    #losing condition
    if count == len(char_list) + 5 and all_together != True:
        print("You lose!")
        print("The word was", word)

#condition that keeps running the program until the user doesn't
#want to play anymore
stop = "Yes"
while stop.upper() != "NO":
    hangman()
    while True:
        stop = input("Would you like to play again? (Type Yes or No): ")
        if stop.upper() in ["YES", "NO"]:
            break
        print("Please type 'YES' or 'NO")
    if stop.upper() == "NO":
        print("Thank you for playing!")


    
