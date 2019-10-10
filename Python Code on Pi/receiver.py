import serial
import vlc
import logzero
import pygame
from logzero import logger
from time import sleep
from PIL import Image

#Logzero file
logzero.logfile("error.log", maxBytes=1e6, backupCount=3)

def picture(img,w,h):
    pic = pygame.image.load(img)
    background = (0, 0, 0)
    screen = pygame.display.set_mode((w,h))
    screen.fill((background))
    screen.blit(pic,(0,0))
    pygame.display.flip()
    #sleep(10)
    #pygame.display.quit()
    #pygame.quit()

def play_video(video):
    print("Running video")
    print(video)
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
#img  = Image.open("title.gif")
#img.show()
picture("title.png",1920,1080)

while True:
    try:
        with serial.Serial('/dev/ttyACM0', 9600, timeout=1) as ser:
            line = str(ser.readline())
            line = line[2]
            print(line)
            if line == "0":
                play_video("0.MOV")
            elif line == "1":
                play_video("1.MOV")
            elif line == "2":
                play_video("2.MOV")
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