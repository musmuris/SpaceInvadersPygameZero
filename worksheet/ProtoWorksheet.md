# Introduction

In this project you will recreate classic game of space invaders

_introduction to pygame zero_
_The following currently assumes students can create a .py file and start a command line_

# Step 1 - The player's ship
+ First create a game window in which we can draw. Make a python file `invaders.py` which contains the following code

    ```python
    WIDTH = 500
    HEIGHT = 500

    def draw():
        screen.clear()
    ```
    
    The `HEIGHT=500` and `WIDTH=500` at the start set the screen size, and then our `draw` function 
    gets called whenever the screen needs drawing. In this case we just clear it to the black background

+ Run this by typing `pgzrun invaders.py` on the command line. A black square window should appear. 
    Not very exciting we know - but we can soon change that.

+ Next we need to make an image for the player ship, using a paint package.
    Something like this (whch is about 50 pixels wide and 30 high):

    ![Player ship](ship.png)

+ To draw this on the screen we need to make what PygameZero calls an Actor and tell it what picture to use.
    We can then set the position. In our screen 250 is the middle and the bottom would be 499 
    (1 below 500 as the top starts at 0 - don't worry if that
    doesn't make sense - trust us for now). We want it a bit above that.
    PygameZero allows us to set where the middle bottom of our sprite easily to place it in the middle
    and bottom of our screen 

    Add the following _above_ the draw function

    ```python
    ship = Actor('ship')
    ship.midbottom = 250,490
    ```

    The update the `draw` function to look like this:

    ```python
    def draw():
        screen.clear()
        ship.draw()
    ```


