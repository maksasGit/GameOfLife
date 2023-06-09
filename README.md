# Game of Life

This project implements the famous cellular automaton known as the "Game of Life" using the Python programming language and the Pygame library.

# Installation
First, make sure you have Python installed on your system. You can download it from the official website: https://www.python.org/downloads/

Next, install Pygame by running the following command in your terminal or command prompt:

**Copy code**

``` python
pip install pygame
```
# Usage

To run the Game of Life simulation, simply run the main.py file. You can do this by typing the following command in your terminal or command prompt:

**Copy code**

```python 
python main.py
```
# How it works

The Game of Life is a cellular automaton invented by John Conway in 1970. It consists of a two-dimensional grid of cells that can be either alive or dead. The state of each cell depends on the state of its eight neighbors, which can be thought of as being adjacent horizontally, vertically, or diagonally.

## The rules for updating the state of the cells are as follows:

+ Any live cell with fewer than two live neighbors dies, as if by underpopulation.
+ Any live cell with two or three live neighbors lives on to the next generation.
+ Any live cell with more than three live neighbors dies, as if by overpopulation.
+ Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/Gospers_glider_gun.gif" alt="animated" />
</p>
