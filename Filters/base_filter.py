class Logger:
    def log(self, message):
        with open("firewall.log", "a") as file:
            file.write(message + "\n")


class Filter:
    def __init__(self, next_filter=None):
        self.next_filter = next_filter

    def handle(self, request):
        if self.next_filter:
            return self.next_filter.handle(request)
        return True
