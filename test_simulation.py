from simulation_manager import SimulationManager

# Parameters to test the logic
num_agents = 5
grid_size = 10

sim_manager = SimulationManager(num_agents, grid_size)

print("Initial agent positions and statuses:")
for agent in sim_manager.agents:
    print(f"Position: {agent.pos}, Status: {agent.status}")

sim_manager.update_status()

print("\nAgent positions after one update:")
for agent in sim_manager.agents:
    print(f"Position: {agent.pos}, Status: {agent.status}")

agent1 = sim_manager.agents[0]
agent2 = sim_manager.agents[1]
print(f"\nIs agent 1 near agent 2? {sim_manager.is_near(agent1, agent2)}")