import random
class Agent:
    def __init__(self, x,y):

        # position
        self.pos = (x,y) 

        # status with initial value of susceptible. other possible values: infected, and recovered.
        self.status = "susceptible" 
    
    def move(self, gridSize):
        # move the agent to a random position within the grid
        dx, dy = random.choice([-1,0,1]), random.choice([-1,0,1])
        newX = max(0, min(self.pos[0]+dx, gridSize - 1))
        newY = max(0, min(self.pos[1]+dy, gridSize - 1))
        self.pos = (newX + newY)

    def infect(self):
        # changes status to infeceted.
        if self.status == "susceptible":
            self.status = "infected"
    
