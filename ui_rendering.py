import pygame

pygame.init()

#Screen dimensions
WIDTH, HEIGHT = 2000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Virus Simulation Game")

background_image = pygame.image.load(r"C:\Users\ecarl\Downloads\istockphoto-1364253812-640x640.jpg")
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
    pygame.image.load(r"C:\Users\ecarl\Downloads\drive-download-20241118T171123Z-001\Untitled_Artwork.png"),
    pygame.image.load(r"C:\Users\ecarl\Downloads\drive-download-20241118T171123Z-001\Untitled_Artwork 1.png"),
    pygame.image.load(r"C:\Users\ecarl\Downloads\drive-download-20241118T171123Z-001\Untitled_Artwork 2.png"),
    pygame.image.load(r"C:\Users\ecarl\Downloads\drive-download-20241118T171123Z-001\Untitled_Artwork 3.png"),
    pygame.image.load(r"C:\Users\ecarl\Downloads\drive-download-20241118T171123Z-001\Untitled_Artwork 4.png"),
    pygame.image.load(r"C:\Users\ecarl\Downloads\drive-download-20241118T171123Z-001\Untitled_Artwork 5.png"),
    pygame.image.load(r"C:\Users\ecarl\Downloads\drive-download-20241118T171123Z-001\Untitled_Artwork 6.png"),
    pygame.image.load(r"C:\Users\ecarl\Downloads\drive-download-20241118T171123Z-001\Untitled_Artwork 7.png")
]

healthy_images = [
    pygame.transform.scale(image, (20, 20)) # adjust the agent radius to preferred size (20x20 is just a example size)
    for image in healthy_images
]

# fonts for text rendering
font = pygame.font.Font(None, 75)
small_font = pygame.font.Font(None,36)

def main_menu():
    """Display the main menu."""
    screen.fill(BLACK)
    title_text = font.render("EpiFLow", True, WHITE)
    start_text = font.render("Press SPACE to Start", True, WHITE)

    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - 50))
    screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 + 10))

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
    pygame.draw.rect(screen, RED, (agent.x - 15, agent.y - 30, 30, 5))  # Red background
    pygame.draw.rect(screen, GREEN, (agent.x - 15, agent.y - 30, 30 * (agent.health / 100), 5))  # Green health bar

def render_simulation(agents):
    """Render simulation"""
    screen.fill(WHITE)
    render_agents(agents) # renders agents base on status.
    for agent in agents:
        draw_health_bar(agent) # draws health bar above each agent.
        pygame.display.flip()
