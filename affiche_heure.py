import time
import datetime
print(" killian \n caillere \n 18 ans")
while True:
    now = datetime.datetime.now()
    print("le temps actuel est:", now.strftime("%H:%M:%S"), end='\r')
    time.sleep(1)
