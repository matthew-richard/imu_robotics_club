# The MIT License (MIT)
#
# Copyright (c) 2016 Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import struct

# Minimal constants carried over from Arduino library
L3G4200D_ADDRESS = 0x69
CTRL_REG1 =  0x20
CTRL_REG2 =  0x21
CTRL_REG3 =  0x22
CTRL_REG4 =  0x23
CTRL_REG5 =  0x24
L3G4200D_DATAX0 =  0x28
L3G4200D_DATAX1 =  0x29
L3G4200D_DATAY0 =  0x2A
L3G4200D_DATAY1 =  0x2B
L3G4200D_DATAZ0 =  0x2C
L3G4200D_DATAZ1 =  0x2D

class L3G4200D(object):
    """L3G4200D gyroscope."""

    def __init__(self, address=L3G4200D_ADDRESS, i2c=None, **kwargs):
        """Initialize using I2C
        """
        # Setup I2C interface for the device.
        if i2c is None:
            import Adafruit_GPIO.I2C as I2C
            i2c = I2C
        self._device = i2c.get_i2c_device(address, **kwargs)
        # Enable x, y, z and turn off power down:
        self._device.write8(CTRL_REG1, 0b00001111)
        
        self._device.write8(CTRL_REG2, 0b00000000)

        self._device.write8(CTRL_REG3, 0b00001000)

        scale = kwargs.get('scale', 2000)
        if scale == 250:
            self._device.write8(CTRL_REG4, 0b00000000)
        elif scale == 500:
            self._device.write8(CTRL_REG4, 0b00010000)
        else:
            self._device.write8(CTRL_REG4, 0b00110000)

        self._device.write8(CTRL_REG5, 0b00000000)
        
    def read(self):
        """Read the current value of the gyroscope and return it as a tuple
        of signed 16-bit X, Y, Z axis values.
        """
        raw = self._device.readList(L3G4200D_DATAX0, 6)
        return struct.unpack('<hhh', raw)
