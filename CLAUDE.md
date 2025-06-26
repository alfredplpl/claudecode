# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Status

This repository contains a simple Python number guessing game.

## Development Setup

This is a Python project that requires Python 3.6 or higher. No additional dependencies are needed as it only uses the standard library.

## Common Commands

- **Run the game**: `python3 game.py`
- **Make executable**: `chmod +x game.py && ./game.py`

## Architecture

Simple single-file Python game with the following structure:

- `game.py` - Main game implementation containing:
  - `play_game()` - Core game logic for a single round
  - `main()` - Game loop with replay functionality
  - Input validation and user interaction handling