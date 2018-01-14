#Author: Lena Voytek
#Get GPS data from uart6
from pyb import UART

def get_gps():
	uart = UART(6, 9600)
	print(uart.readline())
	pyb.LED(3).on()	

	

get_gps()

