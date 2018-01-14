#Author: Lena Voytek
import pyboard

def execfil(filename, device='/dev/ttyACM0'):
	pyb = pyboard.Pyboard(device)
	pyb.enter_raw_repl()
	output = pyb.execfile(filename)
	pyb.exit_raw_repl()
	pyb.close()
	return output


def measure():
	print("MEASURE:")
	logfile = open('/var/www/html/log.txt','a')
	logfile.write(execfil('main.py'))
		

if __name__ == "__main__":
	measure()
