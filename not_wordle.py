import random

list_of_words = ["apple", "worst", "least", "feast"]
word_to_guess = random.choice(list_of_words)

max_tries = 6
for guess_number in range(0,max_tries+1):
    
    not_valid_guess = True
    while not_valid_guess:
        guess = input(f"Please enter your {guess_number+1} guess:")
        guess = guess.strip()
        if len(guess) == len(word_to_guess):
            not_valid_guess = False
        else:
            print ("You guess was invalid")
            
    
    if guess == word_to_guess:
        print("Hooray you have guessed the word")
        break 
    else:
        feedback = ""
        for letter_index in range(0, len(word_to_guess)):

            if guess[letter_index] == word_to_guess[letter_index]:
                feedback = feedback + guess[letter_index]
            else:
                feedback = feedback + "_"
                
        print(f"Feedback: {feedback}")
    

    
