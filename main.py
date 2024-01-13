import pygame
import time
pygame.init()
win = pygame.display.set_mode((800,800))
color = (190,130,190)
win.fill(color)
clock = pygame.time.Clock()
img=pygame.image.load("Анатольев.jpg")
img1=pygame.transform.scale(img,(200,200))
k=()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            win.blit(img1, (0, 0))
            pygame.display.update()
            k=pygame.mouse.get_pos()
            pygame.draw.rect(win, (255, 255, 255), (k[0], k[1],250,250))
            pygame.display.update()

    clock.tick(60) #FPS