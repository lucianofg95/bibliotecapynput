from pynput.keyboard import Listener, Key

lista = []
def press(key):
    lista.append(key)
def release(key):
    if key == Key.shift:
        print(lista)



with Listener(on_press=press, on_release=release) as listener:
    listener.join()

