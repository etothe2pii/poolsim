from pool_objects import Ball, Table
import sys

import tkinter as tk

def read_config_file(file) -> list:
    with open(file) as f:
        text = f.readlines()

    text = [t.split() for t in text]

    balls = []
    for t in text:
        if len(t) == 2:
            b = Ball((t[0], t[1]), (0,0))
        elif len(t) == 4:
            b = Ball((t[0], t[1]), (t[2],t[3]))
        else:
            print(f"Invalid config file. Expected 4 fields got {len(t)}", file = sys.stderr)
            sys.exit(1)
        
        balls.append(b)
    
    return balls




class PoolSimApp:
    def __init__(self, root, init_file = None):
        # Create the start button and link it to the stub method
        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(pady=20)

        self.scale_factor = 1000

        if init_file is None:

            self.table = Table([])
        
        else:
            self.table = Table(read_config_file(init_file))
        
        # Create the canvas
        self.canvas = tk.Canvas(root, width=self.table.dimensions[0] * self.scale_factor, height=self.table.dimensions[1] * self.scale_factor, bg="white")
        self.canvas.pack(pady=20)
        
        # Link a click event on the canvas to the canvas_clicked method
        self.canvas.bind("<Button-1>", self.canvas_clicked)

       

        self.time = 0

    def start(self):
        print("Stub method called!")

    def canvas_clicked(self, event):
        print(f"Canvas clicked at {event.x}, {event.y}")
        self.draw_ball(Ball((event.x, event.y), (0,0)))

    def draw_ball(self, ball: Ball):

        pos = ball.get_position(self.time)
        rad = ball.radius * self.scale_factor

        self.canvas.create_oval(pos[0] + rad,  pos[1] + rad, pos[0] - rad, pos[1] - rad)
        


if __name__ == "__main__":
    print(";)")

    root = tk.Tk()
    root.title("Pool Sim")
    app = PoolSimApp(root)
    root.mainloop()