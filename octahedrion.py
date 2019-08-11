import pygame
from pygame.locals import *
from math import sqrt
from OpenGL.GL import *
from OpenGL.GLU import *

phi = (1+sqrt(5))/(2)
verticies = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, -1, 0),
    (0, 1, 0),
    (0, 0, 1),
    (0, 0, -1),
    )

edges = (
    (0,3),
    (3,1),
    (1,2),
    (2,0),
    (0,4),
    (1,4),
    (2,4),
    (3,4),
    (0,5),
    (1,5),
    (2,5),
    (3,5),
    )


def Octahedron():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-1,0,0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(1,0,0)
                if event.key == pygame.K_UP:
                    glTranslatef(0,1,0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0,-1,0)

            if event.type ==  pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0,0,1)
                if event.button == 5:  
                     glTranslatef(0,0,-1)

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Octahedron()
        pygame.display.flip()
        pygame.time.wait(10)


main()
