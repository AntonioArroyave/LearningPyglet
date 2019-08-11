import pyglet
from pyglet.gl import *

window = pyglet.window.Window()

@window.event
def on_draw():
    window.clear()
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
