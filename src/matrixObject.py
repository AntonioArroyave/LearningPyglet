import pygame
from pygame.locals import *
from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

def Octahedron(dx=(0), dy=(0), dz=(0), F=(1)):
    phi = (1+sqrt(5))/(2)
    translateMatrix = np.array([
    [dx, dy, dz],
    [dx, dy, dz],
    [dx, dy, dz],
    [dx, dy, dz],
    [dx, dy, dz],
    [dx, dy, dz],
    ])
    Verticies =np.array([
    [1, 0, 0],
    [-1, 0, 0],
    [0, -1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [0, 0, -1]])
    rangeVerticies = np.size(Verticies,0)
    Verticies = (Verticies + translateMatrix) * F
    edges = np.array([[0, 0, 0, 1, 1, 1],  [0, 0, 1, 0, 1, 1],  [1, 0, 0, 0, 1, 1], [0, 1, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
    aristas = np.where(edges == 1)
    edges =  list(zip(aristas[0], aristas[1])) 
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(Verticies[vertex])
    glEnd()

def fullMesh(dx=(0), dy=(0), dz=(0), F=(1)):
    phi = (1+sqrt(5))/(2)
    translateMatrix = np.array([
    [dx, dy, dz],
    [dx, dy, dz],
    [dx, dy, dz],
    [dx, dy, dz],
    [dx, dy, dz],
    [dx, dy, dz],
    ])
    Verticies =np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [-1, 0, 0],
    [0, -1, 0],
    [0, 0, -1]])
    rangeVerticies = np.size(Verticies,0)
    #Verticies = (Verticies + translateMatrix) * F
    edges = np.ones((rangeVerticies, rangeVerticies))
    edges = np.array([[0, 0, 0, 1, 1, 1],  [0, 0, 1, 0, 1, 1],  [1, 0, 0, 0, 1, 1], [0, 1, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
    aristas = np.where(edges == 1)
    edges =  list(zip(aristas[0], aristas[1])) 
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(Verticies[vertex])
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
        F=sin((loopNumber/1000)*pi)
        print(loopNumber)
        for i in range(0,n):
            for j in range(0,n):
                for l in range(0,n):
                    fullMesh(i,j,l,F)
        pygame.display.flip()
        pygame.time.wait(10)


main()
