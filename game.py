import pygame
import random
import sys
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Snake AI (Final Optimized)")

clock = pygame.time.Clock()

# Colors
WHITE = (240, 240, 240)
GREEN = (0, 200, 0)
DARK = (0, 120, 0)
RED = (220, 0, 0)
BLACK = (0, 0, 0)

NUM_AGENTS = 10
font = pygame.font.SysFont(None, 26)


def draw_cube(x, y, color):
    pygame.draw.rect(screen, color, (x, y, CELL, CELL))
    pygame.draw.rect(screen, BLACK, (x, y, CELL, CELL), 1)


class Worm:
    def __init__(self):
        self.reset()

    def reset(self):
        x = random.randint(5, (WIDTH // CELL) - 5) * CELL
        y = random.randint(5, (HEIGHT // CELL) - 5) * CELL

        self.body = [(x, y), (x - CELL, y), (x - 2 * CELL, y), (x - 3 * CELL, y)]
        self.food = self.spawn_food()

        self.prev_head = self.body[0]
        self.reward = 0.0

    def spawn_food(self):
        return (
            random.randint(0, (WIDTH // CELL) - 1) * CELL,
            random.randint(0, (HEIGHT // CELL) - 1) * CELL
        )

    def move(self):
        hx, hy = self.body[0]
        fx, fy = self.food

        dx = fx - hx
        dy = fy - hy

        # AI direction
        if abs(dx) > abs(dy):
            step = (CELL if dx > 0 else -CELL, 0)
        else:
            step = (0, CELL if dy > 0 else -CELL)

        new_head = (hx + step[0], hy + step[1])

        # 🔥 REWARD CALCULATION

        # Distance improvement
        prev_dist = math.hypot(self.food[0] - self.prev_head[0],
                               self.food[1] - self.prev_head[1])

        new_dist = math.hypot(self.food[0] - new_head[0],
                              self.food[1] - new_head[1])

        velocity_reward = max(0, min(1, (prev_dist - new_dist) / CELL + 0.5))

        # Direction alignment
        move_vec = (new_head[0] - hx, new_head[1] - hy)
        target_vec = (fx - hx, fy - hy)

        dot = move_vec[0] * target_vec[0] + move_vec[1] * target_vec[1]
        mag1 = math.hypot(*move_vec)
        mag2 = math.hypot(*target_vec)

        if mag1 == 0 or mag2 == 0:
            direction_reward = 0
        else:
            cos_theta = dot / (mag1 * mag2)
            direction_reward = max(0, min(1, (cos_theta + 1) / 2))

        # 🔥 Improved reward shaping
        step_reward = (velocity_reward * 0.6 + direction_reward * 0.4) * 2

        # Decay-based accumulation (stable)
        self.reward = self.reward * 0.99 + step_reward

        # Cap reward
        self.reward = min(self.reward, 100)

        # Move body
        self.body.insert(0, new_head)

        if new_head == self.food:
            self.food = self.spawn_food()
            self.reward += 20  # strong goal reward
        else:
            self.body.pop()

        self.prev_head = new_head

        # Reset on wall
        if (
            new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT
        ):
            self.reset()

    def draw(self):
        # Head
        hx, hy = self.body[0]
        pygame.draw.circle(screen, DARK, (hx + CELL // 2, hy + CELL // 2), CELL // 2)

        # Body
        for seg in self.body[1:]:
            draw_cube(seg[0], seg[1], GREEN)

        # Food
        pygame.draw.rect(screen, RED, (*self.food, CELL, CELL))


worms = [Worm() for _ in range(NUM_AGENTS)]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)

    total_reward = 0

    for w in worms:
        w.move()
        w.draw()
        total_reward += w.reward

    avg_reward = total_reward / NUM_AGENTS

    # Benchmark scaling
    display_score = int(avg_reward * 8)
    display_score = min(display_score, 800)

    text = font.render(
        f"Agents: 10 | Avg Reward: {display_score} / 800",
        True, BLACK
    )
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(12)
