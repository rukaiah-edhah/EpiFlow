import os
import pygame
import random
from simulation_manager import SimulationManager

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 2000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Virus Simulation Game")

# Font for instructions
font = pygame.font.Font(None, 36)  
instruction_text = font.render("Press SPACE to run the simulation and Q to quit", True, (255, 255, 255))  
text_rect = instruction_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Assets directory
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "Assets")

# Verify Assets directory exists
if not os.path.exists(ASSETS_DIR):
    print(f"Error: Assets directory not found at {ASSETS_DIR}")
    exit()

# Load background image
background_image_path = os.path.join(ASSETS_DIR, "EpiFlow_Background.jpg")
background_image = pygame.image.load(background_image_path)
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Load and scale agent images
healthy_images = [
    pygame.image.load(os.path.join(ASSETS_DIR, f"Untitled_Artwork_{i}.png"))
    for i in range(8)
]
agent_radius = 20
healthy_images = [
    pygame.transform.scale(image, (2 * agent_radius, 2 * agent_radius))
    for image in healthy_images
]

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)

# Game loop variables
RUNNING = False
PAUSED = False
speed = 1  # Default speed

# Main game loop
running = True
simulation = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                num_agents = 120
                grid_size = 100
                simulation = SimulationManager(num_agents, grid_size, healthy_images)
                num_infected = max(1, num_agents // 10)  
                initial_infected_agents = random.sample(simulation.agents, num_infected)
                for agent in initial_infected_agents:
                    agent.infect()
                
                RUNNING = True
                PAUSED = False
            elif event.key == pygame.K_p:
                PAUSED = not PAUSED
            elif event.key == pygame.K_q:
                running = False
            
    screen.blit(instruction_text, text_rect)

    if RUNNING and not PAUSED and simulation:
        screen.blit(background_image, (0, 0))
        simulation.update_status()

        for agent in simulation.agents:
            x, y = agent.pos[0] * 20, agent.pos[1] * 10
            screen.blit(agent.image, (x - agent_radius, y - agent_radius))

            if agent.status == "infected":
                status_color = RED
            elif agent.status == "recovered":
                status_color = GREEN
            else:
                status_color = ORANGE

            pygame.draw.circle(screen, status_color, (x, y), agent_radius + 2, 2)

            # Health bar
            health_bar_length = 30
            health_bar_height = 5
            health_bar_x = x - health_bar_length // 2
            health_bar_y = y - agent_radius - 10
            pygame.draw.rect(screen, RED, (health_bar_x, health_bar_y, health_bar_length, health_bar_height))
            pygame.draw.rect(screen, GREEN, (health_bar_x, health_bar_y, int(health_bar_length * agent.health / 100), health_bar_height))

    pygame.display.flip()
    pygame.time.Clock().tick(30 * speed)

pygame.quit()