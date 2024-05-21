class Snake:
    def __init__(self, x, y, bodylength, direction):
        self.x=x
        self.y=y
        self.bodylength=bodylength
        self.direction = direction

    def draw(self, display, green):
        pygame.draw.rect(display,green,[self.x,self.y,20,20])       
        for i in range(0, self.bodylength):
            if self.direction == "RIGHT":
                pygame.draw.rect(display,green,[self.x-(20 * i),self.y,20,20])
            elif self.direction == "LEFT":
                pygame.draw.rect(display,green,[self.x+(20 * i),self.y,20,20]) 
            elif self.direction == "UP":
                pygame.draw.rect(display,green,[self.x,self.y+(20 * i),20,20])
            elif self.direction == "DOWN":
                pygame.draw.rect(display,green,[self.x,self.y-(20 * i),20,20])

    def change_direction(self, newdirection):
        if newdirection == "UP":
            self.direction = "UP"
        elif newdirection == "DOWN":
            self.direction = "DOWN"
        elif newdirection == "LEFT":
            self.direction = "LEFT"
        elif newdirection == "RIGHT":
            self.direction = "RIGHT"
               
    def move(self):
        if self.direction == "UP":
            self.y -= speed
            pygame.draw.rect(display,green,[self.x,self.y,20,20])   
        elif self.direction == "DOWN":
            self.y += speed
            pygame.draw.rect(display,green,[self.x,self.y,20,20])   
        elif self.direction == "LEFT":
            self.x -= speed
            pygame.draw.rect(display,green,[self.x,self.y,20,20])   
        elif self.direction == "RIGHT":
            self.x += speed

        

    def grow(self):
        bodylength += 1
    def die(self):
        pass
class Food:
    
    def __init__(self, x, y, food_numb):
        self.x=x
        self.y=y
        self.food_numb=food_numb
        
    def draw(self, display, red):
        pygame.draw.rect(display,red,[self.x,self.y,20,20])
        
    def move(self):
        self.x = round(random.randrange(0, 79) * 10)
        self.y = round(random.randrange(0, 59) * 10)
        pygame.draw.rect(display,red,[self.x,self.y,20,20])
        
# code starts
import pygame
import random
pygame.init()
display=pygame.display.set_mode((1000,1000))
pygame.display.set_caption('Snake Game')
pygame.display.update()
speed = 0.5
red=(255,0,0)
blue=(0,0,255)
black=(0,0,0)
green=(0,255,0)
game_over = False
movedirection = ""
foodx = round(random.randrange(0, 79) * 10)
foody = round(random.randrange(0, 59) * 10)
food1 = Food(500, 500, 1)
elis_snake = Snake(300,300,1,"RIGHT")
while not game_over:
    display.fill(black)
    food1.draw(display, red)
    color = display.get_at((int(elis_snake.x),int(elis_snake.y)))

    for i in range (20):
        for z in range (20):
            color = display.get_at((int(elis_snake.x+z),int(elis_snake.y+i)))
            if color.r == 255:
                food1.move()
                print("we hit red")
                break
            else:
                continue
            break  
    elis_snake.draw(display, green)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                elis_snake.change_direction("LEFT")
            elif event.key == pygame.K_RIGHT:
                elis_snake.change_direction("RIGHT")
            elif event.key == pygame.K_UP:
                elis_snake.change_direction("UP")
            elif event.key == pygame.K_DOWN:
                elis_snake.change_direction("DOWN")
    elis_snake.move()
    pygame.display.update()
