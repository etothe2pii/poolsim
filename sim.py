from pool_objects import Ball, Table
import sys

def read_config_file(file) -> list[Ball]:
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


if __name__ == "__main__":
    print(";)")