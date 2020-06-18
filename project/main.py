import playsound
import os
for filename in os.listdir(r'C:\Users\owner\Music'):
    playsound.playsound(
        os.path.join(r'C:\Users\owner\Music', filename))
