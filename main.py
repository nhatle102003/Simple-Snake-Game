# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pygame, random

class Snake:
    def __init__(self):
        self.x = 400
        self.y = 400
        self.changex = 0
        self.changey = 0
        self.snakeHead = []
        self.snakeList = []
        self.total = 1
        self.snake_rect = pygame.Rect(self.x, self.y, 40, 40)


    def move_snake(self):
        self.x += snake.changex
        self.y += snake.changey

    def draw_snake(self):
        for body in self.snakeList:
            self.snake_rect = pygame.Rect((body[0] + 60)  , (body[1] + 60) , 40, 40)
            pygame.draw.rect(screen, green, self.snake_rect)

class Fruit:
    def __init__(self):
        self.x = random.randint(0, 790)
        self.y = random.randint(0, 790)
        self.fruit_rect = pygame.Rect(self.x, self.y, 20, 20)

    def draw_fruit(self):
        self.fruit_rect = pygame.Rect(self.x, self.y, 20, 20)
        pygame.draw.rect(screen, red, self.fruit_rect)


pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Snake game')

black = (0,0,0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0,225,0)
white = (225, 225, 225)

clock = pygame.time.Clock()
fruit = Fruit()
snake = Snake()


def gameLoop():

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.changex = -10
                    snake.changey = 0
                elif event.key == pygame.K_RIGHT:
                    snake.changex = 10
                    snake.changey = 0
                elif event.key == pygame.K_UP:
                    snake.changex = 0
                    snake.changey = -10
                elif event.key == pygame.K_DOWN:
                    snake.changex = 0
                    snake.changey = 10


        screen.fill(black)
        fruit.draw_fruit()
        snake.move_snake()

        snake.snakeHead = []
        snake.snakeHead.append(snake.x)
        snake.snakeHead.append(snake.y)
        snake.snakeList.append(snake.snakeHead)
        snake.draw_snake()


        if snake.snake_rect.colliderect(fruit.fruit_rect):
            fruit.x = random.randint(0, 700)
            fruit.y = random.randint(0, 700)
            print("Yummy")
            snake.total += 1

        if len(snake.snakeList) > snake.total:
            del snake.snakeList[0]

        for body in snake.snakeList[:-1]:
            if body == snake.snakeHead:
                game_over = True

        if snake.snakeHead[0] < -40 or snake.snakeHead[0] > 700 or snake.snakeHead[1] < -40 or snake.snakeHead[1] > 700:
            game_over = True

        pygame.display.update()
        clock.tick(10)
        print(snake.snakeHead[0])
        print(snake.snakeHead[1])

    pygame.quit()
    quit()
gameLoop()