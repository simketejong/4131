import time
import RPi.GPIO as GPIO

SPI_CS_PIN = 21 # Channel Select This is inverted so False = Active and True = DeActivate 
SPI_CLK_PIN = 10 # The Clock
SPI_SDISDO_PIN = 11 # mosi, DATA
SPEED_PIN = 20 # Yellow cable fan (use pull up resistor)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# input voor speed 
GPIO.setup(SPEED_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# RPM for speed
x = 0
interval = 1

# Count number of pulses
def count(channel):
  global x
  x = x + 1

# defineer dat PIN's deconfigireerd zijn als outputs
GPIO.setup(SPI_CS_PIN, GPIO.OUT)
GPIO.setup(SPI_CLK_PIN, GPIO.OUT)
GPIO.setup(SPI_SDISDO_PIN, GPIO.OUT)

# Interrupt for speed
GPIO.add_event_detect(SPEED_PIN, GPIO.RISING, callback=count)

def set_value(value):
# Zit "chip select" even uit. Als True dan ontvangt chip geen data
    GPIO.output(SPI_CS_PIN, True)
# Zit klok voor zekerheid laag
    GPIO.output(SPI_CLK_PIN, False)
# Activeer de chip die data moet ontvangen
    GPIO.output(SPI_CS_PIN, False)

# Zit de bitstream in het goeie formaat
    b = '{0:016b}'.format(value)
# Loop door de byte en stuur dus na chip
    for x in range(0, 16):
        #print 'x:' + str(x) + ' -> ' + str(b[x])
# Dit is de Output voor de Data
        GPIO.output(SPI_SDISDO_PIN, int(b[x]))
# Pulse de klok
        GPIO.output(SPI_CLK_PIN, True)
        GPIO.output(SPI_CLK_PIN, False)
# Deselecteer de chip
    GPIO.output(SPI_CS_PIN, True)
# 
# DEMO beneden loopt van 0 tot 5 volt
#

while True:
    for level in range(0, 128):
        x = 0
        time.sleep(interval)
        print int(x /2 /interval *60), "RPM"        
        print 'level:' + str(level)
        set_value(level)
 