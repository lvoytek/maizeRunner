#Author: Lena Voytek

#Get sensor data from resistance values
def get_data():
	s_light = pyb.ADC(pyb.Pin.cpu.A1)
	s_humidity = pyb.ADC(pyb.Pin.cpu.A2)
	s_temp = pyb.ADC(pyb.Pin.cpu.A3)
	s_flex = pyb.ADC(pyb.Pin.cpu.A4)
	print (s_light.read(), s_humidity.read(), s_temp.read(), s_flex.read())
	pyb.LED(4).on()

get_data()

