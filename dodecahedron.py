import pygame
from pygame.locals import *
from math import sqrt
from OpenGL.GL import *
from OpenGL.GLU import *

phi = (1+sqrt(5))/(2)

verticies = (
    (1, 1, 1), # Orange basic cube
    (-1, 1, 1),
    (-1, -1, 1),
    (1, -1, 1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, -1),
    (0, phi, 1/phi),  # Green
    (0, -phi, 1/phi),
    (0, -phi, -1/phi),
    (0, phi, -1/phi),
    (1/phi, 0, phi),  # Blue
    (-1/phi, 0, phi),
    (-1/phi, 0, -phi),
    (1/phi, 0, -phi),
    (phi, 1/phi, 0),  # Pink
    (-phi, 1/phi, 0),
    (-phi, -1/phi, 0),
    (phi, -1/phi, 0),)

edges = (
    (0,12),
    (0,8),
    (0,16),
    (1,13),
    (1,8),
    (1,17),
    (2,13),
    (2,9),
    (2,18),
    (3,12),
    (3,19),
    (3,9),
    (4,16),
    (4,15),
    (4,11),
    (5,11),
    (5,17),
    (5,14),
    (6,18),
    (6,10),
    (6,14),
    (7,15),
    (7,19),
    (7,10),
    (8,11),
    (9,10),
    (12,13),
    (14,15),
    (16,19),
    (17,18),
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
