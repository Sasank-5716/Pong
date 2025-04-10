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

# Ball
ball = pygame.Rect(WIDTH // 2 - ball_size // 2, HEIGHT // 2 - ball_size // 2, ball_size, ball_size)

# Speeds
paddle_speed = 7
ball_speed_x, ball_speed_y = 5, 5

# Scores
score_a, score_b = 0, 0
font = pygame.font.Font(None, 36)

# Game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle_a.top > 0:
        paddle_a.y -= paddle_speed
    if keys[pygame.K_s] and paddle_a.bottom < HEIGHT:
        paddle_a.y += paddle_speed
    if keys[pygame.K_UP] and paddle_b.top > 0:
        paddle_b.y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle_b.bottom < HEIGHT:
        paddle_b.y += paddle_speed

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # Ball collision with top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
    
    # Ball collision with paddles
    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_speed_x *= -1

    # Scoring
    if ball.left <= 0:
        score_b += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x *= -1
    if ball.right >= WIDTH:
        score_a += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x *= -1

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle_a)
    pygame.draw.rect(screen, WHITE, paddle_b)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    
    # Score display
    score_text = font.render(f"{score_a} - {score_b}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))
    
    pygame.display.flip()
    clock.tick(60)