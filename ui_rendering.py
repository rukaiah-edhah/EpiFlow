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
    pygame.transform.scale(image, (2 * agent_radius, 2 * agent_radius))
    for image in healthy_images
]

#Draw health bar
        pygame.draw.rect(surface, RED, (self.x - 15, self.y - 30, 30, 5))  # Red background
        pygame.draw.rect(surface, GREEN, (self.x - 15, self.y - 30, 30 * (self.health / 100), 5))  # Green health bar
        surface.blit(self.image, (self.x - agent_radius, self.y - agent_radius))

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

        #feedback message
        feedback(f"Simulation Running: {len([a for a in agents if a.infected])} Infected")

    else:
        feedback("Simulation Paused")

    #Display controls
    controls()

    #Update the display
    pygame.display.flip()


        
