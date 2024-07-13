import matplotlib.pyplot as plt
import numpy as np

def hexagon(a_center, b_center, size):
  
    angles = np.linspace(0, 2 * np.pi, 7)
    a_hexagon = a_center + size * np.cos(angles)
    b_hexagon = b_center + size * np.sin(angles)
    return a_hexagon, b_hexagon

def plot_hexagonal_grid(rows, cols, size=1):
    fig, ax = plt.subplots(1)
    ax.set_aspect('equal')

    for row in range(rows):
        for col in range(cols):
            a_offset = size * 3/2 * col
            b_offset = size * np.sqrt(3) * (row + 0.5 * (col % 2))
            a_hexagon, b_hexagon = hexagon(a_offset, b_offset, size)
            ax.plot(a_hexagon, b_hexagon, 'k-')
    
    plt.axis('off')
    plt.show()

plot_hexagonal_grid(4, 7)  
plot_hexagonal_grid(3, 5)  
