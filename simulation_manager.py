import random
from agent import Agent

class SimulationManager:
    def __init__(self, num_agents, grid_size):
        self.agents = []
        for _ in range(num_agents):
            x = random.randint(0, grid_size - 1)
            y = random.randint(0, grid_size - 1)
            self.agents.append(Agent(x, y))
        self.grid_size = grid_size
        self.time_step = 0
    
    def update_status(self):
        for agent in self.agents:
            agent.move(self.grid_size)
            if agent.status == "infected":
                self.handle_collision(agent)  
                self.handle_infection_and_recovery(agent)  

    def handle_collision(self, infected_agent):
        for other_agent in self.agents:
            if other_agent != infected_agent and other_agent.status == "susceptible":
                distance = (infected_agent.pos[0] - other_agent.pos[0]) ** 2 + \
                               (infected_agent.pos[1] - other_agent.pos[1]) ** 2
                if distance <= 1:  
                    other_agent.infect()  

    def handle_recovery(self, agent):
        # Handle recovery only since infection is handled by handle_collision
        # If the agent is infected and the random chance threshold is met, the agent recovers.
        if agent.infected and not agent.recovered:
            if random.random() < self.recovery_chance:
                agent.infected = False
                agent.recovered = True
                print(f"Agent at ({agent.x}, {agent.y}) has recovered.")

    def is_near(self, agent1, agent2):
        distance = (agent1.pos[0] - agent2.pos[0]) ** 2 + (agent1.pos[1] - agent2.pos[1]) ** 2
        return distance <= 1

    def run_simulation(self, steps):
        for _ in range(steps):
            self.time_step += 1
            self.update_status()
