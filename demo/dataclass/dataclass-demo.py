# populate_dataclass_file.py
from jinja2 import Template
from dataclasses import dataclass, asdict
from typing import List

# Load template from file
with open("../input.txt.j2") as f:
    template_str = f.read()
template = Template(template_str)


@dataclass
class Particle:
    name: str
    mass: float
    charge: float


@dataclass
class Simulation:
    time_step: float
    polynomial_order: int
    particles: List[Particle]
    export_currents: bool


# Example data
sim = Simulation(
    time_step=0.01,
    polynomial_order=3,
    particles=[
        Particle(name="'electron'", mass=9.11e-31, charge=-1.6e-19),
        Particle(name="'proton'", mass=1.67e-27, charge=1.6e-19),
    ],
    export_currents=True,
)

# Render template and save
output = template.render(**asdict(sim))
with open("input_dataclass.txt", "w") as f:
    f.write(output)

print("Input file created using dataclass from template file!")
