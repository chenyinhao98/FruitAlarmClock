import time
import board
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd

lcd_columns = 16
lcd_rows = 2


i2c =board.I2C()
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)
lcd.clear()
lcd.color = [100,0,0]
lcd.message = "Hello World!!!!\n Yinhao"
time.sleep(10)

lcd.color = [0,0,0]
lcd.clear()




           





    