import serial
import vlc
from time import sleep

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

while True:
    with serial.Serial('/dev/ttyACM0', 9600, timeout=1) as ser:
        line = str(ser.readline())
        line = line[2]
        print(line)
        if line == "0":
            play_video("/home/pi/Pathe/0.mp4")
        elif line == "1":
            play_video("/home/pi/Pathe/1.mp4")
        elif line == "2":
            play_video("/home/pi/Pathe/2.mp4")
        elif line == "3":
            play_video("/home/pi/Pathe/3.mp4")
        elif line == "4":
            play_video("/home/pi/Pathe/Mini-Mega.mp4")
        elif line == "5":
            play_video("/home/pi/Pathe/Mini-Mega.mp4")
