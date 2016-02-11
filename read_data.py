#Author: Lena Voytek

import pyboard
import pynmea2 #used to parse gps data

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
		
	logfileb = open('/var/www/html/gpslog.txt','a')

	gpsdatastr = str()
	gpsdatastr += execfil('gpsinput.py')
	gpsdatastr = gpsdatastr[2:-7]
	logfileb.write(gpsdatastr + '\n')
	

	prox = str()
	prox += execfil('proximity.py')

	logfilec = open('proximity.txt', 'w')
	#logfilec.write(execfil('proximity.py'))
	logfilec.write(prox)

	logfile.write("Proximity: " + prox) 

	try:
		msg = pynmea2.parse(gpsdatastr)
		logfile.write("Location: (" + msg.latitude.__str__() + ", " + msg.longitude.__str__() + ")\n\n")
		return (msg.latitude, msg.longitude)
	except pynmea2.nmea.ParseError:
		logfile.write("\n")
		return (None, None)

if __name__ == "__main__":
	measure()
