import random
from agent import Agent

class SimulationManager:
    def __init__(self, num_agents, grid_size, images):
        self.agents = []
        for _ in range(num_agents):
            x = random.randint(0, grid_size - 1)
            y = random.randint(0, grid_size - 1)
            image = random.choice(images)
            self.agents.append(Agent(x, y, image))
        self.grid_size = grid_size
        self.time_step = 0
    
    def update_status(self):
        self.time_step += 1
        for agent in self.agents:
            agent.move(self.grid_size)  
            
            if agent.status == "infected":
                self.handle_collision(agent) 
                agent.update_health()       
            
            self.handle_recovery(agent)    

    def handle_collision(self, infected_agent):
        for other_agent in self.agents:
            if other_agent != infected_agent and other_agent.status == "susceptible":
                if self.is_near(infected_agent, other_agent): 
                    if random.random() < 0.9:  
                        other_agent.infect()  

    def handle_recovery(self, agent):
        if agent.status == "infected" and agent.health <= 0:
            agent.recover()  

    def is_near(self, agent1, agent2):
        distance = (agent1.pos[0] - agent2.pos[0]) ** 2 + (agent1.pos[1] - agent2.pos[1]) ** 2
        return distance <= 1 

    def run_simulation(self, steps):
        for _ in range(steps):
            self.time_step += 1
            self.update_status()

    def get_statistics(self):
        susceptible = sum(1 for agent in self.agents if agent.status == "susceptible")
        infected = sum(1 for agent in self.agents if agent.status == "infected")
        recovered = sum(1 for agent in self.agents if agent.status == "recovered")
        return susceptible, infected, recovered