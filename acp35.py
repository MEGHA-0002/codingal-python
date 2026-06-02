# Import pygame library
import pygame

# Initialize pygame
pygame.init()

# Create game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sprites Movement")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Sprite 1 (movable)
sprite1 = pygame.Rect(100, 100, 50, 50)

# Sprite 2 (static)
sprite2 = pygame.Rect(400, 300, 50, 50)

# Movement speed
speed = 5

# Game loop
running = True
while running:
    
    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key controls
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        sprite1.x -= speed

    if keys[pygame.K_RIGHT]:
        sprite1.x += speed

    if keys[pygame.K_UP]:
        sprite1.y -= speed

    if keys[pygame.K_DOWN]:
        sprite1.y += speed

    # Fill background
    screen.fill(WHITE)

    # Draw sprites
    pygame.draw.rect(screen, BLUE, sprite1)
    pygame.draw.rect(screen, RED, sprite2)

    # Update display
    pygame.display.update()

# Quit pygame
pygame.quit()