# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character('Me', color="#FF00FF")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room


    # These display lines of dialogue.

    m "This is me in hell"
    m "Let's see if this works"

    # This ends the game.

    return
