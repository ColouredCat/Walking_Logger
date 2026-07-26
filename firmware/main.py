
#import libraries
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from gps import GPS_Module
from OSGridConverter import ll_to_os
from bme280_int import BME280
from time import sleep

#setup display, bme and gps
i2cA = I2C(scl=Pin(5), sda=Pin(4))
i2cB = I2C(scl=Pin(7), sda=Pin(6))

dis = SSD1306_I2C(128, 64, i2cA)
GPS = GPS_Module(0, 12, 13)
BME = BME280(i2c=i2cB)

while True:
    #check if a fix is found
    if GPS.get_fix():
        dis.fill(0)
        dis.text(GPS.str_time(), 0, 0, 1)
        
        #get and format os grid reference from lat long
        g = ll_to_os(GPS.lat, GPS.long)
        str_g = f"{g[0]} {g[1]}"
        dis.text(str_g, 0, 16, 1)
        
        dis.text(str(GPS.sat) + " sat tracked", 0, 32, 1)
    else:
        #show if no fix is found
        dis.fill(0)
        dis.text("No fix found", 0, 0, 1)

    dis.text(f"{BME.values[0]} {BME.values[1]} {BME.values[2]}",0, 48, 1)
        
    dis.show()
    sleep(1)

