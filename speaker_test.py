import time
from soundplayer import SoundPlayer

p = SoundPlayer("/home/pi/sound/salza1.wav",1)
print("playerfor 10s with volume 0.5")
p.play(0.5)
time.sleep(10)
P.stop()