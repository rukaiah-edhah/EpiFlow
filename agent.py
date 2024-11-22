import random

class Agent:
    def __init__(self, x, y, image):

        # position
        self.pos = (x,y) 

        # status with initial value of susceptible. 
        self.status = "susceptible" 

        self.health = 100
        self.image = image
    
    def move(self, gridSize):
        # move the agent to a random position within the grid
        dx, dy = random.uniform(-1.2, 1.2), random.uniform(-1.2, 1.2)
        newX = max(0, min(self.pos[0]+dx, gridSize - 1))
        newY = max(0, min(self.pos[1]+dy, gridSize - 1))
        self.pos = (newX, newY)

    def infect(self):
        # changes status to infeceted.
        if self.status == "susceptible":
            self.status = "infected"
            self.health = 80
    
    def recover(self):
        if self.status == "infected":
            self.status = "recovered"
            self.health = 100

    def update_health(self):
        if self.status == "infected":
            self.health -= 1
            if self.health <= 0:
                self.recover()
