#Author: Lena Voytek

#Get proximity sensor data for AI movement
def get_data():
	prox_left = pyb.ADC(pyb.Pin.cpu.A1)
	prox_right = pyb.ADC(pyb.Pin.cpu.A2)
	print (prox_left.read(), prox_right.read())
	pyb.LED(2).on()

get_data()

