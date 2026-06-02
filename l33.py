# =====================================
# ACTIVITY 65: Create a Basic Pygame Window
# =====================================

import pygame

# Initialize pygame
pygame.init()

# Setup window
screen = pygame.display.set_mode((400, 500))
pygame.display.set_caption("Basic Pygame Window")

done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()

pygame.quit()


# =====================================
# ACTIVITY 66: Add Background Image, Sprite and Text
# =====================================

import pygame

# Initialize Pygame
pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# Create display surface
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Adding Image and Background")

# Load images
background_image = pygame.transform.scale(
    pygame.image.load("background.png").convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

penguin_image = pygame.transform.scale(
    pygame.image.load("penguin.png").convert_alpha(),
    (200, 200)
)

penguin_rect = penguin_image.get_rect(
    center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30)
)

# Create text
font = pygame.font.Font(None, 36)
text = font.render("Hello World", True, pygame.Color("black"))

text_rect = text.get_rect(
    center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110)
)

# Game Loop
clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.blit(background_image, (0, 0))
    display_surface.blit(penguin_image, penguin_rect)
    display_surface.blit(text, text_rect)

    pygame.display.update()
    clock.tick(30)

pygame.quit()