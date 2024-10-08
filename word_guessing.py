import random

# Introduction
print("="*40)
print("      WELCOME TO WORD GUESSING GAME      ")
print("="*40)

# Player Name Input
name = input("\nEnter your name: ")
print(f"\nWelcome, {name}! Let's begin the game.")
print("="*40)

# Word List
words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board']
random_word = random.choice(words)
turns = 10
guesses = ''

# Display Initial Game Info
print(f"\nA word has been selected! It has {len(random_word)} letters.")
print("_ " * len(random_word))
print(f"\nYou have {turns} guesses. Good luck!")
print("="*40)

# Game Loop
while turns > 0:
    failed = 0
    print("\nCurrent Guess: ", end=" ")
    
    # Display the word with blanks
    for char in random_word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    
    # Winning Condition
    if failed == 0:
        print("\n\nCongratulations! You won!")
        print("="*40)
        break
    
    # Player Input
    guess = input("\n\nGuess a letter: ").lower()
    guesses += guess
    
    # If guess is incorrect
    if guess not in random_word:
        turns -= 1
        print("\nWrong guess!")
        print(f"You have {turns} turns left.")
        
        if turns == 0:
            print("\nSorry, you've run out of guesses. You lose.")
            print(f"The word was: {random_word}")
            print("="*40)
    else:
        print("\nGood guess!")
