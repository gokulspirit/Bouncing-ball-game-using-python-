# Ball Bounce Simulation using Pygame
# 5 balls bounce under gravity with elastic collision

import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set up screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Bounce Simulation")

# Load background and ball image
background = pygame.image.load("background.jpeg")
ball_img_original = pygame.image.load("Ball.jpeg")
ball_img = pygame.transform.scale(ball_img_original, (32, 32))  # Resize to 32x32 pixels

# Define Ball class
class Ball:
    gravity = 1  # Gravity acceleration

    def __init__(self):
        self.image = ball_img
        self.x = random.randint(0, WIDTH - 32)
        self.y = random.randint(0, 300)
        self.vx = random.choice([-4, 4])  # Random horizontal direction
        self.vy = random.randint(2, 6)

    def render(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        # Apply gravity
        self.vy += Ball.gravity

        # Update position
        self.x += self.vx
        self.y += self.vy

        # Collision with vertical walls
        if self.x <= 0 or self.x >= WIDTH - 32:
            self.vx *= -1

        # Collision with top
        if self.y <= 0 and self.vy < 0:
            self.vy *= -1
            self.y = 0

        # Collision with bottom
        if self.y >= HEIGHT - 32 and self.vy > 0:
            self.vy *= -1
            self.y = HEIGHT - 32

# Create multiple balls
balls = [Ball() for _ in range(5)]

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for ball in balls:
        ball.move()
        ball.render()

    pygame.display.update()
    clock.tick(60)  # Run at 60 FPS

# Quit pygame
pygame.quit()
