import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Paddle and ball
paddle_width, paddle_height = 15, 100
ball_size = 15

# Paddle A
paddle_a = pygame.Rect(50, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)

# Paddle B
paddle_b = pygame.Rect(WIDTH - 50 - paddle_width, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)