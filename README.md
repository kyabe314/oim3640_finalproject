*Names: Angeline Cho, K Yabe*

# **Naval War Simulation Game** 

>“If you know the enemy and know yourself, you need not fear the result of a hundred battles. If you know yourself but not the enemy, for every victory gained you will also suffer a defeat. If you know neither the enemy nor yourself, you will succumb in every battle.” --- Sun Tzu

## 1. Introduction

Have you ever wondered what it is like to demolish your long-time enemy on a naval battle? Have you ever wanted to reveal your secret strength as a mediaval marine strategist? Well, this game is for you! Summon your crews, procure your ammunitions, and go on an adventure of naval war simulation with Captain Angelina and K!

## 2. Description

For this final project of OIM3640, we are going to create a battle ship game for 2 players. On a coordinate system of n x n matrix, players are going to be able place customazed number of ships on the coordinate. There are various sizes for ships, 3 coordinate size being the largest and all the way to 1 coordinate size being the smallest ship. The number of ships which players can place is disproportionate to the size of ships (i.e. 3 sized ships will have the smallest number of ships and 1 sized ships will have the highest number of ships.) The players will take turn to bombard one coordinate per turn, and players will get an extra turn if they manage to hit a coordinate in which a part of a ship lies. 

## 3. Technical Architecture

We are planning to create the game through employing multiple functions with python. We will be writing functions to create the board, which is an n x n matrices (we haven’t exactly decided on the size yet). We will also create a function that can help us put random ships of random size on random locations of the board. We may need to create multiple functions to assist it, for example get_column and get_row. We will also make a file to play and run games, with functions that allow us to have user input on guessing the coordinates of the ships. If the ship is hit, then the ship on the coordinate will be replaced with an “x”, displaying a message showing the user that the ship is hit. While if the player missed, then it will simply present a message telling the player that they missed the ship. If the ships are all hit, then the player wins, if the ships are not hit within the number of given moves, then the player loses the game. There will be other smaller functions to assist the game.

## How to run the code?

To play the game of Battleship, simply run battleship1.py and an external screen will pop up. You will also need to install pygame before hand with:
    pip install pygame
or see [here](https://www.pygame.org/wiki/GettingStarted).
