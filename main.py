#Author: Lena Voytek

from pyb import I2C
#Get sensor data from resistance values
def get_data():
	s_light = pyb.ADC(pyb.Pin.cpu.A4)
	s_humidity = pyb.ADC(pyb.Pin.cpu.A1)

	s_temp = I2C(2, I2C.MASTER, baudrate=100000) #Y9-10
	

	s_flex = pyb.ADC(pyb.Pin.cpu.A0)
	print ("Light:", s_light.read(), "Humidity:", s_humidity.read(), "WindSpeed:", s_flex.read(), " "),
	pyb.LED(4).on()

get_data()

