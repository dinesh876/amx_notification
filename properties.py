import yaml 

def read_yaml(file_path):
    with open(file_path,"r") as f:
        return yaml.safe_load(f)

config = read_yaml("properties.yaml")

DB_HOST = config["DATABASE"]["HOST"]
DB_USERNAME = config["DATABASE"]["USERNAME"]
DB_PASSWORD = config["DATABASE"]["PASSWORD"]
DB_PORT = config["DATABASE"]["PORT"]
DATABASE = config["DATABASE"]["DB"]

