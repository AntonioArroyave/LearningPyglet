import pyglet
from pyglet.gl import *

window = pyglet.window.Window()
label = pyglet.text.Label('Hello kathe', font_name='Times New Roman', font_size=36, color=(200,200,200,200), x = window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')
image = pyglet.resource.image('magos.png')

@window.event
def on_draw():
    window.clear()
    glBegin(GL_LINES)
    glVertex2i(50, 50)
    glVertex2i(75, 100)
    glVertex2i(100, 150)
    glVertex2i(200, 200)
    image.blit(0,0)
    label.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    print('Mouse pressed in position: ' + str(x) + ","+str(y))
    if button == pyglet.window.mouse.LEFT:
        print('The keft mouse button ws pressed.')

@window.event
def on_key_press(symbol, modifiers):
    print('A key was pressed')
    if symbol == pyglet.window.key.A:
        print('The "A" key was pressed.')

pyglet.app.run()
