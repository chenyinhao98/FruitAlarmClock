import time
import board
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd

from pydub import AudioSegment
from pydub.playback import play

lcd_columns = 16
lcd_rows = 2


i2c =board.I2C()
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)
lcd.clear()
lcd.color = [100,0,0]
sound = AudioSegment.from_wav('piano2.wav')
lcd.message = "Welcome to\nFruit Alarm"
play(sound)

lcd.clear()

lcd.message = "It is 8:00AM! \n Get Up!"
sound = AudioSegment.from_wav('iphone_radar.wav')
play(sound)

lcd.color = [0,0,0]
lcd.clear()




           





    