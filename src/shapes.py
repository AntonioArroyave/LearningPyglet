import pyglet
from pyglet.gl import *

class Object():
    """A privitive class for draw math objects"""

    """Construct an math object to draw"""
    def __init__(self, shapePrimitive):
        self.shapePrimitive = shapePrimitive

    def draw():
        glBegin(GL_POLYGON)
        glVertex3f(0,0,0)
        glVertex3f(0,0,5)
        glVertex3f(5,5,0)
        glVertex3f(0,5,0)
        glVertex3f(5,5,5)

pos = [0, 0, -20]
rot_y = 0

config = Config(sample_buffers=1, samples=8)
tela = pyglet.window.Window(height=500, width=500, config=config)

@tela.event
def on_draw():

    global pos_z, rot_y

    tela.clear()

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90, 1, 0.1, 100)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glTranslatef(*pos)
    glRotatef(rot_y, 0, 1, 0)
    glBegin(GL_QUADS)
    glVertex3f(0,0,0)
    glVertex3f(0,0,5)
    glVertex3f(5,5,0)
    glVertex3f(0,5,0)
    glVertex3f(5,5,5)

    newObject = Object(GL_POLYGON) 

    glEnd()

    glFlush()

@tela.event
def on_key_press(s,m):

    global pos_z, rot_y

    if s == pyglet.window.key.W:
        pos[2] -= 1
    if s == pyglet.window.key.S:
        pos[2] += 1
    if s == pyglet.window.key.A:
        rot_y += 5
    if s == pyglet.window.key.D:
        rot_y -= 5


def draw_objects(objects_list):
    for object in objects_list:
        object.begin()
        object.draw()
        glEnd()
        glFlush()


pyglet.app.run()
