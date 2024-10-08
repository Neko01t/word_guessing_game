# Word Guessing Game

Welcome to the **Word Guessing Game**! This is a simple terminal-based game where players guess letters of a randomly chosen word within a limited number of attempts.

## How to Play

1. The game will randomly select a word from a predefined list.
2. You have 10 attempts to guess the correct word, one letter at a time.
3. For each correct guess, the letter will be revealed in the word.
4. For incorrect guesses, you will lose one turn.
5. The game ends when you either guess the word correctly or run out of turns.

## Game Flow

- The game starts by asking for the player's name.
- You will be shown the number of letters in the word as underscores (e.g., `_ _ _ _ _`).
- You can guess one letter at a time.
- After each guess, the game will display the updated word with the guessed letters revealed.
- If your guess is incorrect, you will be informed, and the number of remaining turns will be displayed.
- The game will continue until you either guess the entire word or lose all your turns.

## Example
```
======================================== 
WELCOME TO WORD GUESSING GAME
Enter your name: John

Enter your name: Om

Welcome, John! Let's begin the game.
A word has been selected! It has 7 letters.
```
## You have 10 guesses. Good luck!
Current Guess: _ _ _ _ _ _ _

Guess a letter: o

Good guess!

Current Guess: _ o _ _ _ o _

Guess a letter: x

Wrong guess! You have 9 turns left.


## Technologies Used

- **Python**: The game is written in Python using basic control flow, loops, and input/output handling.

## Installation

To run this game, make sure you have Python installed. You can download it from [Python's official website](https://www.python.org/).

### Steps to Run the Game

1. Clone or download the repository.
2. Navigate to the project directory in your terminal.
3. Run the game using the following command:
   ```bash
   python word_guessing_game.py
