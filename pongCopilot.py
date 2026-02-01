import pygame
import sys
from enum import Enum

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class GameState(Enum):
    RUNNING = 1
    PAUSED = 2
    GAME_OVER = 3

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 15, 100)
        self.speed = 6
    
    def move_up(self):
        if self.rect.top > 0:
            self.rect.y -= self.speed
    
    def move_down(self):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed
    
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 10, 10)
        self.vel_x = -5
        self.vel_y = 5
    
    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        
        # Wall collisions
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.vel_y *= -1
    
    def paddle_collision(self, paddle):
        if self.rect.colliderect(paddle.rect):
            self.vel_x *= -1
            self.rect.x += self.vel_x
    
    def reset(self):
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.vel_x = -5
        self.vel_y = 5
    
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

class PingPongGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Ping Pong")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 74)
        
        self.player1 = Paddle(10, SCREEN_HEIGHT // 2 - 50)
        self.player2 = Paddle(SCREEN_WIDTH - 25, SCREEN_HEIGHT // 2 - 50)
        self.ball = Ball()
        
        self.score1 = 0
        self.score2 = 0
        self.state = GameState.RUNNING
    
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player1.move_up()
        if keys[pygame.K_s]:
            self.player1.move_down()
        if keys[pygame.K_UP]:
            self.player2.move_up()
        if keys[pygame.K_DOWN]:
            self.player2.move_down()
        
        return True
    
    def update(self):
        if self.state != GameState.RUNNING:
            return
        
        self.ball.update()
        self.ball.paddle_collision(self.player1)
        self.ball.paddle_collision(self.player2)
        
        # Score points
        if self.ball.rect.left <= 0:
            self.score2 += 1
            self.ball.reset()
        elif self.ball.rect.right >= SCREEN_WIDTH:
            self.score1 += 1
            self.ball.reset()
    
    def draw(self):
        self.screen.fill(BLACK)
        
        # Draw center line
        for y in range(0, SCREEN_HEIGHT, 20):
            pygame.draw.rect(self.screen, WHITE, (SCREEN_WIDTH // 2 - 2, y, 4, 10))
        
        self.player1.draw(self.screen)
        self.player2.draw(self.screen)
        self.ball.draw(self.screen)
        
        # Draw scores
        score_text = self.font.render(f"{self.score1}  {self.score2}", True, WHITE)
        self.screen.blit(score_text, (SCREEN_WIDTH // 2 - 70, 50))
        
        pygame.display.flip()
    
    def run(self):
        running = True
        while running:
            running = self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = PingPongGame()
    game.run()