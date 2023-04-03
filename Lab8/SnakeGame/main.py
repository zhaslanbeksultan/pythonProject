import pygame
import time
import random

pygame.init()
# colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Basic sets
dis = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

# Initial length of a snake
snake_block = 10

# font sets
font_style = pygame.font.SysFont("bahnschrift", 30)
score_font = pygame.font.SysFont("comicsansms", 35)


# Score and Level message
def Your_score(score, level):
    value = score_font.render(" Your Score: " + str(score) + "  Level: " + str(level), True, yellow)
    dis.blit(value, [0, 0])


# Draw a snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])


# Message to User
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [200 / 6, 400 / 3])

# The main game loop
def gameLoop():
    game_over = False
    game_close = False

    # Initial position of a snake
    x1 = 600 / 2
    y1 = 400 / 2

    # Change in position
    x1_change = 0
    y1_change = 0

    # Speed, Length, level of a snake
    snake_speed = 10
    snake_List = []
    Length_of_snake = 1
    level = 1

    # Random position for the food
    foodx = round(random.randrange(0, 600 - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, 400 - snake_block) / 10.0) * 10.0

    while not game_over:
        # Level Increasing depending on length of a snake
        if Length_of_snake == 5:
            level = 2
            snake_speed = 12
        if Length_of_snake == 10:
            level = 3
            snake_speed = 15
        if Length_of_snake == 15:
            level = 4
            snake_speed = 17
        while game_close == True:
            dis.fill(black)
            # Message to User if he lost the game
            message("You Lost! Press C-Play Again or Q-Quit", red)

            Your_score(Length_of_snake - 1, level)
            pygame.display.update()

            # Checking for keydown event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        # Checking for wall collision
        if x1 >= 600 or x1 < 0 or y1 >= 400 or y1 < 0:
            game_close = True
        # Position change
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        # Draw the food
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        # Snake movement
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Checking for collision of snake by himself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1, level)

        pygame.display.update()

        # Generating random position for food, so that it does not fall on a wall or a snake
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, 600 - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, 400 - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
