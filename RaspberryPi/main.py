import HiwonderSDK.Sonar as Sonar
import HiwonderSDK.Board as Board
from HiwonderSDK import mecanum
import time

'''MOTOR STEP UP'''
motor = mecanum.MecanumChassis()

def stop_car():
	motor.set_velocity(0, 0, 0)

def drive_forward(velocity = 100):
	motor.translation(0, velocity)

def rotate_car(direction, velocity):
	pass


'''SONAR SET UP'''
sonar = Sonar.Sonar()
sonar.setRGBMode(0)
sonar.setPixelColor(0, Board.PixelColor(0,0,255))
sonar.setPixelColor(1, Board.PixelColor(0,0,255))
sonar.show()

def sonar_detect_obstacle(stoping_distance = 120, verbose = True):
	distance = sonar.getDistance()
	if stoping_distance > distance:
		
		if verbose:
			print("sonar: car stops", distance)
		return True
	else:
		if verbose:
			print("sonar: ", distance)
		return False
	



'''MAIN LOOP'''
while True:
	time.sleep(1)
	if sonar_detect_obstacle():
		stop_car()
	else:
		pass
		#drive_forward()
	
	
	
	
	

print('Hello')

