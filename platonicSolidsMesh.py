import pygame
from pygame.locals import *
from math import sqrt
from OpenGL.GL import *
from OpenGL.GLU import *

phi = (1+sqrt(5))/(2)

def Tetrahedron(deltaX):
    verticies = ((0 + deltaX, 0, 0), (1 + deltaX, 0, 0), (0.5 + deltaX, 1, 0), (0.5 + deltaX, 0.5, -1))
    edges = ((0,1), (1,2), (2,0), (0,3), (1,3), (2,3))
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def Cube(deltaX):
    verticies = ((1+deltaX, -1, -1),(1+deltaX, 1, -1),(-1+deltaX, 1, -1),(-1+deltaX, -1, -1),(1+deltaX, -1, 1),
                 (1+deltaX, 1, 1),(-1+deltaX, -1, 1),(-1+deltaX, 1, 1))
    edges = ((0,1),(0,3),(0,4),(2,1),(2,3),(2,7),(6,3),(6,4),(6,7),(5,1),(5,4),(5,7))
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def Octahedron(deltaX):
    verticies = ((1+deltaX, 0, 0), (-1+deltaX, 0, 0), (0+deltaX, -1, 0), (0+deltaX, 1, 0), (0+deltaX, 0, 1), (0+deltaX, 0, -1),)
    edges = ((0,3),(3,1),(1,2),(2,0),(0,4),(1,4),(2,4),(3,4),(0,5),(1,5),(2,5),(3,5))
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def Dodecahidron(deltaX):
    verticies = ((1+deltaX, 1, 1), (-1+deltaX, 1, 1), (-1+deltaX, -1, 1), (1+deltaX, -1, 1), (1+deltaX, 1, -1),
                 (-1+deltaX, 1, -1), (-1+deltaX, -1, -1), (1+deltaX, -1, -1), (0+deltaX, phi, 1/phi),
                 (0+deltaX, -phi, 1/phi), (0+deltaX, -phi, -1/phi), (0+deltaX, phi, -1/phi), ((1/phi)+deltaX, 0, phi),
                 ((-1/phi)+deltaX, 0, phi), ((-1/phi)+deltaX, 0, -phi), ((1/phi)+deltaX, 0, -phi),
                 (phi+deltaX, 1/phi, 0), (-phi+deltaX, 1/phi, 0), (-phi+deltaX, -1/phi, 0), (phi+deltaX, -1/phi, 0),)
    edges = ((0,12),(0,8),(0,16),(1,13),(1,8),(1,17),(2,13),(2,9),(2,18),(3,12),(3,19),(3,9),(4,16),(4,15),(4,11),(5,11)
             ,(5,17),(5,14),(6,18),(6,10),(6,14),(7,15),(7,19),(7,10),(8,11), (9,10),(12,13),(14,15),(16,19),(17,18),)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def Icosahedron():
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
        (0,2), (0,4), (0,8), (0,6), (0,10), (1,9), (1,6), (1,4), (1,3), (1,11), (2,10), (2,7), (2,5), (2,8), (3,9), (3,5), (3,7), (3,11), (4,6), (4,9), (4,8), (5,8), (5,9), (5,7), (6,10), (6,11), (7,10), (7,11), (8,9), (10,11),)
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

        glRotatef(1, 3, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Tetrahedron(12)
        Octahedron(10)
        Cube(8)
        Dodecahidron(4)
        Icosahedron()
        pygame.display.flip()
        pygame.time.wait(10)


main()
