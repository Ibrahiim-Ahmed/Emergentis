import sys

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "gui":
        from GUI.app import LifeGUI
        import tkinter as tk

        root = tk.Tk()
        app = LifeGUI(root)
        root.mainloop()
    else:
        from CLI.runner import run
        run(steps=150, delay=0.1)