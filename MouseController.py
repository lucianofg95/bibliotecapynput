from pynput.mouse import Button, Controller

mouse = Controller( )

mouse.position = (1296,496) #coloca o mouse nas coordenadas citadas
#mouse.move(150, 0) #move o mouse nos valores de pixel informado
#mouse.click(Button.right) #clica com o botão rigth ou left e quantidade de vezes informado
# mouse.press(Button.left) #clica e mantem pressionado
# mouse.release(Button.left) #solta o que está pressionado
mouse.scroll(0, -4) #move o scroll do mouse
