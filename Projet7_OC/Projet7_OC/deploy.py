import subprocess
import yaml
# script qui lit le fichier yaml, print le nom des étapes puis les exécute
# Load the YAML file
with open('deploy.yml', 'r') as yml_file:
    data = yaml.safe_load(yml_file)

deployment_steps = data.get('deployment_steps', [])
for step in deployment_steps:
    name = step.get('name', 'N/A')
    command = step.get('command', 'N/A')
    print(f"Step Name: {name}")
    print(f"Command: {command}")
    print('-' * 20)

    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed with error: {e}")


