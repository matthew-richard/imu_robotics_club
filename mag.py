#!/usr/bin/python
# Simple demo of of the L3G4200D gyroscope library.  Will print the X, Y, Z
# axis acceleration values every half second.
# Author: Matt Richard 
# License: Public Domain 
import time

# Import the module.
import JHURC_HMC5883

# Create an L3G4200D instance.
mag = JHURC_HMC5883.HMC5883()

print('Printing X, Y, Z axis values, press Ctrl-C to quit...')
while True:
    # Read the X, Y, Z axis acceleration values and print them.
    x, y, z = mag.read()
    print('X={0}, Y={1}, Z={2}'.format(x, y, z))
    # Wait half a second and repeat.
    time.sleep(0.5)
