import pygame
from pygame.locals import *
from math import sqrt
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy 

def distance(x,y,verticies):
    result = ((sqrt((verticies[x][0]-verticies[y][0])**2+(verticies[x][1]-verticies[y][1])**2+((verticies[x][2]-verticies[y][2])**2))))
    print(result)
    return result

def Grid(xSize, ySize, step):
    xAxis = numpy.arange(-(xSize/2), (xSize/2), step)
    yAxis = numpy.arange(-(ySize/2), (ySize/2), step)
    verticies = [[x,y,((x**2)-(y**2))] for x in xAxis for y in yAxis]
    verticiesIndex = [ x for x in range(0, len(verticies),1)]
    edges = [[x,y] for x in verticiesIndex for y in verticiesIndex if ((x!=y) and (y!=x) and (distance(x,y, verticies)<=step+0.5))]
    print("verticies"+str(verticies))
    print("verticiesIndex"+str(verticiesIndex))
    print("edges"+str(edges))
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
        Grid(2,2, 1)
        pygame.display.flip()
        pygame.time.wait(10)


main()
