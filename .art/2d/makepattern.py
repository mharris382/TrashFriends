import svgwrite
import random

def random_bezier_path():
    """Generate a random bezier path that looks vaguely floral."""
    path = "M"
    start_x, start_y = random.randint(50, 462), random.randint(50, 462)
    path += f"{start_x},{start_y} "
    for _ in range(3):  # Add 3 bezier curves
        ctrl1_x, ctrl1_y = random.randint(50, 462), random.randint(50, 462)
        ctrl2_x, ctrl2_y = random.randint(50, 462), random.randint(50, 462)
        end_x, end_y = random.randint(50, 462), random.randint(50, 462)
        path += f"C{ctrl1_x},{ctrl1_y} {ctrl2_x},{ctrl2_y} {end_x},{end_y} "
    return path

def create_floral_pattern(filename):
    """Create a tileable SVG with floral-like bezier shapes."""
    size = 512
    dwg = svgwrite.Drawing(filename, size=(size, size))
    for _ in range(10):  # Add 10 random floral shapes
        path = random_bezier_path()
        color = f"rgb({random.randint(100, 255)}, {random.randint(100, 255)}, {random.randint(100, 255)})"
        dwg.add(dwg.path(d=path, fill=color, stroke="black", stroke_width=1, fill_opacity=0.7))
    dwg.save()

# Save the SVG file
create_floral_pattern("paisley.svg")