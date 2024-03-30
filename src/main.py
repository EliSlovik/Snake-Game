import pygame
import random
pygame.init()
display=pygame.display.set_mode((1000,1000))
pygame.display.set_caption('Snake Game')
pygame.display.update()
red=(255,0,0)
blue=(0,0,255)
black=(0,0,0)
green=(0,255,0)
x1=300
y1=300
xchange=0
ychange=0
foodx = round(random.randrange(0, 790) / 20.0) * 20.0
foody = round(random.randrange(0, 590) / 20.0) * 20.0 
#def createfood():
    #foodx = round(random.randrange(0, 790) / 10.0) * 10.0
    #foody = round(random.randrange(0, 590) / 10.0) * 10.0
game_over = False
while not game_over:
    pygame.draw.rect(display,green,[foodx,foody,10,10])
    display.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xchange = (-1/10)*10
                ychange = 0
            elif event.key == pygame.K_RIGHT:
                xchange = (1/10)*10
                ychange = 0
            elif event.key == pygame.K_UP:
                ychange = (-1/10)*10
                xchange = 0
            elif event.key == pygame.K_DOWN:
                ychange = (1/10)*10
                xchange = 0
    x1 += xchange
    y1 += ychange
    if x1 >= 1000 or x1 <= 0 or y1 >= 1000 or y1 <= 0:
        game_over = True
    if x1 >= foodx and x1 <= foodx+20 and y1 >= foody and y1 <= foody+20 or foodx >= x1 and foodx <= x1+20 and foody >= y1 and foody <= y1+20:
        print("good job")
        #createfood()
        foodx = round(random.randrange(0, 790) / 10.0) * 10.0
        foody = round(random.randrange(0, 590) / 10.0) * 10.0 
        pygame.draw.rect(display,green,[foodx,foody,10,10])
    display.fill(black)
    pygame.draw.rect(display,blue,[x1,y1,20,20])
    pygame.draw.rect(display, green, [foodx, foody, 20,20])
    pygame.display.update()
print("You Lost")
pygame.display.update()
pygame.quit()
quit()
