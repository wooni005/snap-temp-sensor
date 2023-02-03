
#!/usr/bin/python3

import time
import signal
import json
import random
import paho.mqtt.publish as mqtt_publish


__version__ = '0.1'
mqttServer = "127.0.0.1"
exitLoop = False


def signal_handler(_signal, frame):
    global exitLoop

    print('You pressed Ctrl+C!')
    exitLoop = True


def main():
    # Init signal handler, because otherwise Ctrl-C does not work
    signal.signal(signal.SIGINT, signal_handler)

    livingroomTemp = {'Temperature': 20.3, 'Humidity': 49}

    while not exitLoop:
        time.sleep(2)  #[sec]

        digitTemp = random.randint(0, 5)
        digitHum = random.randint(5, 9)

        livingroomTemp['Temperature'] = "20.%d" % digitTemp
        livingroomTemp['Humidity'] = "4%d" % digitHum

        mqtt_publish.single("house/Livingroom/temp", json.dumps(livingroomTemp, separators=(', ', ':')), qos=1, hostname=mqttServer, retain=False)

    print("Clean exit")
