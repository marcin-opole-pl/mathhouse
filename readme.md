
# Mathhouse

## Video Demo:  [Mathhouse](https://youtu.be/hJUcvj_EmGc)

### Description

___

#### Purpose of the project

The purpose of this program is to help master mathematical operations.

Given a goal (which is being dropped from right top corner of the screen), player have to use mathematical operations:

- adding,
- subtracting,
- multiplying,
- dividing

to achieve the goal.

Game is numpad operated. '+' for adding, '-' for subtracting, '*' for multiplying and '/' for dividing.
There is also one more special key: 'Enter' (numpad enter). 'Enter' removes closest box to the machine from conveyor belt, but there is price to be paid. You loose one chance.
Chances are also lost when division creates reminder or you are trying to divide by '0'.

When chances are gone, game is over.
___

#### Program structure

1. GUI

    Pygame library has been used for GUI creation.

2. OOP approach

    Object-oriented approach led to creation of four classes:

    - Box
    - FreeLocation
    - Calculator
    - Conveyor

3. Program overview

    Box class is responsible for boxes' behavior and value of each box.
    Every time box is created, it takes random value from range 0-9. Box is only created when FreeLocation list is not empty. By creation of box, FreeLocation list is appended. To enable proper existence of each Box object, class takes as attributes object of FreeLocation class and object of Calculator class.

    FreeLocation class contains list of all available locations, and controls it. It exists independently.

    Calculator class is the brain this program. It does all the math, creates target values, compares actual value with target, measures score and control available chances. When box reaches its final location (next to the machine), and adequate key is pressed, the Calculator object does the math. Then it compares it to target value, if both values are equal, score is raised, and new sequence of boxes is being released. Calculator object is also responsible for catching division errors ( division by zero, and division with reminder). Finally it keep track of chances.

    Conveyor class only controls behavior of the conveyor. It is the simplest class.

### Final word

This is my second project of this scale. I am fully aware of missing functionality, that would improve user's experience. Project will evolve...
