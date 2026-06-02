# =====================================
# ACTIVITY 67: My First Game Screen
# =====================================

import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set window title
pygame.display.set_caption("My First Game Screen")

# Define background color (Sky Blue)
BACKGROUND_COLOR = (135, 206, 235)

# Game loop
running = True

while running:

    # Fill screen with background color
    screen.fill(BACKGROUND_COLOR)

    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update display
    pygame.display.update()

# Quit pygame
pygame.quit()