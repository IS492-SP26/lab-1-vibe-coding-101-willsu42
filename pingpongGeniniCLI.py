# Pygame Ping-Pong Game
import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ping-Pong")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Game objects
# Paddles
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100
paddle_a = pygame.Rect(50, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_b = pygame.Rect(SCREEN_WIDTH - 50 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball
BALL_RADIUS = 15
ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_RADIUS, SCREEN_HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed_x = 7
ball_speed_y = 7

# Player scores
player_a_score = 0
player_b_score = 0
font = pygame.font.Font(None, 74)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle_a.y -= 10
    if keys[pygame.K_s]:
        paddle_a.y += 10
    if keys[pygame.K_UP]:
        paddle_b.y -= 10
    if keys[pygame.K_DOWN]:
        paddle_b.y += 10

    # Paddle boundaries
    if paddle_a.top < 0:
        paddle_a.top = 0
    if paddle_a.bottom > SCREEN_HEIGHT:
        paddle_a.bottom = SCREEN_HEIGHT
    if paddle_b.top < 0:
        paddle_b.top = 0
    if paddle_b.bottom > SCREEN_HEIGHT:
        paddle_b.bottom = SCREEN_HEIGHT

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with walls
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1
    if ball.left <= 0:
        player_b_score += 1
        ball.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        ball_speed_x *= -1
    if ball.right >= SCREEN_WIDTH:
        player_a_score += 1
        ball.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        ball_speed_x *= -1
        
    # Ball collision with paddles
    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_speed_x *= -1

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle_a)
    pygame.draw.rect(screen, WHITE, paddle_b)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))

    # Display scores
    player_a_text = font.render(str(player_a_score), True, WHITE)
    screen.blit(player_a_text, (SCREEN_WIDTH // 4, 10))
    player_b_text = font.render(str(player_b_score), True, WHITE)
    screen.blit(player_b_text, (SCREEN_WIDTH * 3 // 4, 10))


    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)
