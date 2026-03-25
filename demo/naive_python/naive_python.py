# naive_write_file.py

# Input data
time_step = 0.01
polynomial_order = 3

particles = [
    {"name": "electron", "mass": 9.11e-31, "charge": -1.6e-19},
    {"name": "proton", "mass": 1.67e-27, "charge": 1.6e-19},
]

export_currents = True

# Open output file
with open("input_naive.txt", "w") as f:
    # Simulation settings
    f.write("# Simulation Resolution\n")
    f.write(f"time_step = {time_step}\n")
    f.write(f"solution_polynomial_order = {polynomial_order}\n\n")

    # Particles
    f.write("# Particles\n")
    for i, particle in enumerate(particles, start=1):
        f.write(f"particle{i}_name = '{particle['name']}'\n")
        f.write(f"particle{i}_mass = {particle['mass']}\n")
        f.write(f"particle{i}_charge = {particle['charge']}\n\n")

    # Output settings
    f.write("# Output\n")
    f.write("print_frequency = 100\n")
    if export_currents:
        f.write("export_currents = True\n")

print("Input file created using naive Python script!")
