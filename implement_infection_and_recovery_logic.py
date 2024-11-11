import random
import math

class agent:
    def __init__(self, x, y, infected=False):
        self.x = x
        self.y = y
        self.infected = infected
        self.recovery_chance = 0.1  # 10% chance to recover each step

class simulationManager:
    def __init__(self, agents, infection_radius=1.5, infection_chance=0.5):
        self.agents = agents
        self.infection_radius = infection_radius  # distance threshold for infection spread
        self.infection_chance = infection_chance  # probability of infection on proximity
    
    def infection_spread(self):
        """spread infection based on proximity and infection chance."""
        for agent in self.agents:
            if agent.infected:
                for other_agent in self.agents:
                    if not other_agent.infected:
                        distance = math.sqrt((agent.x - other_agent.x)**2 + (agent.y - other_agent.y)**2)
                        if distance <= self.infection_radius:
                            if random.random() < self.infection_chance:
                                other_agent.infected = True

    def recovery(self):
        """recover infected agents based on a random chance."""
        for agent in self.agents:
            if agent.infected and random.random() < agent.recovery_chance:
                agent.infected = False

# example usage
agents = [Agent(random.uniform(0, 10), random.uniform(0, 10), infected=(i == 0)) for i in range(10)]
sim_manager = simulationmanager(agents)

# simulate infection spread and recovery
for _ in range(10):  # run 10 simulation steps
    sim_manager.infection_spread()
    sim_manager.recovery()
