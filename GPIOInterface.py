#Author: Lena Voytek
#it's weatherproof thnx

import time, keypress, read_data



#direct keyboard: 1, Auto: 2
MODE = 1

#setup and import GPIO library
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Motor1A = 23
Motor1B = 25
Motor1E = 24
 
Motor2A = 17
Motor2B = 27
Motor2E = 26

ModeButton = 18
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
 
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

GPIO.setup(ModeButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#movement functions
def forward():
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor1E,GPIO.HIGH)
 
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)
	GPIO.output(Motor2E,GPIO.HIGH)
	return

def leftturn():
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)
	GPIO.output(Motor2E,GPIO.HIGH)

	GPIO.output(Motor1E,GPIO.LOW)
	return
	
def rightturn():
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor1E,GPIO.HIGH)

	GPIO.output(Motor2E,GPIO.LOW)
	return
	
def stopmoving():
	GPIO.output(Motor1E,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.LOW)
	return




runtimes = 0

while 1:

	#Button Mode Switching
	if GPIO.input(ModeButton):
		Mode += 1
		if Mode > 2:
			Mode = 1
	
	#using direct keyboard input
	if (MODE == 1):
		#get the current pressed key
		key = str(keypress.getKey())

		#make vehicle run accordingly
		if key == "w":
			forward()
		elif key == "a":
			leftturn()
		elif key == "d":
			rightturn()
		elif key == "e":
			read_data.measure()
		elif key == "q":
			break
		else:
			stopmoving()
 	
 	
	#AI Movement
 	elif (MODE == 2):
		read_data.measure()	

	#continuous read mode
	elif (MODE == 3):
		read_data.measure()
		
	
GPIO.cleanup()
