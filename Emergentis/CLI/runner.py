import time
import os
from Core.engine import Engine

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def display(engine):
    print(f"Generation: {engine.generation}")
    print("-" * engine.grid.width)

    for row in engine.grid.cells:
        print("".join("█" if cell else " " for cell in row))

    print("-" * engine.grid.width)

def run(steps=100, delay=0.2):
    """
    Controlled simulation run
    steps = number of generations
    delay = speed of simulation
    """
    engine = Engine()

    for _ in range(steps):  # ✅ controlled iteration
        clear()
        display(engine)
        engine.step()
        time.sleep(delay)

    print("\nSimulation complete.")