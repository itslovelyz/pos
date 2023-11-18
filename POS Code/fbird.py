import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

# Set bird dimensions
BIRD_WIDTH = 50
BIRD_HEIGHT = 50

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set window title
pygame.display.set_caption("Flappy Bird")

# Create a bird object
bird = pygame.image.load("https://e7.pngegg.com/pngimages/948/516/png-clipart-flappy-bird-pixel-art-minecraft-flappy-bird-sprite-game-text-thumbnail.png")
bird_rect = bird.get_rect(center=(100, 100))

# Create a pipe object
pipe = pygame.image.load("https://upload.wikimedia.org/wikipedia/commons/9/93/Mario_pipe.png")
pipe_rect = pipe.get_rect(midtop=(SCREEN_WIDTH + 100, random.randint(0, SCREEN_HEIGHT - 200)))

# Initialize game variables
clock = pygame.time.Clock()
score = 0
done = False

def game_loop():
    global clock, score, done

    while not done:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Update game state
        clock.tick(60)
        score += 1

        # Move the bird based on user input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            bird_rect.centery -= 5

        # Check for collisions with pipes
        if pipe_rect.colliderect(bird_rect):
            done = True

        # Check if the bird has flown beyond the screen
        if bird_rect.centery < -BIRD_HEIGHT or bird_rect.centery > SCREEN_HEIGHT:
            done = True

        # Update pipe position
        pipe_rect.centerx -= 5

        # If the pipe has moved beyond the screen, move it back to the right and change its height
        if pipe_rect.right < 0:
            pipe_rect.left = SCREEN_WIDTH
            pipe_rect.centery = random.randint(0, SCREEN_HEIGHT - 200)

        # Draw the scene
        screen.fill(WHITE)
        screen.blit(bird, bird_rect)
        screen.blit(pipe, pipe_rect)

        # Update the display
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game_loop()