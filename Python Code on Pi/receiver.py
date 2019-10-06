import serial
import vlc
import logzero
from logzero import logger
from time import sleep
from PIL import Image

#Logzero file
logzero.logfile("error.log", maxBytes=1e6, backupCount=3)

def play_video(video):
    print("Running video")
    #media = vlc.MediaPlayer("/home/les/Videos/2019-09-28 11-39-00.m4v")
    media = vlc.MediaPlayer(video)
    media.set_fullscreen(b_fullscreen=True)
    media.play()
    sleep(3)
    state = str(media.get_state())
    print(type(state))
    print(state)
    while state == "State.Playing":
        print("playing")
        sleep(1)
        state = str(media.get_state())
    else:
        media.stop()
        print("ENDED")

#Display an image
img  = Image.open("/home/les/Pictures/APOD.jpg")
img.show()

while True:
    try:
        with serial.Serial('/dev/ttyACM0', 9600, timeout=1) as ser:
            line = str(ser.readline())
            line = line[2]
            print(line)
            if line == "0":
                play_video("/home/les/Desktop/Pathe/0.mp4")
            elif line == "1":
                play_video("/home/les/Desktop/Pathe/1.mp4")
            elif line == "2":
                play_video("/home/les/Desktop/Pathe/2.mp4")
            elif line == "3":
                play_video("/home/les/Desktop/Pathe/3.mp4")
            elif line == "4":
                play_video("/home/les/Videos/Mini-Mega.mp4")
            elif line == "5":
                play_video("/home/les/Videos/Mini-Mega.mp4")
    except:
        print("No Bare Conductive Touch Board found")
        logger.error("No Bare Conductive Touch Board has been found.")
        break
