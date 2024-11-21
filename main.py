import pygame
from simulation_manager import SimulationManager
from ui_rendering import *

# pygame setup 
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("EpiFlow - Virus Spread Simulation")

num_agents = 100
grid_size = 50
sim_manager = SimulationManager(num_agents, grid_size)

RUNNING = False
PAUSED = False

def controls():
    """display controls"""
    control_text = small_font.render("Controls: [S] Start  [P] Pause  [Q] Quit", True, WHITE)
    screen.blit(control_text, (10, HEIGHT - 30))
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # We will render our simulator here 
def run_simulation():
    global RUNNING, PAUSED

    running = True
    while running:
        for event in pygame.event.get():
        # pygame.QUIT event means the user clicked X to close the window
            if event.type == pygame.QUIT:
                running = False
        # key pressed sim control
            if event.type == pygame.K_SPACE:
                RUNNING = True
                PAUSED = False
            elif event.type == pygame.K_s:
                RUNNING = True
                PAUSED = False
            elif event.type == pygame.K_p:
                PAUSED = not PAUSED
            elif event.type == pygame.K_q:
                running = False
        if not RUNNING:
            # displays main menu
            main_menu()
            continue

        if not PAUSED:
            # updates: move agents, check infection and recover
            sim_manager.update_status()

            render_simulation(sim_manager.agents)
            feedback(f"Infected agents: {len([a for a in sim_manager.agents if a.status == 'infected'])}")
        else: 
            feedback("simulation paused")
        # displats controls
        controls()
    # flip() the display to put our work on screen
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
run_simulation()