import Adafruit_ADXL345
import Adafruit_BMP.BMP085 as Adafruit_BMP085
import JHURC_HMC5883
import JHURC_L3G4200D

class GY80(object):
    """GY80 IMU"""

    CONVERT_ACCEL = 3.9 * 0.001 * 9.8; # m/s^2
    CONVET_GYRO = 250 * 0.001;
   

    def __init__(self):
        self.gyro = JHURC_L3G4200D.L3G4200D()
        self.accel = Adafruit_ADXL345.ADXL345()
        self.baro = Adafruit_BMP085.BMP085()
        self.mag = JHURC_HMC5883.HMC5883()

    def getOrientation(self):
        return self.gyro.read()

    def getAcceleration(self):
        return [x*self.CONVERT_ACCEL for x in self.accel.read()]

    def getTemperature(self):
        return self.baro.read_temperature()

    def getPressure(self):
        return self.baro.read_pressure()

    def getSeaLevelPressure(self):
        return self.baro.read_sealevel_pressure()

    def getAltitude(self):
        return self.baro.read_altitude()

    def getBearing(self):
        return self.mag.read()


    def __str__(self):
        ret = "Orientation:\t{0}\n".format(self.getOrientation()) \
            + "Accel:\t\t({:.3f}, {:.3f}, {:.3f}) m/s^2\n".format(*self.getAcceleration()) \
            + "Temp:\t\t{0}\n".format(self.getTemperature()) \
            + "Press:\t\t{0}\n".format(self.getPressure()) \
            + "Altitude:\t{0}\n".format(self.getAltitude()) \
            + "Bearing:\t{0}".format(self.getBearing())
        return ret
