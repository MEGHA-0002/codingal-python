# Import pygame
import pygame

# Initialize pygame
pygame.init()

# Create game window
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Custom Event Example")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Create two sprite rectangles
sprite1 = pygame.Rect(150, 150, 80, 80)
sprite2 = pygame.Rect(350, 150, 80, 80)

# Initial colors
sprite1_color = BLUE
sprite2_color = RED

# Create a custom event
CHANGE_COLOR = pygame.USEREVENT + 1

# Set timer for the custom event (every 2 seconds)
pygame.time.set_timer(CHANGE_COLOR, 2000)

running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Handle custom event
        if event.type == CHANGE_COLOR:
            if sprite1_color == BLUE:
                sprite1_color = GREEN
                sprite2_color = YELLOW
            else:
                sprite1_color = BLUE
                sprite2_color = RED

    # Fill background
    screen.fill(WHITE)

    # Draw sprites
    pygame.draw.rect(screen, sprite1_color, sprite1)
    pygame.draw.rect(screen, sprite2_color, sprite2)

    # Update display
    pygame.display.flip()

# Quit pygame
pygame.quit()