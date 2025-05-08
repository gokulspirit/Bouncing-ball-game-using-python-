# This program shows the simulation of 5 balls bouncing under gravitational acceleration.
# It is also accompanied by elastic collision with the walls of the container.
# It is fun to watch.

import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Setting screen size
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('Background.jpeg')

# Adding title
pygame.display.set_caption('Ball Bounce Simulation')

# Ball class definition
class Ball:
    ball_image = pygame.image.load('Ball.jpeg')
    g = 1  # Gravitational acceleration

    def __init__(self):
        self.velocityX = 4
        self.velocityY = 4
        self.X = random.randint(0, 768)
        self.Y = random.randint(0, 350)

    def render_ball(self):
        screen.blit(Ball.ball_image, (self.X, self.Y))

    def move_ball(self):
        # Apply gravity
        self.velocityY += Ball.g

        # Update position
        self.X += self.velocityX
        self.Y += self.velocityY

        # Collision with walls
        if self.X < 0 or self.X > 768:
            self.velocityX *= -1

        if self.Y < 0 and self.velocityY < 0:
            self.velocityY *= -1
            self.Y = 0

        if self.Y > 568 and self.velocityY > 0:
            self.velocityY *= -1
            self.Y = 568

# Create a list of 5 ball objects
Ball_List = [Ball() for _ in range(5)]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time.sleep(0.02)
    screen.blit(background, (0, 0))

    for ball_item in Ball_List:
        ball_item.render_ball()
        ball_item.move_ball()

    pygame.display.update()
