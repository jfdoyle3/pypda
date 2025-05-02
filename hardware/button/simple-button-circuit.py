##   Simple button Test Raspberry Pi 3b
##   button - use one side
##   resistor 
##   wires
##
##   wire a pin from button to pin 10 (RDX0/GPIO15)
##   connect one end of resister to other button pin
##   wire other side of resistor to pin 1 (3V3)
##
##   run program
##
##   CTRL-C to exit




import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
print("Press Button")
while True: # Run forever
    if GPIO.input(10) == GPIO.HIGH:
        print("Button was pushed!")
    if GPIO.input(10)==GPIO.LOW:
        print("Press Button")
