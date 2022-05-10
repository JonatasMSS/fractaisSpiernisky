from dis import dis
from lib2to3.refactor import FixerError
from operator import le
import random
from turtle import Screen, circle, width
import pygame
import math
pygame.init()




WIDTH, HEIGHT = 600,600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Planetas")


class point():
    def __init__(self,x,y):
        self.x,self.y = x,y
    def draw(self):
        pygame.draw.circle(WIN,(255,255,255),(self.x,self.y),1)
class textOBJ():
    def __init__(self,text,color,pos):
        self.text = text
        self.color = color
        self.pos = pos
    def draw(self):
        font = pygame.font.SysFont(None,24)
        img = font.render(self.text,True,self.color)
        WIN.blit(img,self.pos)
        



def middlePointsCreator(pA,pB):
    pAx,pAy,pBx,pBy = pA.x,pA.y,pB.x,pB.y
    dxAB = pBx + pAx
    dyAB = pBy + pAy
    middlePX = dxAB/2
    middlePY = dyAB/2
    return point(middlePX,middlePY)


def main():
    run = True
    clock = pygame.time.Clock()
    p1 = point(WIDTH/2,HEIGHT/2-200)
    p2 = point(WIDTH/2-200,HEIGHT/2+200)
    p3 = point(WIDTH/2+200,HEIGHT/2+200)
    fixedPoints = [p1,p2,p3]
    middlePoints = [p1,p2,p3]
    TIME = 120
    
    while run:
        clock.tick(TIME)
        WIN.fill((0,0,0))
        texto = textOBJ(f"Numero de pontos:{len(middlePoints)}",(255,255,255),(400,560))
        texto.draw()
        for pt in fixedPoints:
            pt.draw()
            nP = middlePointsCreator(pt,middlePoints[random.randint(0,len(middlePoints)) - 1])
            middlePoints.append(nP)
        for ptN in middlePoints:
            ptN.draw()
                
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
          

        

        pygame.display.update()
        
    pygame.quit()
main()
