# TODO:
# get current orientation of the accelerometer (integrate the gyro) to get oritentation
# then use this orientation to determine the effect of gravity, and subtract it
# method:
# - rotate the acceleration vector by the quaternion (determined from the orientation) to get the acceleration in the earth's frame of reference
# - then simply subtract off gravity in the earth's frame of reference (0, 0, -9.81)

import time

import Adafruit_ADXL345
accel = Adafruit_ADXL345.ADXL345()

import JHURC_L3G4200D
gyro = JHURC_L3G4200D.L3G4200D()

def calcOrientation(da, db, dc, a, b, c, dt):
	a += da * dt
	b += db * dt
	c += dc * dt
	return da, db, dc

def calcVelocity(ddx, ddy, ddz, dx, dy, dz, dt):
	dx += ddx * dt
	dy += ddy * dt
	dz += ddz * dt
	return dx, dy, dz

def calcPosition(dx, dy, dz, x, y, z, dt):
	x += dx * dt
	y += dy * dt
	z += dz * dt
	return x, y, z

def main():
	i = 0
	x = y = z = 0
	dx = dy = dz = 0
	a = b = c = 0
	da = db = dc = 0

	while True:
		startTime = time.time()
		ddx, ddy, ddz = accel.read()
		dt = time.time() - startTime
	
		dx, dy, dz = calcVelocity(ddx, ddy, ddz, dx, dy, dz, dt)
		x, y, z = calcPosition(dx, dy, dz, x, y, z, dt)

		a, b, c = calcOrientation(da, db, dc, a, b, c, dt)

		i += 1
		if i % 100 == 0:
			print("position: {0}, {1}, {2}".format(x, y, z))
			print("velocity: {0}, {1}, {2}".format(dx, dy, dz))

if __name__ == "__main__":
	main()
