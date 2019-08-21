import pygame
from pygame.locals import *
from math import sqrt
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np 


class surface:
    """Create a surface centered in cero, return a Vector and Edges matricies"""
    def __init__(self, number_of_squares = (4), number_of_dimensions = (2), length=(1)):
        self.number_of_dimensions = number_of_dimensions # x and y
        self.length = length # lenght of the grid
        self.number_of_squares = number_of_squares # Number of squares must be a even number 
        self.step = length/number_of_squares # Step
        self.one_side = self.number_of_squares/2 # Number of squares in one side; rigth, left
        self.number_of_verticies = (number_of_squares)**number_of_dimensions
        V = [x for x in np.arange(-length/2, (length/2)+self.step, self.step)]
        V = [[x,y, 0.5*(x**3)+0.5*(y**3)] for x in V for y in V] # here must be replace for de desired function of z 
        self.verticies = np.asarray(V)
        self.verticies_index = [x for x in range(0,self.verticies.shape[0])]
        self.edges = [[x,y] for x in self.verticies_index for y in self.verticies_index if ((x!=y) and (y!=x) and ((sqrt((self.verticies[x][0]-self.verticies[y][0])**2+(self.verticies[x][1]-self.verticies[y][1])**2))<=self.step))]

def draw_edge_verticies_object(verticies, edges):
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
        hiperbolic = surface(number_of_squares = (10), number_of_dimensions = (2), length=(5))
        draw_edge_verticies_object(hiperbolic.verticies, hiperbolic.edges)
        pygame.display.flip()
        pygame.time.wait(10)


main()
