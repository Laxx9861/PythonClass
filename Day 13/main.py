import datetime as dt
from playsound import playsound


def play():
    # Sound Play
    playsound('sound.mp3')


i = 100
while(i==100):
    x = dt.datetime.now()
    print(x)

    if int(x.strftime("%M")) ==42:
        play()
        break
        i = 101
         