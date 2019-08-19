import pyglet
import time

window = pyglet.window.Window()

@window.event
def on_draw():
    v1r = 0
    v2g = 255
    v3b = 0
    v2r = 255
    v2g = 0
    v2b = 0
    v3r = 0 
    v3g = 0 
    v3b = 255

    pyglet.graphics.draw(3, pyglet.gl.GL_TRIANGLES, ('v2i', (100,125,150,50,300,25)), ('c3B', (v1r,v1g,v1b,v2r,v2g,v2b,v2r,v3g,v3b)))
    pyglet.app.run()
    #wait(1000)

