# hybrid_dataclass_yaml.py
from dataclasses import dataclass, field, asdict
from typing import List
import yaml
from jinja2 import Template


# Define dataclasses
@dataclass
class Particle:
    name: str
    mass: float
    charge: float


@dataclass
class Simulation:
    time_step: float = 0.01
    polynomial_order: int = 3
    particles: List[Particle] = field(
        default_factory=lambda: [
            Particle(name="electron", mass=9.11e-31, charge=-1.6e-19),
            Particle(name="proton", mass=1.67e-27, charge=1.6e-19),
        ]
    )
    export_currents: bool = False


# Load YAML overrides
with open("simulation_override.yaml") as f:
    overrides = yaml.safe_load(f)

# Create default simulation object
sim = Simulation()

# Apply overrides from YAML
for key, value in overrides.items():
    if key == "particles":
        # Replace default particles with YAML list
        sim.particles = [Particle(**p) for p in value]
    else:
        setattr(sim, key, value)

# Load Jinja2 template from file
with open("../input.txt.j2") as f:
    template_str = f.read()
template = Template(template_str)

# Render template using dataclass fields
output = template.render(
    time_step=sim.time_step,
    polynomial_order=sim.polynomial_order,
    particles=sim.particles,
    export_currents=sim.export_currents,
)

# Save output to file
with open("input_hybrid.txt", "w") as f:
    f.write(output)

print("Input file created using hybrid dataclass + YAML!")
