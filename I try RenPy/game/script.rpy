init python:
    import random

define m = Character('Me', color="#FF00FF")

label random_event:
    $ roll = random.randint(0,2)
    if roll == 0:
        "Nothing happened"
    elif roll == 1:
        "Option 1 happened"
    elif roll == 2:
        "Option 2 happened"
    return

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room


    # These display lines of dialogue.

    m "This is me in hell"
    m "Let's see if this works"
    call random_event
    "Random event over"

    # This ends the game.

    return
