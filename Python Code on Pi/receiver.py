import serial
import vlc
from time import sleep
while True:
    with serial.Serial('/dev/ttyACM0', 9600, timeout=1) as ser:
        line = str(ser.readline())
        line = line[2]
        print(line)
        if line == "0":
            print("Running video")
            media = vlc.MediaPlayer("/home/les/Videos/2019-09-28 11-39-00.m4v")
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

