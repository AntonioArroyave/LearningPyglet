import pygame
from pygame.locals import *
from math import *
from OpenGL.GL import *
from OpenGL.GLU import *


def Octahedron(dx=(0), dy=(0), dz=(0), F=(1)):
    phi = (1+sqrt(5))/(2)
    verticies = (
    ((1+dx)*F, (0+dy)*F, (0+dz)*F),
    ((-1+dx)*F, (0+dy)*F, (0+dz)*F),
    ((0+dx)*F, (-1+dy)*F, (0+dz)*F),
    ((0+dx)*F, (1+dy)*F, (0+dz)*F),
    ((0+dx)*F, (0+dy)*F, (1+dz)*F),
    ((0+dx)*F, (0+dy)*F, (-1+dz)*F),
    )
    edges = (
    (0,3), (3,1), (1,2), (2,0),
    (0,4), (1,4), (2,4), (3,4),
    (0,5), (1,5), (2,5), (3,5),
    )

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

    glTranslatef(0.0,0.0, -10.0)

    n = 1
    loopNumber = 0
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
                if event.key == pygame.K_0:
                    n+=1
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

            if event.type ==  pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0,0,1)
                if event.button == 5:  
                     glTranslatef(0,0,-1)

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        loopNumber +=1
        F=sin(loopNumber/pi)
        for i in range(0,n):
            for j in range(0,n):
                for l in range(0,n):
                    Octahedron(i,j,l,F)
        pygame.display.flip()
        pygame.time.wait(10)


main()
