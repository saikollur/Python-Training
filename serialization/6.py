import json

with open("config.json", 'r') as file:
    config = json.load(file)
    print("Current Configuration")
    print(config)

print("\nUpdating configuration...")

config["theme"] = "light"
config["version"] = 1.2
config["users"] += 200
config["notifications"] = True

with open("config.json", 'w') as file:
    json.dump(config, file)

with open("config.json", 'r') as file:
    print(file.read())

print("\nConfiguration updated and saved!")
