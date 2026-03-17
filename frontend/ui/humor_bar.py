import pygame

GREEN = (0, 255, 0)

RED = (255, 0, 0)

class HumorBar:

    def __init__(self,x,y):

        self.x = x
        self.y = y

    def draw(self,screen,value):

        width = 200
        height = 20

        ratio = value / 100
        fill = width * ratio

        color = None

        if value <= 50:
            color = RED
        else: color = GREEN

        pygame.draw.rect(screen,(255,255,255),(self.x,self.y,width,height),2) # bordo
        pygame.draw.rect(screen, color,(self.x,self.y,fill,height)) # riempimento