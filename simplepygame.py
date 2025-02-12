import pygame
import random

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 500, 600
PLAYER_SIZE = 50
OBSTACLE_SIZE = 50
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 0, 255)
SPEED = 5

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Blocks!")

# Player setup
player = pygame.Rect(WIDTH//2, HEIGHT - 2*PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE)

# Obstacle setup
obstacles = []
def create_obstacle():
    x_pos = random.randint(0, WIDTH - OBSTACLE_SIZE)
    obstacles.append(pygame.Rect(x_pos, 0, OBSTACLE_SIZE, OBSTACLE_SIZE))

# Game loop variables
clock = pygame.time.Clock()
running = True
score = 0

while running:
    clock.tick(30)
    screen.fill(WHITE)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= SPEED
    if keys[pygame.K_RIGHT] and player.x < WIDTH - PLAYER_SIZE:
        player.x += SPEED
    
    # Create obstacles
    if random.randint(1, 30) == 1:
        create_obstacle()
    
    # Move obstacles
    for obstacle in obstacles[:]:
        obstacle.y += SPEED
        if obstacle.y > HEIGHT:
            obstacles.remove(obstacle)
            score += 1
        if player.colliderect(obstacle):
            running = False
    
    # Draw player
    pygame.draw.rect(screen, BLUE, player)
    
    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)
    
    # Update display
    pygame.display.flip()

print(f"Game Over! Your score: {score}")
pygame.quit()
