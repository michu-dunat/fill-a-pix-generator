# Fill-a-pix Generator

Python program that allows you to generate a fill-a-pix puzzle and allows you to check if the indicated square is colored. 

## Introduction

Briefly, a fill-a-pix puzzle is defined as a rectangle consisting of `n x m` square grids. The selected square can be labeled with integer values. These are prompts. 
The integer value specifies the number of neighboring squares, including the labeled box, that are colored (we assume that a square has 8 neighbors). 
When solving a puzzle, the goal is to find all the colored squares based on the hints. Pointing to an uncolored square is considered an error.

## Python libraries:

- numpy,
- Pillow.

## Running the application

First, install required libraries:

```
python -m pip install -r requirements.txt
```

Then inside console:

```
python main.py
```

## Implementation

`Game` class contains:

- a method that, given an input (a picture stored on disk), will generate a rectangle containing the hint labels,
- a method that checks if the attempt to indicate a colored grid is correct.

The application also contains a demonstration of the above mentioned methods - the application runs in console mode.
