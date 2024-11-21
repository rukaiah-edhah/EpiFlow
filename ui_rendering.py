import pygame
import os

pygame.init()

#Screen dimensions
WIDTH, HEIGHT = 2000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Virus Simulation Game")

background_image = pygame.image.load(os.path.join("assets", "EpiFlow_Background.jpg"))
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

healthy_images = [
    pygame.image.load(os.path.join("assets", f"Untitled_Artwork_{i}.png"))
    for i in range(8)  
]

# Scale images
healthy_images = [
    pygame.transform.scale(image, (20, 20))  
    for image in healthy_images
]

# fonts for text rendering
font = pygame.font.Font(None, 75)
small_font = pygame.font.Font(None,36)

def main_menu():
    """Display the main menu."""
    screen.fill(BLACK)
    title_text = font.render("EpiFlow", True, WHITE)
    start_text = font.render("Press SPACE to Start", True, WHITE)

    # Center the text
    title_x = WIDTH // 2 - title_text.get_width() // 2
    title_y = HEIGHT // 2 - 100
    start_x = WIDTH // 2 - start_text.get_width() // 2
    start_y = HEIGHT // 2

    screen.blit(title_text, (title_x, title_y))
    screen.blit(start_text, (start_x, start_y))

    pygame.display.flip()


def controls():
    """Display simulation controls."""
    control_text = small_font.render("Controls: [S] Start  [P] Pause  [Q] Quit", True, WHITE)
    screen.blit(control_text, (10, HEIGHT - 30))


def feedback(message):
    """Display feedback messages."""
    feedback_text = small_font.render(message, True, YELLOW)
    screen.blit(feedback_text, (10, 10))

def render_agents(agents):
    """Render agents"""
    for agent in agents:
        if agent.status == "infected":
            pygame.draw.circle(screen,RED, (agent.pos[0] * 10, agent.pos[1] * 10, 5))
        elif agent.status == "recovered":
            pygame.draw.circle(screen,GREEN, (agent.pos[0] * 10, agent.pos[1] * 10, 5))
        else:
            image = healthy_images[0]
            screen.blit(image, (agent.pos[0] * 10, agent.pos[1] * 10))

#Draw health bar
def draw_health_bar(agent):
    """draw health bar above agent"""
    pygame.draw.rect(screen, RED, (agent.pos[0] * 10 - 15, agent.pos[1] * 10 - 30, 30, 5))  # Red background
    pygame.draw.rect(screen, GREEN, (agent.pos[0] * 10 - 15, agent.pos[1] * 10 - 30, 30 * (agent.health / 100), 5))  # Green health bar

def render_simulation(agents):
    """Render simulation"""
    screen.fill(WHITE)
    render_agents(agents) # renders agents base on status.
    for agent in agents:
        draw_health_bar(agent) # draws health bar above each agent.
        pygame.display.flip()
