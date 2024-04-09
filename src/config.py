import yaml

with open("config.yaml", "r") as stream:
    config = yaml.safe_load(stream)

PORT = config["port"]

DB_PATH = config["data_storage"]
DB_SCHEMA = config["data_schema"]
