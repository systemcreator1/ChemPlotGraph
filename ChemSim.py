import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import tkinter as tk
from tkinter import simpledialog, messagebox

# Core Functions
def create_atom_model(element, atomic_number):
    """
    Creates a 3D model of an atom with a nucleus and electron shells.

    Parameters:
        element (str): Symbol of the element.
        atomic_number (int): Atomic number of the element.
    """
    fig = plt.figure(figsize=(16, 8))

    # Subplot 1: Atomic model
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.set_title(f"Atomic Model of {element} (Z = {atomic_number})", fontsize=14)

    # Nucleus representation (a sphere at the center)
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = 0.1 * np.outer(np.cos(u), np.sin(v))
    y = 0.1 * np.outer(np.sin(u), np.sin(v))
    z = 0.1 * np.outer(np.ones(np.size(u)), np.cos(v))
    ax1.plot_surface(x, y, z, color='red', alpha=0.6, edgecolor='black', label='Nucleus')

    # Electron shells representation
    for i in range(1, (atomic_number // 2) + 2):
        phi = np.linspace(0, 2 * np.pi, 100)
        theta = np.linspace(0, np.pi, 100)
        x_shell = i * 0.3 * np.outer(np.sin(theta), np.cos(phi))
        y_shell = i * 0.3 * np.outer(np.sin(theta), np.sin(phi))
        z_shell = i * 0.3 * np.outer(np.cos(theta), np.ones_like(phi))
        ax1.plot_wireframe(x_shell, y_shell, z_shell, color='blue', alpha=0.5, linewidth=0.3)

    # Set plot limits
    ax1.set_xlim([-2, 2])
    ax1.set_ylim([-2, 2])
    ax1.set_zlim([-2, 2])

    # Plot labels
    ax1.set_xlabel("X-axis")
    ax1.set_ylabel("Y-axis")
    ax1.set_zlabel("Z-axis")

    # Subplot 2: Particle theory representation
    ax2 = fig.add_subplot(122, projection='3d')
    ax2.set_title(f"Particle Theory of {element} (Z = {atomic_number})", fontsize=14)

    # Protons and neutrons in the nucleus
    num_protons = atomic_number
    num_neutrons = atomic_number  # Simplified assumption for stability
    num_particles = num_protons + num_neutrons

    nucleus_x = np.random.normal(0, 0.1, num_particles)
    nucleus_y = np.random.normal(0, 0.1, num_particles)
    nucleus_z = np.random.normal(0, 0.1, num_particles)

    ax2.scatter(nucleus_x[:num_protons], nucleus_y[:num_protons], nucleus_z[:num_protons], color='red', label='Protons')
    ax2.scatter(nucleus_x[num_protons:], nucleus_y[num_protons:], nucleus_z[num_protons:], color='gray', label='Neutrons')

    # Electrons
    electron_positions = []
    for i in range(1, (atomic_number // 2) + 2):
        num_electrons_in_shell = min(2 * i**2, atomic_number - len(electron_positions))
        phi = np.random.uniform(0, 2 * np.pi, num_electrons_in_shell)
        theta = np.random.uniform(0, np.pi, num_electrons_in_shell)
        r = i * 0.3

        x_electrons = r * np.sin(theta) * np.cos(phi)
        y_electrons = r * np.sin(theta) * np.sin(phi)
        z_electrons = r * np.cos(theta)

        ax2.scatter(x_electrons, y_electrons, z_electrons, color='blue', label='Electrons' if i == 1 else "")
        electron_positions.extend(zip(x_electrons, y_electrons, z_electrons))

    # Set plot limits
    ax2.set_xlim([-2, 2])
    ax2.set_ylim([-2, 2])
    ax2.set_zlim([-2, 2])

    # Plot labels
    ax2.set_xlabel("X-axis")
    ax2.set_ylabel("Y-axis")
    ax2.set_zlabel("Z-axis")

    # Add legend
    ax2.legend()

    plt.show()

def mix_elements(element1, atomic_number1, element2, atomic_number2):
    """
    Creates a combined 3D model of two elements, mixing their structures.

    Parameters:
        element1 (str): Symbol of the first element.
        atomic_number1 (int): Atomic number of the first element.
        element2 (str): Symbol of the second element.
        atomic_number2 (int): Atomic number of the second element.
    """
    combined_atomic_number = atomic_number1 + atomic_number2
    create_atom_model(f"{element1}-{element2}", combined_atomic_number)

# Periodic Table Data
PERIODIC_TABLE = {
    "H": 1, "He": 2, "Li": 3, "Be": 4, "B": 5, "C": 6, "N": 7, "O": 8, "F": 9, "Ne": 10,
    "Na": 11, "Mg": 12, "Al": 13, "Si": 14, "P": 15, "S": 16, "Cl": 17, "Ar": 18, "K": 19, "Ca": 20,
    "Sc": 21, "Ti": 22, "V": 23, "Cr": 24, "Mn": 25, "Fe": 26, "Co": 27, "Ni": 28, "Cu": 29, "Zn": 30,
    "Ga": 31, "Ge": 32, "As": 33, "Se": 34, "Br": 35, "Kr": 36, "Rb": 37, "Sr": 38, "Y": 39, "Zr": 40,
    "Nb": 41, "Mo": 42, "Tc": 43, "Ru": 44, "Rh": 45, "Pd": 46, "Ag": 47, "Cd": 48, "In": 49, "Sn": 50,
    "Sb": 51, "Te": 52, "I": 53, "Xe": 54, "Cs": 55, "Ba": 56, "La": 57, "Ce": 58, "Pr": 59, "Nd": 60,
    "Pm": 61, "Sm": 62, "Eu": 63, "Gd": 64, "Tb": 65, "Dy": 66, "Ho": 67, "Er": 68, "Tm": 69, "Yb": 70,
    "Lu": 71, "Hf": 72, "Ta": 73, "W": 74, "Re": 75, "Os": 76, "Ir": 77, "Pt": 78, "Au": 79, "Hg": 80,
    "Tl": 81, "Pb": 82, "Bi": 83, "Po": 84, "At": 85, "Rn": 86, "Fr": 87, "Ra": 88, "Ac": 89, "Th": 90,
    "Pa": 91, "U": 92, "Np": 93, "Pu": 94, "Am": 95, "Cm": 96, "Bk": 97, "Cf": 98, "Es": 99, "Fm": 100,
    "Md": 101, "No": 102, "Lr": 103
}

# GUI Implementation
def run_gui():
    # Initialize the Tkinter main window
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window

    def visualize_element():
        element = simpledialog.askstring("Element Input", "Enter the symbol of the element:", parent=root)
        if element and element.capitalize() in PERIODIC_TABLE:
            atomic_number = PERIODIC_TABLE[element.capitalize()]
            create_atom_model(element.capitalize(), atomic_number)
        else:
            messagebox.showerror("Error", "Invalid element symbol or element not found.", parent=root)

    def mix_elements_gui():
        element1 = simpledialog.askstring("Element Input", "Enter the first element symbol:", parent=root)
        element2 = simpledialog.askstring("Element Input", "Enter the second element symbol:", parent=root)

        if (
            element1 and element1.capitalize() in PERIODIC_TABLE and
            element2 and element2.capitalize() in PERIODIC_TABLE
        ):
            atomic_number1 = PERIODIC_TABLE[element1.capitalize()]
            atomic_number2 = PERIODIC_TABLE[element2.capitalize()]
            mix_elements(element1.capitalize(), atomic_number1, element2.capitalize(), atomic_number2)
        else:
            messagebox.showerror("Error", "Invalid element symbols or elements not found.", parent=root)

    # Show the main GUI window
    root.deiconify()
    root.title("ChemSim: Atomic Structure Visualizer")
    root.geometry("300x200")

    # Add buttons for user actions
    tk.Button(root, text="Visualize Element", command=visualize_element).pack(pady=10)
    tk.Button(root, text="Mix Elements", command=mix_elements_gui).pack(pady=10)
    #tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

    root.mainloop()
run_gui()
