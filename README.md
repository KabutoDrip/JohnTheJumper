# JohnTheJumper
A small hangman like game


---
## Getting Started
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and browse to the project's root folder. Start the program by running the following command.
```
python3 JohnTheJumper 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- JohnTheJumper       (source code for game)
    +-- word.py         (selects word and evaluates input)
    +-- terminal.py     (gets input and returns for use by word.py)
    +-- display.py      (displays a parachute state in pygame as well as the progress towards the right word in the terminal)
    +-- director.py     (directs the flow of the game by calling classes for gameplay loop)
  +-- main.py           (program entry point)
+-- README.md           (general info)
```

## Required Technologies
* Python 3.8.0

## Authors
*  Camden Miller
*  Mary Goff
*  Kosie Kameta
*  Jennifer Walton
