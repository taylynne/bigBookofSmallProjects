# Project 15 in the book by Al Sweigart
# Deep Cave 'animation' 
"""Deep Cave, by Al Sweigart recoded by Taylynne
An animation of a deep cave that goes on forever into the earth.
(At least until it is stopped)"""

import random, sys, time

# Set up the constants
WIDTH = 40 
PAUSE_AMOUNT = 0.05

print("Deep Cave, by Al Sweigart recoded by Taylynne")
print("Press ctrl+C to stop")
time.sleep(2)

leftWidth = 20
gapWidth = 10

while True:
    # Display the tunnel segment:
    rightWidth = WIDTH - gapWidth -leftWidth
    print(('#' * leftWidth) + ("." * gapWidth) + ("#" * rightWidth))

    # Check for ctrl+C press during the brief pause
    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit() # Ends program with ctrl+C

    # Adjust the left side
    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and leftWidth > 1:
        leftWidth = leftWidth - 1 # decreases left side width 
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
        leftWidth = leftWidth + 1 # Increases the width
    else:
        pass # do nada

    # Adjust the gap width
    # Commenting this out for the first run
    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and gapWidth > 1:
        gapWidth = gapWidth - 1
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
        gapWidth = gapWidth + 1
    else:
        pass
