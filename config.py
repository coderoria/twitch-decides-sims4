import configparser
from pathlib import Path

configPath = str(Path(__file__).parent.parent.resolve())
config = configparser.ConfigParser()
config.read(configPath+"/tds.ini")
if "IRC" not in config:
    config["IRC"] = {}
    config["IRC"]["nick"] = ""
    config["IRC"]["token"] = ""
    config["IRC"]["channel"] = ""
with open(configPath+"/tds.ini", "w") as configfile:
    config.write(configfile)

def reload():
    config.read(configPath+"/tds.ini")