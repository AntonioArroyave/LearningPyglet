import pygame
from pygame.locals import *
from math import sqrt
from OpenGL.GL import *
from OpenGL.GLU import *

phi = (1+sqrt(5))/(2)

verticies = (
    (0, 1, phi), #yz plane
    (0, 1, -phi), 
    (0, -1, phi), 
    (0, -1, -phi), 
    (1, phi, 0), #xy plane
    (1, -phi, 0), 
    (-1, phi, 0), 
    (-1, -phi, 0), 
    (phi, 0, 1), #xz plane
    (phi, 0, -1), 
    (-phi, 0, 1), 
    (-phi, 0, -1),)

edges = (
    (0,2),
    (0,4),
    (0,8),
    (0,6),
    (0,10),
    (1,9),
    (1,6),
    (1,4),
    (1,3),
    (1,11),
    (2,10),
    (2,7),
    (2,5),
    (2,8),
    (3,9),
    (3,5),
    (3,7),
    (3,11),
    (4,6),
    (4,9),
    (4,8),
    (5,8),
    (5,9),
    (5,7),
    (6,10),
    (6,11),
    (7,10),
    (7,11),
    (8,9),
    (10,11),
    )


def Icosahedron():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    pygame.init()
    display = (1500,700)
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
        Icosahedron()
        pygame.display.flip()
        pygame.time.wait(10)


main()
