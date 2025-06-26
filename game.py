#!/usr/bin/env python3
"""
Simple Number Guessing Game
The computer picks a random number between 1 and 1000, and you try to guess it!
"""

import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 1000.")
    
    secret_number = random.randint(1, 1000)
    attempts = 0
    max_attempts = 7
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            
            if guess < 1 or guess > 1000:
                print("Please enter a number between 1 and 1000!")
                continue
            
            if guess == secret_number:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                return True
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
                
        except ValueError:
            print("Please enter a valid number!")
            
    print(f"\n😔 Game over! The number was {secret_number}.")
    return False

def main():
    while True:
        won = play_game()
        
        play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
        if play_again not in ['y', 'yes']:
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()