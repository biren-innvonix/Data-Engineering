# import cowsay

# cowsay.cow("good moooooring")

import configparser
config = configparser.ConfigParser()

config.read("config.ini")
host = config["database"]["host"]
port = config["database"]["port"]

print(host)
print(port)