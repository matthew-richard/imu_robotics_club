# The MIT License (MIT)
#
# Copyright (c) 2016 Adafruit Industries
# # Permission is hereby granted, free of charge, to any person obtaining a copy
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
HMC5883_ADDRESS = 0x1E
HMC5883_SAMPLERATE_CTL = 0x00
HMC5883_MODE_CTL = 0x02 
HMC5883_DATAX0 = 0x03 
HMC5883_DATAX1 = 0x04 
HMC5883_DATAY0 = 0x05 
HMC5883_DATAY1 = 0x06 
HMC5883_DATAZ0 = 0x07 
HMC5883_DATAZ1 = 0x08 

class HMC5883(object):
    """HMC5883 magnetometer."""

    def __init__(self, address=HMC5883_ADDRESS, i2c=None, **kwargs):
        """Initialize using I2C
        """
        # Setup I2C interface for the device.
        if i2c is None:
            import Adafruit_GPIO.I2C as I2C
            i2c = I2C
        self._device = i2c.get_i2c_device(address, **kwargs)

        self._device.write8(HMC5883_MODE_CTL, 0b00000000)
	self._device.write8(HMC5883_SAMPLERATE_CTL, 0b00011000)
        
    def read(self):
        """Read the current value of the magnetometer and return it as a tuple
        of signed 16-bit X, Y, Z axis values.
        """
        raw = self._device.readList(HMC5883_DATAX0, 6)
        return struct.unpack('<hhh', raw)
