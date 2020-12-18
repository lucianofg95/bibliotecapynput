from pynput.keyboard import Key, Controller

keyb = Controller()

# keyb.press('1')
# keyb.release('1')

# keyb.type('Olá mundo')

keyb.press(Key.f11)
keyb.release(Key.f11)

#with keyb.pressed(Key.ctrl, Key.alt):
#    keyb.press('l')
#    keyb.press('l')
