import os
import pygame
import random

#Initialize Pygame
pygame.init()


#Screen dimensions
WIDTH, HEIGHT = 2000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Virus Simulation Game")



ASSETS_DIR = os.path.join(os.path.dirname(__file__), "Assets")

#Verify Assets directory exists
if not os.path.exists(ASSETS_DIR):
    print(f"Error: Assets directory not found at {ASSETS_DIR}")
    exit()

#Define the path to the background image
background_image_path = os.path.join(ASSETS_DIR, "EpiFlow_Background.jpg")

#Debug: Print the path
print(f"Loading background image from: {background_image_path}")

#Check if the file exists
if not os.path.isfile(background_image_path):
    print(f"Error: File not found at {background_image_path}")
    exit()

#Load the background
background_image = pygame.image.load(background_image_path)
background_image = pygame.transform.scale(background_image, (2000, 1000))


#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

#Load and scale images
healthy_images = [
    pygame.image.load(os.path.join(ASSETS_DIR, f"Untitled_Artwork_{i}.png"))
    for i in range(8)  #Assumes images are named sequentially
]

agent_radius = 40

healthy_images = [
    pygame.transform.scale(image, (2 * agent_radius, 2 * agent_radius))
    for image in healthy_images
]

#Clock for controlling FPS
clock = pygame.time.Clock()
FPS = 60

#Fonts
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 28)

#Game states
RUNNING = False
PAUSED = False

#Simulation variables
agents = []
agent_count = 80
infected_percentage = 0.2


class Agent:
    def __init__(self, x, y, infected=False):
        self.x = x
        self.y = y
        self.dx = random.choice([-2, -1, 1, 2])
        self.dy = random.choice([-2, -1, 1, 2])
        self.infected = infected
        self.health = 100  #Health percentage
        self.image = random.choice(healthy_images)

    def move(self):
        self.x += self.dx
        self.y += self.dy

        #Bounce off walls
        if self.x - agent_radius < 0 or self.x + agent_radius > WIDTH:
            self.dx *= -1
        if self.y - agent_radius < 0 or self.y + agent_radius > HEIGHT:
            self.dy *= -1

    def draw(self, surface):
        #Draw health bar
        pygame.draw.rect(surface, RED, (self.x - 15, self.y - 30, 30, 5))  #Red background
        pygame.draw.rect(surface, GREEN, (self.x - 15, self.y - 30, 30 * (self.health / 100), 5))  #Green health bar
        surface.blit(self.image, (self.x - agent_radius, self.y - agent_radius))


def main_menu():
    """Display the main menu."""
    screen.fill(BLACK)
    title_text = font.render("EpiFlow", True, WHITE)
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


def setup_simulation():
    """Initialize agents for the simulation."""
    global agents
    agents = []
    for _ in range(agent_count):
        x = random.randint(agent_radius, WIDTH - agent_radius)
        y = random.randint(agent_radius, HEIGHT - agent_radius)
        infected = random.random() < infected_percentage
        agents.append(Agent(x, y, infected))


#Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Handle keypresses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                setup_simulation()
                RUNNING = True
                PAUSED = False
            elif event.key == pygame.K_s:
                RUNNING = True
                PAUSED = False
            elif event.key == pygame.K_p:
                PAUSED = not PAUSED
            elif event.key == pygame.K_q:
                running = False

    #Display main menu if not running
    if not RUNNING:
        main_menu()
        continue

    #Run simulation if not paused
    if not PAUSED:
        screen.blit(background_image, (0, 0))

        #Update and draw agents
        for agent in agents:
            agent.move()
            agent.draw(screen)

        #Feedback message
        feedback(f"Simulation Running: {len([a for a in agents if a.infected])} Infected")

    else:
        feedback("Simulation Paused")

    #Display controls
    controls()

    #Update the display
    pygame.display.flip()

    #Cap the frame rate
    clock.tick(FPS)

pygame.quit()
