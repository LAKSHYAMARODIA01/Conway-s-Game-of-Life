def save_pattern_to_file(filename, live_cells):
    with open(filename, 'w') as f:
        f.write("# Saved Pattern\n")
        for x, y in live_cells:
            f.write(f"{x},{y}\n")

def load_pattern_from_file(filename):
    live_cells = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                parts = line.split(',')
                if len(parts) != 2:
                    continue
                x, y = int(parts[0]), int(parts[1])
                live_cells.append((x, y))
    except FileNotFoundError:
        print(f"Pattern file not found: {filename}")
    return live_cells
