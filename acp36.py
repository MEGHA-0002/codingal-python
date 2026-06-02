# Import pygame library
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

# Create two sprites
sprite1 = pygame.Rect(150, 150, 80, 80)
sprite2 = pygame.Rect(350, 150, 80, 80)

# Initial sprite colors
color1 = BLUE
color2 = RED

# Create a custom event
CHANGE_COLOR = pygame.USEREVENT + 1

# Trigger custom event every 2 seconds (2000 ms)
pygame.time.set_timer(CHANGE_COLOR, 2000)

# Game loop
running = True
while running:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        # Handle custom event
        if event.type == CHANGE_COLOR:
            if color1 == BLUE:
                color1 = GREEN
                color2 = YELLOW
            else:
                color1 = BLUE
                color2 = RED

    # Fill background
    screen.fill(WHITE)

    # Draw sprites
    pygame.draw.rect(screen, color1, sprite1)
    pygame.draw.rect(screen, color2, sprite2)

    # Update display
    pygame.display.update()

# Quit pygame
pygame.quit()