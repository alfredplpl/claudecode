# Number Guessing Game

A simple Python implementation of the classic number guessing game where the computer picks a random number and the player tries to guess it.

## Game Rules

- The computer selects a random number between 1 and 100
- You have 7 attempts to guess the correct number
- After each guess, you'll receive a hint:
  - "Too low!" if your guess is below the target
  - "Too high!" if your guess is above the target
  - "Congratulations!" if you guess correctly
- Input validation ensures only valid numbers between 1-100 are accepted

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## How to Run

### Method 1: Direct execution
```bash
python3 game.py
```

### Method 2: Make executable and run
```bash
chmod +x game.py
./game.py
```

## Features

- Input validation with error handling
- Replay functionality - play multiple rounds
- Attempt counter with maximum limit
- Clear feedback and user-friendly interface
- Emoji feedback for win/loss states

## Example Gameplay

```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Attempt 1/7 - Enter your guess: 50
Too high! Try a lower number.

Attempt 2/7 - Enter your guess: 25
Too low! Try a higher number.

Attempt 3/7 - Enter your guess: 37
🎉 Congratulations! You guessed it in 3 attempts!

Would you like to play again? (y/n): 
```