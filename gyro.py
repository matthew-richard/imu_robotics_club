#!/usr/bin/python
# Simple demo of of the L3G4200D gyroscope library.  Will print the X, Y, Z
# axis acceleration values every half second.
# Author: Matt Richard 
# License: Public Domain 
import time

# Import the L3G4200D module.
import JHURC_L3G4200D


# Create an L3G4200D instance.
gyro = JHURC_L3G4200D.L3G4200D()

print('Printing X, Y, Z axis values, press Ctrl-C to quit...')
while True:
    # Read the X, Y, Z axis acceleration values and print them.
    x, y, z = gyro.read()
    print('X={0}, Y={1}, Z={2}'.format(x, y, z))
    # Wait half a second and repeat.
    time.sleep(0.5)
