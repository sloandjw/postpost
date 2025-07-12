import yaml

def load_rules(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)
