# populate_yaml_file.py
import yaml
from jinja2 import Template

# Load template from file
with open("../input.txt.j2") as f:
    template_str = f.read()
template = Template(template_str)
# Could load template directly from package data!

# Load YAML data
with open("simulation.yaml") as f:
    data = yaml.safe_load(f)

# Render template and save output
output = template.render(data)
with open("input_yaml.txt", "w") as f:
    f.write(output)

print("Input file created using YAML from template file!")
