# Import pygame
import pygame

# Initialize pygame and mixer
pygame.init()
pygame.mixer.init()

# Create game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Level Up Game")

# Load background image
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (800, 600))

# Load and play background music
pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.play(-1)   # -1 means loop forever

# Define colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Create two sprites
sprite1 = pygame.Rect(150, 250, 80, 80)
sprite2 = pygame.Rect(550, 250, 80, 80)

# Sprite colors
sprite1_color = BLUE
sprite2_color = RED

# Create custom event
CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 2000)

running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Change sprite colors every 2 seconds
        if event.type == CHANGE_COLOR:
            if sprite1_color == BLUE:
                sprite1_color = RED
                sprite2_color = BLUE
            else:
                sprite1_color = BLUE
                sprite2_color = RED

    # Draw background image
    screen.blit(background, (0, 0))

    # Draw sprites
    pygame.draw.rect(screen, sprite1_color, sprite1)
    pygame.draw.rect(screen, sprite2_color, sprite2)

    # Update display
    pygame.display.flip()

# Quit pygame
pygame.quit()