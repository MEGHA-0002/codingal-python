import pygame

# Initialize Pygame
pygame.init()

# Create game window
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("My Game Screen")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Font for text
font = pygame.font.Font(None, 36)

# Create text
text = font.render("Welcome to My Game!", True, BLACK)

# Game loop
running = True
while running:
    screen.fill(WHITE)  # Background color

    # Draw rectangle
    pygame.draw.rect(screen, BLUE, (200, 150, 200, 100))

    # Display text
    screen.blit(text, (150, 50))

    pygame.display.update()

    # Check for exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()