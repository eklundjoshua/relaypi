#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

#pinList = [2, 3, 4, 17, 27, 22, 10, 9]

# New Pin List According to WiringPi GPIO 0-7
# These pins will all be Active Low & IN on Boot
# according to the RPI Rev 2 Board Specs
pinList = [17, 18, 27, 22, 23, 24, 25, 4]

# loop through pins and set mode and state to 'low'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeL = 2

# main loop

try:
  GPIO.output(17, GPIO.LOW)
  print "ONE"
  time.sleep(SleepTimeL); 
  GPIO.output(18, GPIO.LOW)
  print "TWO"
  time.sleep(SleepTimeL);  
  GPIO.output(27, GPIO.LOW)
  print "THREE"
  time.sleep(SleepTimeL);
  GPIO.output(22, GPIO.LOW)
  print "FOUR"
  time.sleep(SleepTimeL);
  GPIO.output(23, GPIO.LOW)
  print "FIVE"
  time.sleep(SleepTimeL);
  GPIO.output(24, GPIO.LOW)
  print "SIX"
  time.sleep(SleepTimeL);
  GPIO.output(25, GPIO.LOW)
  print "SEVEN"
  time.sleep(SleepTimeL);
  GPIO.output(4, GPIO.LOW)
  print "EIGHT"
  time.sleep(SleepTimeL);
  GPIO.cleanup()
  print "Good bye!"

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()


# find more information on this script at
# http://youtu.be/oaf_zQcrg7g