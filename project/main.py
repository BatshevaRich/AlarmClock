import pygame
import time
import os
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()

while True:
    now = time.localtime()
    if now.tm_hour == int(16) and now.tm_min == int(13):
        print("ALARM NOW!")
        for filename in os.listdir(r'C:\Users\owner\Music\הנשמה בקרבי'):
            pygame.mixer.music.load(
                os.path.join(r'C:\Users\owner\Music\הנשמה בקרבי', filename))
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(1000.0)
            time.sleep(30)
            pygame.mixer.music.stop()
        break

    else:
        time.sleep(60 - now.tm_sec)
        print("no alarm", 60 - now.tm_sec)