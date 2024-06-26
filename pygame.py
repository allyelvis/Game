import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Simple Car Racing Game')

# Clock to control the frame rate
clock = pygame.time.Clock()

# Load car image
car_img = pygame.image.load('car.png')
car_width = car_img.get_width()

def draw_car(x, y):
    screen.blit(car_img, (x, y))

def draw_obstacles(obstacles):
    for obstacle in obstacles:
        pygame.draw.rect(screen, BLACK, obstacle)

def create_obstacle():
    obstacle_x = random.randint(0, SCREEN_WIDTH - 50)
    obstacle_y = -100
    return pygame.Rect(obstacle_x, obstacle_y, 50, 100)

def game_loop():
    x = SCREEN_WIDTH * 0.45
    y = SCREEN_HEIGHT * 0.8
    x_change = 0

    obstacles = [create_obstacle()]
    score = 0
    speed = 5

    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        screen.fill(WHITE)

        for obstacle in obstacles:
            obstacle.y += speed
            if obstacle.y > SCREEN_HEIGHT:
                obstacles.remove(obstacle)
                obstacles.append(create_obstacle())
                score += 1
                speed += 0.5

        draw_obstacles(obstacles)
        draw_car(x, y)

        for obstacle in obstacles:
            if y < obstacle.y + obstacle.height:
                if x > obstacle.x and x < obstacle.x + obstacle.width or x + car_width > obstacle.x and x + car_width < obstacle.x + obstacle.width:
                    font = pygame.font.SysFont(None, 75)
                    text = font.render("You
