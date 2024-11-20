import os
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 2000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Virus Simulation Game")

# Assets directory
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "Assets")

# Verify Assets directory exists
if not os.path.exists(ASSETS_DIR):
    print(f"Error: Assets directory not found at {ASSETS_DIR}")
    exit()

# Define the path to the background image
background_image_path = os.path.join(ASSETS_DIR, "EpiFlow_Background.jpg")

# Check if the file exists
if not os.path.isfile(background_image_path):
    print(f"Error: File not found at {background_image_path}")
    exit()

# Load the background image
background_image = pygame.image.load(background_image_path)
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Load and scale agent images
healthy_images = [
    pygame.image.load(os.path.join(ASSETS_DIR, f"Untitled_Artwork_{i}.png"))
    for i in range(8)  # Assumes images are named sequentially
]

agent_radius = 40

healthy_images = [
    pygame.transform.scale(image, (2 * agent_radius, 2 * agent_radius))
    for image in healthy_images
]

# Game loop variables
RUNNING = False
PAUSED = False

# Agent class for visuals
class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = random.choice([-2, -1, 1, 2])
        self.dy = random.choice([-2, -1, 1, 2])
        self.image = random.choice(healthy_images)

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Bounce off walls
        if self.x - agent_radius < 0 or self.x + agent_radius > WIDTH:
            self.dx *= -1
        if self.y - agent_radius < 0 or self.y + agent_radius > HEIGHT:
            self.dy *= -1

    def draw(self, surface):
        surface.blit(self.image, (self.x - agent_radius, self.y - agent_radius))

# Main game loop
running = True
agents = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Initialize agents for the simulation
                agents = [Agent(random.randint(40, WIDTH - 40), random.randint(40, HEIGHT - 40)) for _ in range(80)]
                RUNNING = True
                PAUSED = False
            elif event.key == pygame.K_p:
                PAUSED = not PAUSED
            elif event.key == pygame.K_q:
                running = False

    # Display background and agents if running
    if RUNNING and not PAUSED:
        screen.blit(background_image, (0, 0))
        for agent in agents:
            agent.move()
            agent.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
