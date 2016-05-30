# 4131
Configuration

This program uses the python lib GPIO

sudo apt-get install python-dev python-rpi.gpio

The PIN configuration
Use Raspberry Pi B+
To use other Raspberry check pinouts

The CHIP 4131
http://cdn.instructables.com/FZD/D5LP/HI3TY4Z0/FZDD5LPHI3TY4Z0.SQUARE2.jpg

4131						    		Raspberry
"Pin 1 (channel select)  Connect to 	Pin 31 "
Pin 2 (Clock)				    Connect to 	Pin 10
Pin 3 (DATA)				    Connect to 	Pin 11
Pin 4 (Vss)					    Connect to 	GND (raspberry)
Pin 5 (POA)					    Connect to 	GND (raspberry)
Pin 6 (Variable Resistor)	Red Cable on two pin connector on AP182
PIN 7 (POB)					    Connect to  5V (raspberry)
Pin 8 (Vdd)					    Connect to 	5V (raspberry)

Black Cable two pin connector connect to GND on raspberry.

On the 3 pin connector
Black to GND raspberry
Red to 12Volt DC power supply
Yellow cable connect to Pin 20 on raspberry
Connect Pin 20 (raspberry) to one side of any resistor and the other side to the 5V on raspberry (PULLUP RESISTOR)
