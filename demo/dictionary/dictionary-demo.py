# populate_dict_file.py
from jinja2 import Template

# Load the template from file
with open("../input.txt.j2") as f:
    template_str = f.read()
template = Template(template_str)
# Could load directly from python package data instead!

# Data as a dictionary
data = {
    "time_step": 0.01,
    "polynomial_order": 3,
    "particles": [
        {"name": "'electron'", "mass": 9.11e-31, "charge": -1.6e-19},
        {"name": "'proton'", "mass": 1.67e-27, "charge": 1.6e-19},
    ],
    "export_currents": True,
}

# Render and save output
output = template.render(**data)
with open("input_dict.txt", "w") as f:
    f.write(output)

print("Input file created using dictionary from template file!")
