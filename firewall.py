from logger import Logger

class Firewall:
    def __init__(self):
        self.logger = Logger()
        self.filters = None

    def configure(self, filters_chain):
        self.filters = filters_chain

    def process_request(self, request):
        if not self.filters.handle(request):
            self.logger.log(f"Blocked request from {request.ip_address}")
            return "403 Forbidden"
        return "200 OK"
