import pygame
import time
import os
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()
for filename in os.listdir(r'C:\Users\owner\Music'):
    pygame.mixer.music.load(
        os.path.join(r'C:\Users\owner\Music', filename))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1000.0)
    time.sleep(30)
    pygame.mixer.music.stop()
