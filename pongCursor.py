"""
Ping-Pong Game
--------------
A classic two-player pong game with paddle controls, ball physics, and score tracking.
Player 1: W (up) / S (down) | Player 2: ↑ (up) / ↓ (down)
"""

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
BALL_SIZE = 15
PADDLE_SPEED = 8
BALL_SPEED_INITIAL = 7
WINNING_SCORE = 5

# Colors (dark theme)
BACKGROUND = (15, 15, 25)
PADDLE_COLOR = (100, 200, 255)
BALL_COLOR = (255, 255, 255)
TEXT_COLOR = (200, 200, 220)
ACCENT_COLOR = (80, 180, 220)


class Paddle:
    """Represents a player's paddle with position and movement logic."""

    def __init__(self, x: int, y: int):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = PADDLE_SPEED

    def move(self, dy: int) -> None:
        """Move paddle vertically, clamping to screen bounds."""
        self.rect.y += dy
        self.rect.y = max(0, min(self.rect.y, HEIGHT - PADDLE_HEIGHT))

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, PADDLE_COLOR, self.rect)
        pygame.draw.rect(surface, ACCENT_COLOR, self.rect, 2)


class Ball:
    """Ball with position, velocity, and collision logic."""

    def __init__(self):
        self.reset()

    def reset(self, direction: int = 1) -> None:
        """Reset ball to center with given horizontal direction (1 or -1)."""
        self.rect = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        self.velocity_x = BALL_SPEED_INITIAL * direction
        self.velocity_y = 0

    def move(self) -> None:
        self.rect.x += int(self.velocity_x)
        self.rect.y += int(self.velocity_y)

    def bounce_wall(self) -> bool:
        """Bounce off top/bottom walls. Returns True if collision occurred."""
        if self.rect.top <= 0:
            self.rect.top = 0
            self.velocity_y = abs(self.velocity_y)
            return True
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.velocity_y = -abs(self.velocity_y)
            return True
        return False

    def collide_paddle(self, paddle: Paddle) -> bool:
        """Bounce off paddle with angle based on hit position. Returns True if collided."""
        if self.rect.colliderect(paddle.rect):
            # Adjust angle based on where ball hits paddle (top = up, bottom = down)
            hit_pos = (self.rect.centery - paddle.rect.top) / PADDLE_HEIGHT
            angle = (hit_pos - 0.5) * 1.5  # -0.75 to 0.75
            speed = (self.velocity_x ** 2 + self.velocity_y ** 2) ** 0.5
            speed = min(speed + 0.5, 14)  # Slight speed increase, cap at 14

            self.velocity_x = -self.velocity_x
            self.velocity_y = angle * speed

            # Prevent sticking: nudge ball out of paddle
            if self.velocity_x > 0:
                self.rect.left = paddle.rect.right + 2
            else:
                self.rect.right = paddle.rect.left - 2

            return True
        return False

    def is_out_left(self) -> bool:
        return self.rect.right < 0

    def is_out_right(self) -> bool:
        return self.rect.left > WIDTH

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.ellipse(surface, BALL_COLOR, self.rect)


class Game:
    """Main game loop and state management."""

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Ping-Pong")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 48)
        self.large_font = pygame.font.Font(None, 72)

        self.paddle1 = Paddle(30, HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.paddle2 = Paddle(WIDTH - 30 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.ball = Ball()

        self.score1 = 0
        self.score2 = 0
        self.reset_delay = 0

    def handle_input(self) -> bool:
        """Process events. Returns False to quit."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.paddle1.move(-self.paddle1.speed)
        if keys[pygame.K_s]:
            self.paddle1.move(self.paddle1.speed)
        if keys[pygame.K_UP]:
            self.paddle2.move(-self.paddle2.speed)
        if keys[pygame.K_DOWN]:
            self.paddle2.move(self.paddle2.speed)

        return True

    def update(self) -> bool:
        """Update game state. Returns False to quit."""
        if self.reset_delay > 0:
            self.reset_delay -= 1
            return True

        self.ball.move()
        self.ball.bounce_wall()

        self.ball.collide_paddle(self.paddle1)
        self.ball.collide_paddle(self.paddle2)

        if self.ball.is_out_left():
            self.score2 += 1
            self.ball.reset(direction=1)
            self.reset_delay = 30

        if self.ball.is_out_right():
            self.score1 += 1
            self.ball.reset(direction=-1)
            self.reset_delay = 30

        return True

    def draw(self) -> None:
        """Render the current frame."""
        self.screen.fill(BACKGROUND)

        # Center line
        for y in range(0, HEIGHT, 30):
            pygame.draw.rect(self.screen, (40, 50, 70), (WIDTH // 2 - 2, y, 4, 15))

        self.paddle1.draw(self.screen)
        self.paddle2.draw(self.screen)
        self.ball.draw(self.screen)

        # Scores
        score1_text = self.font.render(str(self.score1), True, TEXT_COLOR)
        score2_text = self.font.render(str(self.score2), True, TEXT_COLOR)
        self.screen.blit(score1_text, (WIDTH // 4 - score1_text.get_width() // 2, 20))
        self.screen.blit(score2_text, (3 * WIDTH // 4 - score2_text.get_width() // 2, 20))

        # Win message
        if self.score1 >= WINNING_SCORE:
            msg = self.large_font.render("Player 1 Wins!", True, PADDLE_COLOR)
            self.screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2 - 40))
        elif self.score2 >= WINNING_SCORE:
            msg = self.large_font.render("Player 2 Wins!", True, PADDLE_COLOR)
            self.screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2 - 40))

        pygame.display.flip()

    def run(self) -> None:
        """Main game loop."""
        running = True
        while running:
            running = self.handle_input() and self.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
