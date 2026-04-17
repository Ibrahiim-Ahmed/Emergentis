import tkinter as tk
from Core.engine import Engine
from Experiments.patterns import PATTERNS
from Experiments.metrics import Metrics

CELL_SIZE = 15

class LifeGUI:
    def __init__(self, root):
        self.root = root
        self.engine = Engine(40, 25)
        self.running = False
        self.speed = 100  # milliseconds
        self.stats_label = tk.Label(root, text="Population: 0", fg="white", bg="black")
        self.stats_label.pack()
        # Canvas
        self.canvas = tk.Canvas(
            root,
            width=self.engine.grid.width * CELL_SIZE,
            height=self.engine.grid.height * CELL_SIZE,
            bg="black"
        )
        self.canvas.pack()
                # Controls frame
        controls = tk.Frame(root)
        controls.pack()

        self.start_btn = tk.Button(controls, text="Start", command=self.toggle)
        self.start_btn.pack(side="left")

        tk.Button(controls, text="Reset", command=self.reset).pack(side="left")
        # Pattern selection
        self.pattern_var = tk.StringVar(value="glider")

        pattern_menu = tk.OptionMenu(controls, self.pattern_var, *PATTERNS.keys())
        pattern_menu.pack(side="left")

        tk.Button(controls, text="Add Pattern", command=self.add_pattern).pack(side="left")

        self.speed_slider = tk.Scale(
            controls,
            from_=10,
            to=500,
            orient="horizontal",
            label="Speed (ms)",
            command=self.set_speed
        )
        self.speed_slider.set(self.speed)
        self.speed_slider.pack(side="left")

        # Mouse interaction
        self.canvas.bind("<Button-1>", self.toggle_cell)

        # Keyboard (still useful)
        self.root.bind("<space>", self.toggle)
        self.root.bind("r", self.reset)

        self.draw()
        self.loop()

    def draw(self):
        self.canvas.delete("all")

        for i in range(self.engine.grid.height):
            for j in range(self.engine.grid.width):
                if self.engine.grid.cells[i][j]:
                    self.canvas.create_rectangle(
                        j * CELL_SIZE,
                        i * CELL_SIZE,
                        (j + 1) * CELL_SIZE,
                        (i + 1) * CELL_SIZE,
                        fill="lime",
                        outline=""
                    )
    def add_pattern(self):
        pattern_name = self.pattern_var.get()
        pattern = PATTERNS[pattern_name]

    # Insert in center
        x = self.engine.grid.height // 2
        y = self.engine.grid.width // 2

        self.engine.insert_pattern(pattern, x, y)
        self.draw()
    def loop(self):
        """Continuous simulation loop (ITERATION ENGINE)"""
        if self.running:
            self.engine.step()
            self.draw()

        self.root.after(self.speed, self.loop)
        population = Metrics.population(self.engine.grid)
        self.stats_label.config(
        text=f"Gen: {self.engine.generation} | Population: {population}")
        
    def toggle(self, event=None):
        self.running = not self.running
        self.start_btn.config(text="Pause" if self.running else "Start")

    def reset(self, event=None):
        self.engine = Engine(40, 25)
        self.draw()

    def set_speed(self, val):
        self.speed = int(val)

    def toggle_cell(self, event):
        """
        Mouse interaction:
        Convert click position → grid cell
        """
        x = event.y // CELL_SIZE
        y = event.x // CELL_SIZE

        current = self.engine.grid.get(x, y)
        self.engine.grid.set(x, y, 0 if current else 1)

        self.draw()

root = tk.Tk()
root.title("Emergentis - Interactive Cellular Lab")

app = LifeGUI(root)
root.mainloop()