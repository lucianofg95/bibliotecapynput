from pynput.mouse import Button, Listener

def click(x,y, button, pressed):
    print(x,y, button, pressed)


# listener = Listener(on_click=click)
# listener.start()
# listener.join()
# listener.stop()

# Fica menor:
with Listener(on_click=click) as listener: #imprime as coordenadas de movimento do mouse
    listener.join()