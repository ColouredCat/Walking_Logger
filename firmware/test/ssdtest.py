
from ssd1306 import SSD1306
from machine import i2c, Pin
from time import sleep

a = i2c(scl = Pin(3), sda = Pin(2))
ssd = SSD1306(128, 64, a)

ssd.fill(1)
ssd.show()
sleep(5)