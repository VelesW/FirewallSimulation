class Logger:
    def log(self, message):
        with open("firewall.log", "a") as file:
            file.write(message + "\n")
