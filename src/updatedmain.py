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
bodylength = 5
movedirection = ""
direction = ["below", "below", "below","below","below",]
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
                if movedirection == "UP" or movedirection == "DOWN" or movedirection == "": #make sure body cant go back on itself
                    movedirection = "LEFT"
                    xchange = (-1/10)*10
                    ychange = 0    
            elif event.key == pygame.K_RIGHT:
                if movedirection == "UP" or movedirection == "DOWN" or movedirection == "":
                    movedirection = "RIGHT" 
                    xchange = (1/10)*10
                    ychange = 0
            elif event.key == pygame.K_UP:
                if movedirection == "LEFT" or movedirection == "RIGHT" or movedirection == "":
                    movedirection = "UP"
                    ychange = (-1/10)*10
                    xchange = 0
            elif event.key == pygame.K_DOWN:
                if movedirection == "LEFT" or movedirection == "RIGHT" or movedirection == "":
                    movedirection = "DOWN"
                    ychange = (1/10)*10
                    xchange = 0
    x1 += xchange
    y1 += ychange
    if x1 >= 1000 or x1 <= 0 or y1 >= 1000 or y1 <= 0: #Check if player hit the wall
        game_over = True
    if x1 >= foodx and x1 <= foodx+20 and y1 >= foody and y1 <= foody+20 or foodx >= x1 and foodx <= x1+20 and foody >= y1 and foody <= y1+20:
        print("good job") #Checks if player hit the food, then makes a new food position
        #createfood()
        foodx = round(random.randrange(0, 790) / 10.0) * 10.0
        foody = round(random.randrange(0, 590) / 10.0) * 10.0 
        pygame.draw.rect(display,green,[foodx,foody,10,10])
    display.fill(black)
    def drawbody():
        x2 = x1
        y2 = y1
        pygame.draw.rect(display,green,[x1,y1,20,20])
        for i in direction: #creates first body position by looking at the instructions in the direction array
            if i == "below":
                y2 += 20
                pygame.draw.rect(display,blue,[x2,y2,20,20])
            elif i == "above":
                y2 -= 20
                pygame.draw.rect(display,blue,[x2,y2,20,20])
            elif i == "left":
                x2 -= 20
                pygame.draw.rect(display,blue,[x2,y2,20,20])
            elif i == "right":
                x2 += 20
                pygame.draw.rect(display,blue,[x2,y2,20,20])
    def getoldcoords(x,y,array,c):
        xcoord = x
        ycoord = y
        for i in array[:c]:
            if i == "below":
                ycoord += 20
            elif i == "above":
                ycoord-= 20
            elif i == "left":
                xcoord-=20
            elif i == "right":
                xcoord+= 20
        return xcoord,ycoord
    def updatearray(array, movedirection):
        i = len(array) - 1
        while i > 0:
            if i != 1:
                array[i] = array[i-1]
                i -= 1
            else: #when the snake turns, change the position of each block
                if movedirection == "DOWN":
                    array[i] = "above"
                elif movedirection == "UP":
                    array[i] = "below"
                elif movedirection == "LEFT":
                    array[i] = "right"
                elif movedirection == "RIGHT":
                    array[i] = "left"
                i -= 1
    for z in range(bodylength):
        if z == 1:
            pygame.draw.rect(display,green,[x1,y1,20,20])
        else:
            a,b = getoldcoords(x1-xchange,y1-ychange,direction,z-1)
            pygame.draw.rect(display,blue,[a,b,20,20])
    updatearray(direction, movedirection)
    pygame.draw.rect(display, green, [foodx, foody, 20,20])
    pygame.display.update()
print("You Lost")
pygame.display.update()
pygame.quit()
quit()
