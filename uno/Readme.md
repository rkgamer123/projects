# UNO Card Game (Java)

A console-based implementation of the classic UNO card game, built in Java using object-oriented programming.
This project was developed as part of a high school computer science course to practice modeling real-world systems using classes and collections.

## Demo

Example gameplay flow:
- Deck is shuffled
- Players receive cards
- Each turn checks playable cards
- Matching rules enforced by color or number
- Game continues until a player runs out of cards

## Features
- Deck creation and shuffle logic
- Card matching rules (color and number)
- Player hand management
- Turn-based gameplay
- Console input and output
- Clean object-oriented design

## Project Structure
UNOCard.java     → Represents a single card  
UNODeck.java     → Deck creation, shuffle, draw logic  
UNOHand.java     → Player hand and playable cards  
UNOGame.java     → Game rules and turn engine  
UNORunner.java   → Main program entry point  

## How to Run

Compile:

    javac *.java
Run:

    java UNORunner
    
## Concepts Demonstrated

- Object-Oriented Programming
- Collections (ArrayList)
-  Game logic and rule implementation
- Modular program structure
- User input handling

## Author
Rishi Kidave - Student Developer 

## Future Improvements

- Add special UNO cards (Skip, Reverse, Wild)
- Add multiple players
- Add computer players (AI logic)
- Build a graphical UI version

